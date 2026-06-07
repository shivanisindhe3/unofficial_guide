# The Unofficial Guide

## Project Overview

The Unofficial Guide is a Retrieval-Augmented Generation (RAG) system that helps students search and answer questions about professor reviews and course experiences. Instead of relying on official university information, the system uses student-generated knowledge stored in local documents.

---

## Domain

The chosen domain is Computer Science professor and course reviews.

Students often want information about:

* Teaching style
* Exam difficulty
* Workload
* Projects
* Grading policies
* Office hours

This information is usually difficult to find through official university websites.

---

## Document Sources

The project uses 10 text documents:

* professor1.txt
* professor2.txt
* professor3.txt
* professor4.txt
* professor5.txt
* professor6.txt
* professor7.txt
* professor8.txt
* professor9.txt
* professor10.txt

Each document contains student-review style information about a professor and course.

---

## Chunking Strategy

Chunk Size: 500 characters

Overlap: 100 characters

Reasoning:

The documents are relatively short. A 500-character chunk preserves context while still allowing precise retrieval. Overlap ensures that important information near chunk boundaries is not lost.

---

## Sample Chunks

### Sample Chunk 1

Source: professor1.txt

Professor Name: Dr. Smith

Course: Data Structures

Students consistently praise Dr. Smith for clear and organized lectures. Exams are heavily based on lecture slides and in-class examples.

### Sample Chunk 2

Source: professor3.txt

Professor Name: Dr. Williams

Course: Introduction to Programming

Students frequently recommend this professor for beginners.

### Sample Chunk 3

Source: professor5.txt

Professor Name: Dr. Davis

Course: Software Engineering

Students praise Dr. Davis for providing detailed and useful feedback.

### Sample Chunk 4

Source: professor6.txt

Professor Name: Dr. Miller

Course: Operating Systems

Students describe this as one of the most demanding courses in the department.

### Sample Chunk 5

Source: professor10.txt

Professor Name: Dr. Anderson

Course: Machine Learning

Students frequently mention the professor's excellent office hours.

---

## Embedding Model

Model Used:

all-MiniLM-L6-v2

Reason:

* Free
* Fast
* Runs locally
* No API costs

Production Considerations:

For a production system I would evaluate:

* Retrieval accuracy
* Multilingual support
* Latency
* Cost
* Context length

---

## Retrieval Results

### Query 1

Question:

Which professor is recommended for beginners?

Top Result:

professor3.txt

Reason:

The document explicitly states that Dr. Williams is recommended for beginners.

### Query 2

Question:

Which professor has the heaviest workload?

Top Result:

professor6.txt

Reason:

The document states that the course is one of the most demanding in the department.

### Query 3

Question:

Which professor gives useful feedback?

Top Result:

professor5.txt

Reason:

The document explicitly mentions detailed and useful feedback.

---

## Grounded Generation

The system uses retrieved chunks as context.

Prompt:

"Answer using only the provided context. If the answer is not available, say that there is not enough information."

This prevents the model from relying on external knowledge.

---

## Example Responses

### Example 1

Question:

Which professor is recommended for beginners?

Answer:

Dr. Williams is recommended for beginners.

Source:

professor3.txt

### Example 2

Question:

Which professor gives useful feedback?

Answer:

Dr. Davis provides detailed and useful feedback.

Source:

professor5.txt

---

## Out-of-Scope Example

Question:

What is the university acceptance rate?

Answer:

I don't have enough information in the documents.

---

## Query Interface

The system uses a Gradio interface.

Input:

* User question

Output:

* Generated answer
* Source documents

---

## Evaluation Report

| Question                                        | Expected Answer       | System Response     | Result   |
| ----------------------------------------------- | --------------------- | ------------------- | -------- |
| Which professor is recommended for beginners?   | Dr. Williams          | Dr. Williams        | Accurate |
| Which professor has the heaviest workload?      | Dr. Miller            | Dr. Miller          | Accurate |
| Which professor emphasizes projects over exams? | Dr. Davis / Dr. Moore | Retrieved correctly | Accurate |
| Which professor gives useful feedback?          | Dr. Davis             | Dr. Davis           | Accurate |
| Which professor has lecture-based exams?        | Dr. Smith             | Dr. Smith           | Accurate |

---

## Failure Case

The retrieval system sometimes returns additional irrelevant source documents alongside the correct one.

Reason:

The dataset is very small and many reviews contain similar educational terminology. As a result, semantic similarity occasionally retrieves extra documents that are not directly related to the question.

---

## Spec Reflection

The planning document helped define chunking, retrieval, and evaluation before implementation.

One implementation difference was that most documents were short enough to become a single chunk, whereas the original plan expected multiple chunks per document.

---

## AI Usage

### Example 1

AI was used to help generate and explain the document chunking function.

I reviewed and modified the implementation to match the planned chunk size and overlap.

### Example 2

AI was used to help debug Groq API key and environment variable issues.

The final solution required manual correction of configuration mistakes.

---

## Technologies Used

* Python
* Sentence Transformers
* ChromaDB
* Groq
* Gradio
* python-dotenv
