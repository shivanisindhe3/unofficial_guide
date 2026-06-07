import os
import chromadb
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("professor_reviews")

groq_client = Groq(api_key=GROQ_API_KEY)


def retrieve_chunks(question, top_k=5):
    query_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    chunks = []

    for doc, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        chunks.append({
            "text": doc,
            "source": metadata["source"],
            "distance": distance
        })

    return chunks


def ask(question):
    chunks = retrieve_chunks(question)

    context = ""
    sources = []

    for chunk in chunks:
        context += f"\nSource: {chunk['source']}\n{chunk['text']}\n"
        sources.append(chunk["source"])

    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not found in the context, say:
"I don't have enough information in the documents."

Context:
{context}

Question:
{question}
"""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a grounded RAG assistant. Use only the provided documents."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "sources": list(set(sources)),
        "chunks": chunks
    }


if __name__ == "__main__":
    question = input("Ask a question: ")
    result = ask(question)

    print("\nAnswer:\n")
    print(result["answer"])

    print("\nSources:")
    for source in result["sources"]:
        print("-", source)