# 🏗️ System Architecture

```text
                              ┌──────────────────────┐
                              │        USER          │
                              └──────────┬───────────┘
                                         │
                    ┌────────────────────┴────────────────────┐
                    │                                         │
                    ▼                                         ▼
          ┌──────────────────┐                    ┌──────────────────┐
          │   React Web App  │                    │ Telephone / IVR  │
          │                  │                    │     DTMF         │
          └────────┬─────────┘                    └────────┬─────────┘
                   │                                       │
                   └──────────────────┬────────────────────┘
                                      ▼
                           ┌──────────────────────┐
                           │    FastAPI Backend   │
                           └──────────┬───────────┘
                                      │
                                      ▼
                           ┌──────────────────────┐
                           │ Document Processing  │
                           │                      │
                           │ • PDF Extraction    │
                           │ • OCR                │
                           │ • Cleaning           │
                           │ • Chunking           │
                           └──────────┬───────────┘
                                      │
                                      ▼
                           ┌──────────────────────┐
                           │ Legal Text Analysis  │
                           │                      │
                           │ • Clause Detection  │
                           │ • Entity Extraction │
                           │ • Intent Detection  │
                           │ • Conditions        │
                           │ • Obligations       │
                           └──────────┬───────────┘
                                      │
                         ┌────────────┴────────────┐
                         │                         │
                         ▼                         ▼
                ┌──────────────────┐     ┌──────────────────┐
                │ Small Language   │     │ Legal Knowledge  │
                │ Model            │     │ Base             │
                │                  │     │                  │
                │ Sinhala NLP      │     │ Acts             │
                │ Transformer      │     │ Regulations      │
                └────────┬─────────┘     │ Gazette          │
                         │               │ Official Sources │
                         │               └────────┬─────────┘
                         │                        │
                         │                        ▼
                         │               ┌──────────────────┐
                         │               │ Vector Database  │
                         │               │ FAISS / Chroma   │
                         │               └────────┬─────────┘
                         │                        │
                         └────────────┬───────────┘
                                      ▼
                           ┌──────────────────────┐
                           │     Gemini API      │
                           │                      │
                           │ Generation /        │
                           │ Reasoning /         │
                           │ Validation Support  │
                           └──────────┬───────────┘
                                      │
                                      ▼
                           ┌──────────────────────┐
                           │ Meaning Preservation │
                           │       Validation     │
                           │                      │
                           │ • Entities           │
                           │ • Dates              │
                           │ • Numbers            │
                           │ • Conditions         │
                           │ • Obligations        │
                           │ • Exceptions         │
                           └──────────┬───────────┘
                                      │
                                      ▼
                           ┌──────────────────────┐
                           │     Final Output     │
                           │                      │
                           │ Original Text        │
                           │ Simplified Text      │
                           │ Key Information      │
                           │ Source               │
                           └──────────────────────┘
```

---

---

# 🧩 Main System Components

```text
1. Document Processing
2. Sinhala NLP
3. Legal Clause Classification
4. Small Language Model
5. Legal Knowledge Base
6. RAG
7. Gemini API
8. Meaning Preservation Engine
9. Web Application
10. IVR / DTMF System
11. Evaluation Framework
```

---

---

# 🛠️ Technology Stack

## AI / Machine Learning

* Python
* PyTorch
* Hugging Face Transformers
* SentencePiece
* BPE Tokenization
* Scikit-learn
* Gemini API

## NLP

* Sinhala NLP
* Tokenization
* Named Entity Recognition
* Text Classification
* Semantic Similarity
* Text Simplification

## RAG

* FAISS
* ChromaDB
* Vector Embeddings
* LangChain or custom RAG pipeline

## Backend

* Python
* FastAPI
* Pydantic
* REST API

## Database

* Oracle DB

## Frontend

* React
* TypeScript
* Vite
* Tailwind CSS

## Document Processing

* PyMuPDF
* pdfplumber
* python-docx
* OCR

## Voice / Telephone

* IVR
* DTMF
* SIP / Telephony APIs
* Speech-to-Text
* Text-to-Speech

## Development / Deployment

* Git
* GitHub
* Docker
* GitHub Actions
* Google Colab / GPU Environment
* Linux

---
