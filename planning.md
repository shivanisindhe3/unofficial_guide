# Planning

## Domain
Student reviews and experiences about Computer Science professors and courses. This knowledge is useful because students often want unofficial information about teaching style, workload, exams, projects, and grading before choosing a class.

## Documents
The corpus contains 10 local text documents stored in the `data/` folder:
- professor1.txt
- professor2.txt
- professor3.txt
- professor4.txt
- professor5.txt
- professor6.txt
- professor7.txt
- professor8.txt
- professor9.txt
- professor10.txt

## Chunking Strategy
I used character-based chunking with:
- Chunk size: 500 characters
- Overlap: 100 characters

The documents are short professor-review style texts, so most reviews fit into one chunk. The overlap helps preserve context if a review becomes longer and important information appears near a chunk boundary.

## Retrieval Approach
Embedding model: `all-MiniLM-L6-v2` from `sentence-transformers`.

Vector store: ChromaDB.

Top-k: 5 chunks.

This model runs locally and is free, which is useful for a student project. In a production system, I would also consider accuracy, multilingual support, latency, context length, and cost.

## Evaluation Plan
1. Question: Which professor is recommended for beginners?
   Expected answer: Dr. Williams.

2. Question: Which professor has the heaviest workload?
   Expected answer: Dr. Miller.

3. Question: Which professor emphasizes projects over exams?
   Expected answer: Dr. Davis or Dr. Moore.

4. Question: Which professor gives useful feedback?
   Expected answer: Dr. Davis.

5. Question: Which professor has exams based on lecture slides?
   Expected answer: Dr. Smith.

## Anticipated Challenges
- Some professor reviews are similar, so retrieval may return extra sources.
- Small documents may produce fewer chunks than ideal.
- The LLM may try to answer from general knowledge, so the prompt must force it to use only retrieved context.
- Source attribution must be shown clearly in every answer.

## AI Tool Plan
I used AI assistance to help structure the project and debug errors. I planned to use AI for specific tasks only:
- Generate and explain the chunking function.
- Help write ChromaDB ingestion and retrieval code.
- Help debug `.env` and Groq API key issues.
- Help create a simple Gradio interface.
- Help structure the README and evaluation report.

## Architecture
```text
Document Ingestion
        ↓
Load text files from data/
        ↓
Clean text
        ↓
Chunking: 500 characters with 100 overlap
        ↓
Embedding: all-MiniLM-L6-v2
        ↓
Vector Store: ChromaDB
        ↓
Semantic Retrieval: top 5 chunks
        ↓
Generation: Groq LLM
        ↓
Grounded Answer + Source Citations