import os
import chromadb
from sentence_transformers import SentenceTransformer

DATA_FOLDER = "data"

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB setup
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("professor_reviews")


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


all_chunks = []

for filename in os.listdir(DATA_FOLDER):

    if filename.endswith(".txt"):

        filepath = os.path.join(DATA_FOLDER, filename)

        with open(filepath, "r") as f:
            text = f.read()

        chunks = chunk_text(text)

        for idx, chunk in enumerate(chunks):

            all_chunks.append(
                {
                    "id": f"{filename}_{idx}",
                    "text": chunk,
                    "source": filename
                }
            )

print(f"Total chunks: {len(all_chunks)}")

for item in all_chunks:

    embedding = model.encode(item["text"]).tolist()

    collection.add(
        ids=[item["id"]],
        embeddings=[embedding],
        documents=[item["text"]],
        metadatas=[{"source": item["source"]}]
    )

print("Documents stored in ChromaDB successfully!")