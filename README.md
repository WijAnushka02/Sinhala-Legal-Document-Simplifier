# 🇱🇰 Sinhala Legal Document Simplifier

### AI-Powered Sinhala Legal Information Simplification Using a Small Language Model, RAG & Gemini API

> **Making Sri Lankan legal information easier to understand — without changing what it means.**

---

## 📌 Overview

**Sinhala Legal Document Simplifier** is an AI-powered system designed to help Sri Lankan users understand complex legal and administrative documents written in Sinhala.

The system combines a **Sinhala-focused Small Language Model (SLM)**, **Retrieval-Augmented Generation (RAG)**, and the **Gemini API** to retrieve, understand, simplify, and explain legal information while attempting to preserve the original legal meaning.

The system will be accessible through both:

* 🌐 Web Application
* ☎️ Telephone-based IVR/DTMF Interface

The telephone interface follows a menu-based interaction model similar to conventional customer-service systems. Users can select their preferred language, select a legal-information category, and access relevant information using keypad numbers.

The primary research focus is the development and evaluation of a **small language model specialized in Sinhala legal-language understanding and simplification**.

---

# ❗ Problem Statement

Sri Lankan legal documents often contain:

* Complex Sinhala terminology
* Long and formal sentences
* Legal terminology that is difficult for ordinary citizens to understand
* Multiple conditions and exceptions
* Complicated procedures
* Legal obligations and restrictions
* Important dates, deadlines, and numerical information

Although many legal documents are publicly available, **availability does not necessarily mean accessibility or understandability**.

For example, a citizen may have access to an Act, regulation, Gazette notification, or government legal document but may struggle to determine:

* What does this mean?
* What am I required to do?
* What are my rights?
* What documents are required?
* What is the deadline?
* What happens if I do not comply?
* Are there any exceptions?

Existing general-purpose AI systems can help explain such information, but they may introduce serious problems when dealing with legal content, including:

* Hallucination
* Missing important conditions
* Changing the original meaning
* Incorrect interpretation of legal terminology
* Incorrect dates or numbers
* Inventing information that does not exist in the source
* Providing confident answers without sufficient evidence

Therefore, there is a need for a system specifically designed to **simplify Sinhala legal information while preserving important legal meaning and grounding responses in verified sources**.

---

# 💡 Proposed Solution

The proposed system will provide an AI-powered platform for understanding Sinhala legal documents.

A user will be able to:

1. Select a preferred language.
2. Select a legal-information category.
3. Upload a legal document or enter legal text.
4. Ask questions about the document.
5. Retrieve relevant information from verified legal sources.
6. Receive a simplified Sinhala explanation.
7. View the original legal content alongside the simplified explanation.
8. Identify important conditions, obligations, dates, and entities.
9. Access legal information through a telephone-based IVR/DTMF interface.

The system will combine:

```text
Small Language Model
        +
Retrieval-Augmented Generation
        +
Gemini API
        +
Legal Meaning Validation
        +
Web / IVR Interface
```

---

# 🎯 Project Objectives

### Primary Objective

Develop a Sinhala-focused Small Language Model capable of assisting with the understanding and simplification of Sri Lankan legal documents while preserving important legal information.

### Secondary Objectives

* Develop a curated Sinhala legal-language dataset.
* Train a lightweight Transformer-based language model.
* Develop a legal-document processing pipeline.
* Implement Retrieval-Augmented Generation using verified legal sources.
* Integrate Gemini API as a supporting AI component.
* Detect important legal entities and information.
* Validate simplified responses against the original legal content.
* Develop a web-based interface.
* Develop a telephone-based IVR/DTMF interface.
* Evaluate the system's accuracy, readability, and meaning preservation.

---

# 🧠 Core Concept

The core concept of the project is:

> **Simplification without meaning distortion.**

The system should make legal information easier to understand while preserving:

```text
Legal Meaning
     │
     ├── Obligations
     ├── Rights
     ├── Conditions
     ├── Exceptions
     ├── Restrictions
     ├── Penalties
     ├── Dates
     ├── Numbers
     ├── Entities
     └── Procedures
```

For example:

### Original

> නියමිත කාල සීමාව තුළ අයදුම්පත ඉදිරිපත් කිරීමට අපොහොසත් වන අයදුම්කරුවෙකුට අදාළ සේවාව ලබා ගැනීම සඳහා නැවත අයදුම් කිරීමට සිදුවේ.

### Simplified

> අයදුම්පත නියමිත කාලය තුළ ලබා නොදුන්නොත්, එම සේවාව ලබා ගැනීමට නැවත අයදුම් කිරීමට සිදුවේ.

### Extracted Information

```text
Person:
Applicant

Action:
Submit application

Deadline:
Specified time period

Condition:
Application is not submitted within the required period

Consequence:
Applicant must reapply
```

The simplified version should be easier to understand without removing the important condition or consequence.

---

# 🤖 Role of the Small Language Model

The **Small Language Model (SLM)** is the main research component of this project.

Rather than relying entirely on a large commercial model, a smaller Transformer-based model will be developed and trained for Sinhala legal-language tasks.

Potential capabilities include:

* Sinhala legal text understanding
* Legal clause classification
* Intent classification
* Information extraction
* Legal text simplification
* Question understanding
* Legal question answering
* Query reformulation
* Response validation

The model will be optimized for the project's specific domain instead of attempting to become a general-purpose language model.

---

# 🔬 Small Language Model Training

The training pipeline will follow:

```text
Sri Lankan Legal Documents
            │
            ▼
      Data Collection
            │
            ▼
       Data Cleaning
            │
            ▼
      Text Extraction
            │
            ▼
 Sentence / Clause Segmentation
            │
            ▼
          Annotation
            │
            ▼
      Sinhala Dataset
            │
            ▼
         Tokenizer
            │
            ▼
     Transformer Training
            │
            ▼
      Domain Fine-tuning
            │
            ▼
        Evaluation
            │
            ▼
      Model Deployment
```

---

# 📚 Legal Dataset

The dataset will contain carefully collected and processed Sinhala legal information.

Potential sources include:

* Sri Lankan Acts
* Regulations
* Gazette notifications
* Legal notices
* Government legal documents
* Public legal information
* Official government publications
* Publicly available legal documents

Official sources should be prioritized wherever possible.

### Dataset Example

```json
{
  "language": "si",
  "category": "consumer_law",
  "clause_type": "OBLIGATION",
  "legal_text": "නියමිත කාලසීමාව තුළ අයදුම්පත ඉදිරිපත් කළ යුතුය.",
  "simplified_text": "අයදුම්පත නියමිත කාලය ඇතුළත ලබා දිය යුතුය.",
  "entities": [],
  "conditions": [],
  "exceptions": [],
  "source": "Official Legal Source"
}
```

### Dataset Fields

```text
Document ID
Original Text
Simplified Text
Language
Legal Category
Clause Type
Entities
Dates
Numbers
Conditions
Exceptions
Obligations
Source
Publication Date
Last Verified Date
```

---

# 🏷️ Legal Clause Classification

The system can classify legal statements into categories such as:

```text
OBLIGATION
RIGHT
PROHIBITION
CONDITION
EXCEPTION
PENALTY
DEADLINE
DEFINITION
PROCEDURE
ELIGIBILITY
REQUIREMENT
RESTRICTION
```

Example:

```text
"අයදුම්කරු විසින් අයදුම්පත ඉදිරිපත් කළ යුතුය."

        ↓

OBLIGATION
```

This classification can help the system understand which information must be preserved during simplification.

---

# 📖 Retrieval-Augmented Generation

The system will use **RAG** to ground AI responses in verified legal information.

Instead of allowing the AI to answer entirely from its learned knowledge:

```text
User Question
      ↓
Search Legal Knowledge Base
      ↓
Retrieve Relevant Legal Information
      ↓
SLM / Gemini
      ↓
Generate Response
```

This reduces the risk of unsupported responses and allows the system to provide the source of the information.

---

# 🔎 RAG Pipeline

```text
Official Legal Documents
          │
          ▼
    Text Extraction
          │
          ▼
      Cleaning
          │
          ▼
       Chunking
          │
          ▼
      Embeddings
          │
          ▼
    Vector Database
          │
          │
          ▼
      User Question
          │
          ▼
     Query Embedding
          │
          ▼
   Semantic Retrieval
          │
          ▼
 Relevant Legal Context
          │
          ▼
 SLM / Gemini Processing
          │
          ▼
   Response Validation
          │
          ▼
      Final Answer
```

---

# ✨ Gemini API Integration

Gemini API will be used as a **supporting component**, while the custom SLM remains the primary research component.

Potential Gemini responsibilities include:

* Complex legal-text interpretation
* Response generation
* Document understanding
* Summarization
* Query reformulation
* Multilingual processing
* Response comparison
* Response validation
* Supporting dataset generation
* Evaluation assistance

The architecture will therefore investigate a hybrid approach:

```text
             ┌────────────────────┐
             │ Small Language     │
             │ Model              │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │       RAG          │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │    Gemini API      │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Response           │
             │ Validation         │
             └────────────────────┘
```

The Gemini API key will be stored securely on the backend and must never be exposed in the frontend application or committed to GitHub.

Example:

```env
GEMINI_API_KEY=your_api_key
```

---

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

# ☎️ IVR / DTMF Interface

A telephone-based interface will allow users to access legal information using a keypad.

The interaction will follow a menu-driven model.

### Step 1 — Language Selection

```text
Welcome to Sinhala Legal Information Service.

Press 1 for Sinhala.
Press 2 for Tamil.
Press 3 for English.
```

### Step 2 — Legal Category

For example:

```text
Select the legal information category.

Press 1 for Consumer Law.
Press 2 for Labour Law.
Press 3 for Property Law.
Press 4 for General Legal Information.
Press 5 for Other Legal Information.
```

### Step 3 — Service / Topic

```text
Select the topic.

Press 1 for Rights.
Press 2 for Requirements.
Press 3 for Procedures.
Press 4 for Deadlines.
Press 5 for Penalties.
```

### Step 4 — AI Processing

```text
DTMF Input
     ↓
Language
     ↓
Legal Category
     ↓
Topic / Intent
     ↓
Legal Knowledge Base
     ↓
SLM
     ↓
RAG
     ↓
Gemini API
     ↓
Validation
     ↓
Voice Response
```

---

# 🔢 IVR System Architecture

```text
                    Incoming Call
                          │
                          ▼
                  ┌───────────────┐
                  │  IVR Gateway  │
                  └───────┬───────┘
                          │
                          ▼
                  Language Selection
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
           Sinhala       Tamil      English
              │           │           │
              └───────────┼───────────┘
                          ▼
                  Legal Category
                          │
                          ▼
                    Topic / Intent
                          │
                          ▼
                  Backend API
                          │
                          ▼
                 Legal RAG System
                          │
                          ▼
                  Small Language
                      Model
                          │
                          ▼
                     Gemini API
                          │
                          ▼
                Response Validation
                          │
                          ▼
                   Text-to-Speech
                          │
                          ▼
                     User Call
```

The exact telephony provider and integration mechanism can be selected during implementation based on the available SLT-MOBITEL telephony/IVR infrastructure and APIs.

---

# 🌐 Web Application

The web interface will provide a more detailed experience than the telephone interface.

### Main Features

* Language selection
* Legal category selection
* Legal document upload
* Text input
* Question answering
* Document simplification
* Key information extraction
* Source display
* Original vs simplified comparison
* Important condition highlighting
* Confidence / validation indicators

### Example Interface

```text
┌──────────────────────────────────────────────┐
│       🇱🇰 Sinhala Legal Document             │
│              Simplifier                     │
├──────────────────────────────────────────────┤
│                                              │
│ Language                                     │
│ [ සිංහල ] [ தமிழ் ] [ English ]             │
│                                              │
│ Legal Category                               │
│ [ Consumer Law ▼ ]                            │
│                                              │
│ Upload Document                              │
│ [ Upload PDF ]                               │
│                                              │
│ OR                                           │
│                                              │
│ Enter Legal Text                             │
│ ┌──────────────────────────────────────────┐ │
│ │                                          │ │
│ │ Paste legal text here...                 │ │
│ │                                          │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│              [ Simplify ]                    │
└──────────────────────────────────────────────┘
```

### Result

```text
┌──────────────────────┬──────────────────────┐
│ Original Legal Text  │ Simplified Sinhala   │
├──────────────────────┼──────────────────────┤
│ Complex legal       │ Easy-to-understand   │
│ sentence...         │ explanation...       │
└──────────────────────┴──────────────────────┘

Important Information

✓ Obligation
✓ Deadline
✓ Condition
✓ Exception

Source:
Official Legal Document
```

---

# 🔐 Meaning Preservation

One of the most important components of the project is **legal meaning preservation**.

The system should compare the original and simplified content.

### Validation Pipeline

```text
Original Legal Text
        │
        ├───────────────┐
        │               │
        ▼               ▼
Important Information   Simplification
Extraction              │
        │               │
        │               ▼
        │        Simplified Text
        │               │
        └───────┬───────┘
                ▼
        Comparison Engine
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
     Entities Dates    Numbers
        │       │        │
        └───────┼────────┘
                ▼
        Conditions /
        Obligations /
        Exceptions
                │
                ▼
       Meaning Preservation
             Score
```

---

# 📊 Evaluation Metrics

The system will be evaluated using multiple dimensions.

## SLM Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* Perplexity
* Intent Classification Accuracy

## RAG Evaluation

* Retrieval Accuracy
* Context Relevance
* Answer Faithfulness
* Source Accuracy
* Hallucination Rate

## Simplification Evaluation

* Semantic Similarity
* Readability
* Fluency
* Meaning Preservation
* Human Evaluation

## Legal Information Preservation

The system will specifically evaluate:

```text
Entity Preservation
Date Preservation
Number Preservation
Condition Preservation
Obligation Preservation
Exception Preservation
Requirement Preservation
Procedure Preservation
Penalty Preservation
```

---

# 🧪 Research Experiments

The project can compare several approaches.

### Experiment 1

```text
SLM
```

### Experiment 2

```text
SLM + RAG
```

### Experiment 3

```text
Gemini + RAG
```

### Experiment 4

```text
SLM + Gemini
```

### Experiment 5

```text
SLM + RAG + Gemini + Validation
```

The performance of these approaches can then be compared.

This provides a strong research component for determining whether a **hybrid architecture can improve Sinhala legal-information accessibility and accuracy**.

---

# 🔬 Research Questions

### Primary Research Question

> **How effectively can a Sinhala-focused Small Language Model simplify Sri Lankan legal documents while preserving their original legal meaning?**

### Secondary Research Questions

1. How does RAG affect the factual accuracy of Sinhala legal-information responses?

2. How does a hybrid SLM and Gemini architecture compare with Gemini-only approaches?

3. How effectively can the proposed system preserve legal obligations, conditions, exceptions, dates, and numbers?

4. Can a domain-specific Sinhala SLM provide competitive performance while requiring significantly fewer computational resources than large language models?

5. How effective is an IVR/DTMF interface for accessing simplified legal information?

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

* PostgreSQL

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

# 📁 Project Structure

```text
Sinhala-Legal-Document-Simplifier/
│
├── README.md
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── annotated/
│   └── datasets/
│
├── documents/
│   ├── extraction/
│   ├── preprocessing/
│   ├── chunking/
│   └── ocr/
│
├── tokenizer/
│   ├── train_tokenizer.py
│   └── tokenizer.model
│
├── model/
│   ├── config.py
│   ├── attention.py
│   ├── embeddings.py
│   ├── transformer.py
│   ├── model.py
│   └── inference.py
│
├── training/
│   ├── pretraining/
│   ├── fine_tuning/
│   └── checkpoints/
│
├── rag/
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── pipeline.py
│
├── gemini/
│   ├── client.py
│   ├── prompts.py
│   ├── generator.py
│   └── validator.py
│
├── legal/
│   ├── clause_classifier.py
│   ├── entity_extractor.py
│   ├── obligation_detector.py
│   ├── condition_detector.py
│   └── legal_processor.py
│
├── validation/
│   ├── meaning.py
│   ├── entities.py
│   ├── dates.py
│   ├── numbers.py
│   ├── obligations.py
│   └── conditions.py
│
├── evaluation/
│   ├── accuracy.py
│   ├── readability.py
│   ├── semantic_similarity.py
│   ├── factuality.py
│   └── human_evaluation.py
│
├── ivr/
│   ├── menus/
│   ├── dtmf/
│   ├── voice/
│   └── telephony/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── models/
│   └── main.py
│
├── frontend/
│   ├── src/
│   └── ...
│
├── notebooks/
│
├── docs/
│   ├── architecture.md
│   ├── dataset.md
│   ├── methodology.md
│   └── evaluation.md
│
├── tests/
│
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# 🚀 Development Roadmap

## Phase 1 — Research & Data Collection

* Identify the initial legal domain.
* Collect publicly available legal documents.
* Prioritize official sources.
* Extract Sinhala text.
* Clean and preprocess the dataset.
* Develop annotation guidelines.

## Phase 2 — Dataset & SLM

* Develop Sinhala tokenizer.
* Create training dataset.
* Implement Transformer architecture.
* Train initial SLM.
* Fine-tune for legal-language tasks.
* Evaluate the model.

## Phase 3 — Legal RAG

* Build legal knowledge base.
* Generate embeddings.
* Create vector database.
* Implement semantic retrieval.
* Integrate retrieved legal context.

## Phase 4 — Gemini Integration

* Integrate Gemini API.
* Implement prompt engineering.
* Develop SLM + Gemini pipeline.
* Implement response validation.
* Compare SLM and Gemini outputs.

## Phase 5 — Web Application

* Develop React frontend.
* Develop FastAPI backend.
* Implement document upload.
* Implement legal-text simplification.
* Implement question answering.
* Display sources and important information.

## Phase 6 — IVR / DTMF

* Implement language selection.
* Implement legal-category navigation.
* Implement DTMF input.
* Connect telephone interface to backend.
* Implement voice responses.

## Phase 7 — Evaluation

* Evaluate SLM.
* Evaluate RAG.
* Evaluate Gemini integration.
* Evaluate meaning preservation.
* Conduct human evaluation.
* Compare experimental approaches.

---

# 🎯 Recommended MVP

To keep the project achievable, the initial version should **not attempt to cover every area of Sri Lankan law**.

### Initial Scope

```text
Language:
Sinhala

Legal Domain:
One selected legal domain

Example:
Consumer Protection
OR
Labour Law
OR
Basic Legal Procedures

AI:
Small Language Model
+
RAG
+
Gemini API

Interface:
React Web Application
```

After the core system works, the project can expand into:

```text
Tamil
English
Additional legal domains
Document upload
IVR
DTMF
Voice interaction
```

---

# 🔒 Security

Security is especially important because the system may process user-provided legal documents.

### API Security

* Input validation
* Authentication
* Authorization
* Rate limiting
* CORS configuration
* Secure API endpoints

### Gemini API Security

The Gemini API key must be stored on the backend.

```text
Frontend
   │
   │ User Request
   ▼
FastAPI Backend
   │
   │ Gemini API Key
   ▼
Gemini API
```

The API key must **never** be included in:

* React source code
* GitHub repository
* Client-side JavaScript
* Public configuration files

Use environment variables:

```env
GEMINI_API_KEY=your_api_key
```

and add `.env` to `.gitignore`.

---

# ⚖️ Responsible AI & Legal Disclaimer

This system is intended to help users **understand publicly available legal information**.

It is not intended to:

* Replace lawyers
* Provide professional legal advice
* Make legal decisions
* Determine legal liability
* Predict court outcomes
* Replace official authorities

The system should clearly communicate uncertainty and provide references to the underlying legal sources whenever possible.

### User Disclaimer

> **මෙම පද්ධතිය නීතිමය උපදෙස් ලබා දීම සඳහා නොවේ. මෙහි ලබා දෙන සරල පැහැදිලි කිරීම් මුල් නීතිමය ලේඛන තේරුම් ගැනීමට සහාය වීම සඳහා පමණි. නීතිමය තීරණ ගැනීමට පෙර අදාළ නිල මූලාශ්‍ර හෝ සුදුසු නීතිමය වෘත්තිකයෙකුගෙන් උපදෙස් ලබා ගන්න.**

---

# 🌍 Future Enhancements

Possible future improvements include:

* Tamil language support
* English language support
* Additional Sri Lankan legal domains
* Voice-based legal questions
* Speech-to-Text
* Text-to-Speech
* Advanced legal entity recognition
* Legal document comparison
* Legal clause highlighting
* Citation-aware answers
* Automatic source verification
* Mobile application
* Human legal-expert escalation
* Improved Sinhala legal tokenizer
* Lightweight edge deployment

---

# 📊 Expected Outcome

The completed system will provide an end-to-end pipeline:

```text
                 Legal Documents
                       │
                       ▼
                Data Processing
                       │
                       ▼
              Sinhala Legal Dataset
                       │
                       ▼
               Small Language Model
                       │
                       ▼
                  User Query
                       │
                       ▼
               Legal RAG Retrieval
                       │
                       ▼
                  Gemini API
                       │
                       ▼
             Response Generation
                       │
                       ▼
             Meaning Validation
                       │
              ┌────────┴────────┐
              ▼                 ▼
         Web Response       Voice Response
```

The project aims to demonstrate that a **Sinhala-focused Small Language Model combined with RAG, Gemini API, and meaning-preservation techniques can make complex Sri Lankan legal information easier to understand while maintaining important legal information.**

---

# ⚡ Quick Start

> **Prerequisites**: Python 3.11+, Node.js 20+, Docker Desktop, Git

### 1 — Clone

```bash
git clone https://github.com/WijAnushka02/Sinhala-Legal-Document-Simplifier.git
cd Sinhala-Legal-Document-Simplifier
```

### 2 — Configure Environment

```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY and database credentials
```

### 3 — Start Infrastructure (Docker)

```bash
docker compose up -d postgres chromadb redis
```

### 4 — Backend

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
alembic upgrade head          # Run DB migrations
uvicorn main:app --reload --port 8000
```

### 5 — Frontend

```bash
cd frontend
npm install
npm run dev                   # Vite dev server → http://localhost:5173
```

### 6 — Verify

```
Backend API docs:  http://localhost:8000/docs
Frontend app:      http://localhost:5173
ChromaDB UI:       http://localhost:8001
```

---

# 📁 Detailed File Structure

```text
Sinhala-Legal-Document-Simplifier/
│
├── README.md                          # Project documentation (this file)
├── .env.example                       # Template for environment variables
├── .gitignore                         # Git ignore rules (includes .env, __pycache__, etc.)
├── docker-compose.yml                 # Multi-service Docker orchestration
├── requirements.txt                   # Python dependencies (pinned versions)
│
├── data/
│   ├── raw/                           # Unprocessed legal documents (PDFs, DOCXs)
│   ├── processed/                     # Cleaned, extracted plain text
│   ├── annotated/                     # Human-annotated legal clause data
│   └── datasets/
│       ├── train.jsonl                # Training dataset (JSONL format)
│       ├── val.jsonl                  # Validation dataset
│       └── test.jsonl                 # Test / held-out dataset
│
├── documents/
│   ├── extraction/
│   │   ├── pdf_extractor.py           # PyMuPDF / pdfplumber-based PDF text extraction
│   │   └── docx_extractor.py          # python-docx Word document extraction
│   ├── preprocessing/
│   │   ├── cleaner.py                 # Noise removal, Unicode normalization
│   │   └── normalizer.py             # Sinhala text normalization rules
│   ├── chunking/
│   │   ├── chunker.py                 # Sentence / clause-level chunking strategy
│   │   └── overlap.py                 # Sliding window overlap for RAG chunks
│   └── ocr/
│       └── ocr_processor.py           # Tesseract / Google Vision OCR for scanned docs
│
├── tokenizer/
│   ├── train_tokenizer.py             # BPE / SentencePiece tokenizer training script
│   ├── tokenizer.model                # Trained tokenizer model file (binary)
│   └── tokenizer_config.json          # Tokenizer vocabulary config
│
├── model/
│   ├── config.py                      # Model hyperparameter config (dims, heads, layers)
│   ├── attention.py                   # Multi-head self-attention implementation
│   ├── embeddings.py                  # Token + positional embeddings
│   ├── transformer.py                 # Transformer encoder/decoder blocks
│   ├── model.py                       # Full SLM model class (assembles above)
│   └── inference.py                   # Inference helpers (beam search, greedy decode)
│
├── training/
│   ├── pretraining/
│   │   ├── pretrain.py                # MLM / CLM pretraining loop
│   │   └── dataset.py                 # PyTorch Dataset class for pretraining
│   ├── fine_tuning/
│   │   ├── finetune_simplification.py # Fine-tuning for legal simplification task
│   │   ├── finetune_classification.py # Fine-tuning for clause classification task
│   │   └── finetune_ner.py            # Fine-tuning for legal NER task
│   └── checkpoints/                   # Saved model weights (.pt files) — git-ignored
│
├── rag/
│   ├── embeddings.py                  # Sentence embedding generation (HuggingFace / custom)
│   ├── vector_store.py                # ChromaDB / FAISS vector store wrapper
│   ├── retriever.py                   # Semantic retrieval logic (top-k nearest neighbors)
│   ├── pipeline.py                    # Full RAG pipeline: query → retrieve → augment
│   └── indexer.py                     # Script to index legal documents into vector store
│
├── gemini/
│   ├── client.py                      # Google Generative AI SDK wrapper (singleton)
│   ├── prompts.py                     # Prompt templates for each Gemini task
│   ├── generator.py                   # Response generation using Gemini API
│   └── validator.py                   # Meaning preservation validation via Gemini
│
├── legal/
│   ├── clause_classifier.py           # Legal clause type classifier (OBLIGATION, RIGHT, etc.)
│   ├── entity_extractor.py            # Named entity recognition for legal entities
│   ├── obligation_detector.py         # Obligation detection in legal text
│   ├── condition_detector.py          # Condition / exception extraction
│   └── legal_processor.py             # Orchestrates full legal text analysis pipeline
│
├── validation/
│   ├── meaning.py                     # Overall meaning preservation score
│   ├── entities.py                    # Entity preservation check (before vs. after)
│   ├── dates.py                       # Date and deadline preservation check
│   ├── numbers.py                     # Numerical value preservation check
│   ├── obligations.py                 # Obligation preservation check
│   └── conditions.py                  # Condition and exception preservation check
│
├── evaluation/
│   ├── accuracy.py                    # Classification accuracy metrics
│   ├── readability.py                 # Readability scoring (Flesch, custom Sinhala metrics)
│   ├── semantic_similarity.py         # BLEU, ROUGE, BERTScore for simplification
│   ├── factuality.py                  # Hallucination detection and factuality score
│   └── human_evaluation.py            # Human evaluation data collection and analysis
│
├── ivr/
│   ├── menus/
│   │   ├── language_menu.py           # Language selection DTMF menu
│   │   ├── category_menu.py           # Legal category DTMF menu
│   │   └── topic_menu.py              # Topic selection DTMF menu
│   ├── dtmf/
│   │   └── handler.py                 # DTMF input parsing and routing
│   ├── voice/
│   │   ├── tts.py                     # Text-to-Speech (Sinhala TTS integration)
│   │   └── audio_files/               # Pre-recorded menu audio prompts
│   └── telephony/
│       └── ivr_gateway.py             # SIP / telephony provider integration
│
├── backend/
│   ├── main.py                        # FastAPI application entry point
│   ├── config.py                      # App config (reads from .env via pydantic-settings)
│   ├── database.py                    # SQLAlchemy engine, session factory
│   ├── dependencies.py                # FastAPI dependency injection (DB session, auth)
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── router.py              # Aggregates all v1 route modules
│   │   │   ├── auth.py                # /auth/* endpoints (register, login, refresh)
│   │   │   ├── documents.py           # /documents/* endpoints (upload, process)
│   │   │   ├── simplify.py            # /simplify endpoint (core AI pipeline)
│   │   │   ├── query.py               # /query endpoint (RAG question answering)
│   │   │   ├── history.py             # /history endpoints (user session history)
│   │   │   └── health.py              # /health endpoint (liveness + readiness)
│   │
│   ├── services/
│   │   ├── auth_service.py            # JWT creation, refresh, password hashing
│   │   ├── document_service.py        # Document upload, storage, retrieval
│   │   ├── simplification_service.py  # Orchestrates SLM + RAG + Gemini + validation
│   │   ├── rag_service.py             # Manages RAG queries against ChromaDB
│   │   ├── gemini_service.py          # Wraps Gemini API calls
│   │   └── validation_service.py      # Coordinates meaning preservation validation
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py                    # SQLAlchemy User ORM model
│   │   ├── document.py                # SQLAlchemy Document ORM model
│   │   ├── session.py                 # SQLAlchemy SimplificationSession ORM model
│   │   ├── legal_source.py            # SQLAlchemy LegalSource ORM model
│   │   └── api_key.py                 # SQLAlchemy ApiKey ORM model
│   │
│   └── schemas/
│       ├── auth.py                    # Pydantic request/response schemas for auth
│       ├── document.py                # Pydantic schemas for documents
│       ├── simplify.py                # Pydantic schemas for simplification requests
│       └── query.py                   # Pydantic schemas for RAG queries
│
├── frontend/
│   ├── index.html                     # Vite HTML entry point
│   ├── vite.config.ts                 # Vite + React configuration
│   ├── tsconfig.json                  # TypeScript configuration
│   ├── package.json                   # Node.js dependencies
│   │
│   └── src/
│       ├── main.tsx                   # React application entry point
│       ├── App.tsx                    # Root component with routing
│       ├── index.css                  # Global styles and design tokens
│       │
│       ├── api/
│       │   ├── client.ts              # Axios instance (base URL, auth interceptors)
│       │   ├── auth.ts                # Auth API calls (login, register, refresh)
│       │   ├── documents.ts           # Document upload/management API calls
│       │   └── simplify.ts            # Simplification + query API calls
│       │
│       ├── components/
│       │   ├── LanguageSelector.tsx   # Language toggle (සිංහල / தமிழ் / English)
│       │   ├── CategorySelector.tsx   # Legal category dropdown
│       │   ├── DocumentUpload.tsx     # PDF/DOCX file upload dropzone
│       │   ├── TextInput.tsx          # Legal text paste/input area
│       │   ├── SimplifyButton.tsx     # Primary action button
│       │   ├── ResultPanel.tsx        # Original vs. simplified side-by-side view
│       │   ├── EntityHighlight.tsx    # Highlighted legal entity display
│       │   ├── SourceCard.tsx         # Legal source citation card
│       │   ├── ValidationBadge.tsx    # Meaning preservation confidence badge
│       │   ├── QuestionInput.tsx      # Question answering input
│       │   └── HistoryPanel.tsx       # User session history list
│       │
│       ├── pages/
│       │   ├── HomePage.tsx           # Main simplification interface
│       │   ├── LoginPage.tsx          # User login form
│       │   ├── RegisterPage.tsx       # User registration form
│       │   └── HistoryPage.tsx        # User's previous queries and results
│       │
│       ├── hooks/
│       │   ├── useAuth.ts             # Authentication state hook
│       │   ├── useSimplify.ts         # Simplification API interaction hook
│       │   └── useHistory.ts          # Session history fetch hook
│       │
│       ├── store/
│       │   └── authStore.ts           # Zustand auth state (JWT token management)
│       │
│       └── types/
│           └── index.ts               # Shared TypeScript interfaces and types
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Dataset exploration and statistics
│   ├── 02_tokenizer_training.ipynb    # Tokenizer development notebook
│   ├── 03_model_training.ipynb        # SLM training experiments
│   ├── 04_rag_experiments.ipynb       # RAG retrieval quality experiments
│   └── 05_evaluation.ipynb            # Full system evaluation notebook
│
├── docs/
│   ├── architecture.md                # Detailed system architecture document
│   ├── dataset.md                     # Dataset collection and annotation guide
│   ├── methodology.md                 # Research methodology
│   └── evaluation.md                  # Evaluation framework and metrics
│
└── tests/
    ├── conftest.py                    # Pytest fixtures (test DB, mock services)
    ├── unit/
    │   ├── test_clause_classifier.py  # Unit tests for legal clause classification
    │   ├── test_entity_extractor.py   # Unit tests for entity extraction
    │   ├── test_meaning_validator.py  # Unit tests for meaning preservation
    │   └── test_rag_retriever.py      # Unit tests for RAG retrieval
    ├── integration/
    │   ├── test_simplification_api.py # Integration tests for /simplify endpoint
    │   ├── test_auth_api.py           # Integration tests for /auth endpoints
    │   └── test_document_api.py       # Integration tests for /documents endpoints
    └── e2e/
        └── test_full_pipeline.py      # End-to-end simplification pipeline test
```

---

# 🗄️ Database Schema

PostgreSQL is used as the primary relational database. ChromaDB is used as the vector database (separate service).

## Entity Relationship Overview

```text
users ──< api_keys
users ──< simplification_sessions
users ──< uploaded_documents
simplification_sessions >── uploaded_documents
simplification_sessions ──< session_sources
legal_sources ──< session_sources
legal_sources ──< legal_chunks
```

## SQL Schema

```sql
-- ============================================================
-- USERS
-- ============================================================
CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email           VARCHAR(255) UNIQUE NOT NULL,
    password_hash   TEXT NOT NULL,
    display_name    VARCHAR(100),
    preferred_lang  VARCHAR(10) DEFAULT 'si',     -- 'si', 'ta', 'en'
    is_active       BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);

-- ============================================================
-- API KEYS  (for programmatic / developer access)
-- ============================================================
CREATE TABLE api_keys (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id     UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    key_hash    TEXT UNIQUE NOT NULL,             -- SHA-256 hash of the raw key
    name        VARCHAR(100),                     -- human label e.g. "My Script"
    last_used   TIMESTAMPTZ,
    expires_at  TIMESTAMPTZ,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_api_keys_user ON api_keys(user_id);
CREATE INDEX idx_api_keys_hash ON api_keys(key_hash);

-- ============================================================
-- UPLOADED DOCUMENTS
-- ============================================================
CREATE TABLE uploaded_documents (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id         UUID REFERENCES users(id) ON DELETE SET NULL,
    filename        TEXT NOT NULL,
    file_path       TEXT NOT NULL,               -- server-side storage path or S3 key
    mime_type       VARCHAR(100),
    file_size_bytes BIGINT,
    extracted_text  TEXT,                         -- plain text after extraction/OCR
    language        VARCHAR(10) DEFAULT 'si',
    legal_category  VARCHAR(100),
    status          VARCHAR(50) DEFAULT 'pending', -- pending | processing | ready | failed
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_docs_user ON uploaded_documents(user_id);
CREATE INDEX idx_docs_status ON uploaded_documents(status);

-- ============================================================
-- LEGAL SOURCES  (the verified knowledge base)
-- ============================================================
CREATE TABLE legal_sources (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title           TEXT NOT NULL,
    source_type     VARCHAR(100),                 -- 'act', 'regulation', 'gazette', 'notice'
    legal_category  VARCHAR(100),                 -- 'consumer_law', 'labour_law', etc.
    language        VARCHAR(10) DEFAULT 'si',
    publication_date DATE,
    last_verified   DATE,
    source_url      TEXT,
    is_active       BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- LEGAL CHUNKS  (chunked text from legal sources for RAG)
-- ============================================================
CREATE TABLE legal_chunks (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_id       UUID NOT NULL REFERENCES legal_sources(id) ON DELETE CASCADE,
    chunk_index     INTEGER NOT NULL,
    chunk_text      TEXT NOT NULL,
    clause_type     VARCHAR(100),                 -- OBLIGATION, RIGHT, CONDITION, etc.
    chroma_doc_id   TEXT,                          -- ID in the ChromaDB collection
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_chunks_source ON legal_chunks(source_id);
CREATE INDEX idx_chunks_chroma ON legal_chunks(chroma_doc_id);

-- ============================================================
-- SIMPLIFICATION SESSIONS
-- ============================================================
CREATE TABLE simplification_sessions (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id                 UUID REFERENCES users(id) ON DELETE SET NULL,
    document_id             UUID REFERENCES uploaded_documents(id) ON DELETE SET NULL,
    input_text              TEXT,                  -- pasted text input (if no doc upload)
    language                VARCHAR(10) DEFAULT 'si',
    legal_category          VARCHAR(100),
    question                TEXT,                  -- optional user question
    -- AI processing results
    simplified_text         TEXT,                  -- final simplified output
    original_text           TEXT,                  -- the exact text that was processed
    clause_types            JSONB,                 -- ["OBLIGATION", "DEADLINE"]
    entities                JSONB,                 -- extracted legal entities
    conditions              JSONB,                 -- extracted conditions
    obligations             JSONB,                 -- extracted obligations
    exceptions              JSONB,                 -- extracted exceptions
    dates                   JSONB,                 -- extracted dates / deadlines
    numbers                 JSONB,                 -- extracted numerical values
    -- validation
    meaning_score           NUMERIC(4,3),           -- 0.000 – 1.000
    entity_preserved        BOOLEAN,
    dates_preserved         BOOLEAN,
    numbers_preserved       BOOLEAN,
    -- pipeline metadata
    slm_used                BOOLEAN DEFAULT FALSE,
    rag_used                BOOLEAN DEFAULT FALSE,
    gemini_used             BOOLEAN DEFAULT FALSE,
    processing_time_ms      INTEGER,
    status                  VARCHAR(50) DEFAULT 'pending', -- pending | processing | done | error
    error_message           TEXT,
    created_at              TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_sessions_user    ON simplification_sessions(user_id);
CREATE INDEX idx_sessions_status  ON simplification_sessions(status);
CREATE INDEX idx_sessions_created ON simplification_sessions(created_at DESC);

-- ============================================================
-- SESSION SOURCES  (which legal sources were retrieved by RAG)
-- ============================================================
CREATE TABLE session_sources (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id      UUID NOT NULL REFERENCES simplification_sessions(id) ON DELETE CASCADE,
    source_id       UUID NOT NULL REFERENCES legal_sources(id),
    chunk_id        UUID REFERENCES legal_chunks(id),
    relevance_score NUMERIC(5,4),                  -- cosine similarity score 0-1
    rank            SMALLINT                        -- retrieval rank (1 = most relevant)
);

CREATE INDEX idx_session_sources_session ON session_sources(session_id);

-- ============================================================
-- RATE LIMIT BUCKETS  (token bucket per user/IP)
-- ============================================================
CREATE TABLE rate_limit_buckets (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    identifier  TEXT UNIQUE NOT NULL,              -- user_id or IP address
    tokens      INTEGER DEFAULT 60,                -- remaining tokens
    last_refill TIMESTAMPTZ DEFAULT NOW()
);
```

---

# 🔌 API Endpoints

**Base URL**: `http://localhost:8000/api/v1`

**Authentication**: Include `Authorization: Bearer <jwt_token>` header for protected routes, or `X-API-Key: <api_key>` for programmatic access.

---

## 🔑 Authentication

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/auth/register` | Public | Create a new user account |
| `POST` | `/auth/login` | Public | Obtain JWT access + refresh tokens |
| `POST` | `/auth/refresh` | Refresh token | Rotate to new access token |
| `POST` | `/auth/logout` | JWT | Invalidate refresh token |
| `GET`  | `/auth/me` | JWT | Get current user profile |

### `POST /auth/register`

```json
// Request
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "display_name": "Anushka"
}

// Response 201
{
  "id": "uuid",
  "email": "user@example.com",
  "display_name": "Anushka",
  "created_at": "2026-09-03T12:00:00Z"
}
```

### `POST /auth/login`

```json
// Request
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}

// Response 200
{
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "bearer",
  "expires_in": 900
}
```

---

## 📄 Documents

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/documents/upload` | JWT | Upload a PDF or DOCX legal document |
| `GET`  | `/documents` | JWT | List user's uploaded documents |
| `GET`  | `/documents/{id}` | JWT | Get document metadata and extracted text |
| `DELETE` | `/documents/{id}` | JWT | Delete a document |

### `POST /documents/upload`

```
Content-Type: multipart/form-data

Fields:
  file          - PDF or DOCX file (max 10 MB)
  language      - "si" | "ta" | "en"  (default: "si")
  legal_category - string (optional)

Response 202
{
  "id": "uuid",
  "filename": "consumer_act.pdf",
  "status": "processing",
  "created_at": "2026-09-03T12:00:00Z"
}
```

---

## ✨ Simplification  _(Core Endpoint)_

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/simplify` | JWT or API Key | Simplify legal text or document |
| `GET`  | `/simplify/{session_id}` | JWT or API Key | Poll / fetch completed result |

### `POST /simplify`

```json
// Request — Text Input
{
  "input_type": "text",
  "text": "නියමිත කාල සීමාව තුළ අයදුම්පත ඉදිරිපත් කිරීමට...",
  "language": "si",
  "legal_category": "consumer_law",
  "use_rag": true,
  "use_gemini": true
}

// Request — Document Input
{
  "input_type": "document",
  "document_id": "uuid",
  "language": "si",
  "legal_category": "consumer_law",
  "use_rag": true,
  "use_gemini": true
}

// Response 200
{
  "session_id": "uuid",
  "status": "done",
  "original_text": "නියමිත කාල සීමාව...",
  "simplified_text": "අයදුම්පත නියමිත කාලය ඇතුළත ලබා දිය යුතුය...",
  "clause_types": ["OBLIGATION", "DEADLINE"],
  "entities": [
    { "text": "අයදුම්කරු", "type": "PERSON_ROLE" }
  ],
  "conditions": ["Application not submitted in time"],
  "obligations": ["Applicant must reapply"],
  "exceptions": [],
  "dates": [],
  "numbers": [],
  "meaning_score": 0.94,
  "entity_preserved": true,
  "dates_preserved": true,
  "numbers_preserved": true,
  "sources": [
    {
      "source_id": "uuid",
      "title": "Consumer Protection Act No. 09 of 2003",
      "section": "Section 12",
      "relevance_score": 0.87,
      "url": "https://..."
    }
  ],
  "processing_time_ms": 2340,
  "slm_used": true,
  "rag_used": true,
  "gemini_used": true
}
```

---

## ❓ Question Answering (RAG Query)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/query` | JWT or API Key | Ask a legal question grounded in RAG |

### `POST /query`

```json
// Request
{
  "question": "ජාවාරම් නීතිය යටතේ පාරිභෝගිකයෙකුගේ අයිතිවාසිකම් මොනවාද?",
  "language": "si",
  "legal_category": "consumer_law",
  "session_id": "uuid"   // optional — provide document context
}

// Response 200
{
  "session_id": "uuid",
  "answer": "ජාවාරම් නීතිය යටතේ...",
  "sources": [...],
  "confidence": 0.89,
  "processing_time_ms": 1890
}
```

---

## 📜 History

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET`  | `/history` | JWT | List user's previous sessions (paginated) |
| `GET`  | `/history/{session_id}` | JWT | Get full session detail |
| `DELETE` | `/history/{session_id}` | JWT | Delete session record |

### `GET /history`

```
Query params:
  page      (default: 1)
  limit     (default: 20, max: 100)
  category  (optional filter)

Response 200
{
  "items": [
    {
      "session_id": "uuid",
      "simplified_text_preview": "...",
      "legal_category": "consumer_law",
      "meaning_score": 0.94,
      "created_at": "2026-09-03T12:00:00Z"
    }
  ],
  "total": 47,
  "page": 1,
  "limit": 20
}
```

---

## 🔑 API Keys (Developer Access)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST`   | `/api-keys` | JWT | Create a new API key |
| `GET`    | `/api-keys` | JWT | List user's API keys |
| `DELETE` | `/api-keys/{id}` | JWT | Revoke an API key |

---

## 🩺 Health

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | Public | Liveness check |
| `GET` | `/health/ready` | Public | Readiness check (DB + ChromaDB + Gemini) |

```json
// GET /health/ready — Response 200
{
  "status": "ready",
  "checks": {
    "database": "ok",
    "vector_store": "ok",
    "gemini_api": "ok"
  },
  "version": "1.0.0"
}
```

---

# 🔑 Configuration Reference

Copy `.env.example` to `.env`. **Never commit `.env` to Git.**

```env
# ============================================================
# APPLICATION
# ============================================================
APP_ENV=development          # development | staging | production
APP_SECRET_KEY=change-me-to-a-long-random-secret-at-least-32-chars
APP_DEBUG=true
APP_VERSION=1.0.0

# ============================================================
# BACKEND SERVER
# ============================================================
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
ALLOWED_ORIGINS=http://localhost:5173   # Comma-separated for prod

# ============================================================
# DATABASE — PostgreSQL
# (Option A: Docker Compose)
# ============================================================
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=sinhala_legal_db
POSTGRES_USER=legal_user
POSTGRES_PASSWORD=change_me_secure_password
DATABASE_URL=postgresql+asyncpg://legal_user:change_me_secure_password@localhost:5432/sinhala_legal_db

# (Option B: Cloud-managed — Supabase / Neon / Railway)
# DATABASE_URL=postgresql+asyncpg://user:password@db.supabase.co:5432/postgres
# SSL_MODE=require

# ============================================================
# VECTOR DATABASE — ChromaDB
# ============================================================
CHROMA_HOST=localhost
CHROMA_PORT=8001
CHROMA_COLLECTION_NAME=sinhala_legal_chunks

# ============================================================
# CACHE — Redis (for rate limiting and session caching)
# ============================================================
REDIS_URL=redis://localhost:6379/0

# ============================================================
# GEMINI API  ← keep secret, backend-only
# ============================================================
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-pro
GEMINI_MAX_TOKENS=4096
GEMINI_TEMPERATURE=0.1       # Low temperature for factual legal tasks

# ============================================================
# JWT AUTHENTICATION
# ============================================================
JWT_SECRET_KEY=another-long-random-secret-different-from-app-secret
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=15
JWT_REFRESH_TOKEN_EXPIRE_DAYS=30

# ============================================================
# RATE LIMITING
# ============================================================
RATE_LIMIT_SIMPLIFY_PER_MINUTE=10   # /simplify endpoint
RATE_LIMIT_QUERY_PER_MINUTE=20      # /query endpoint
RATE_LIMIT_GLOBAL_PER_MINUTE=100    # all endpoints combined

# ============================================================
# FILE STORAGE
# ============================================================
UPLOAD_DIR=./uploads           # local (dev) or S3 bucket name (prod)
MAX_UPLOAD_SIZE_MB=10
ALLOWED_MIME_TYPES=application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document

# ============================================================
# ML MODEL
# ============================================================
SLM_MODEL_PATH=./training/checkpoints/best_model.pt
SLM_MAX_LENGTH=512
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-mpnet-base-v2

# ============================================================
# LOGGING
# ============================================================
LOG_LEVEL=INFO                 # DEBUG | INFO | WARNING | ERROR
LOG_FORMAT=json                # json | text
```

---

# 🐳 Docker & Deployment

## Docker Compose Services

```yaml
# docker-compose.yml (summary)

services:

  postgres:                    # PostgreSQL 16
    image: postgres:16-alpine
    environment:
      POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD (from .env)
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  chromadb:                    # ChromaDB vector database
    image: chromadb/chroma:latest
    volumes:
      - chroma_data:/chroma/chroma
    ports:
      - "8001:8000"

  redis:                       # Redis for rate limiting + caching
    image: redis:7-alpine
    ports:
      - "6379:6379"

  backend:                     # FastAPI application
    build: ./backend
    depends_on: [postgres, chromadb, redis]
    env_file: .env
    ports:
      - "8000:8000"
    volumes:
      - ./uploads:/app/uploads
      - ./training/checkpoints:/app/checkpoints:ro

  frontend:                    # Vite + React (production build served by Nginx)
    build: ./frontend
    ports:
      - "80:80"
    depends_on: [backend]
```

## Production Deployment

```text
Option 1: Self-Hosted (VPS / Cloud VM)
  docker compose -f docker-compose.prod.yml up -d

Option 2: Cloud Hosting
  Backend  → Google Cloud Run / Railway / Render
  Frontend → Vercel / Netlify / Cloudflare Pages
  Database → Supabase / Neon / AWS RDS
  Vector DB → ChromaDB (self-hosted) or Weaviate Cloud
  Cache    → Upstash Redis
```

### GitHub Actions CI/CD

```text
.github/workflows/
  ├── ci.yml          # On PR: lint + type-check + run tests
  └── deploy.yml      # On push to main: build Docker images → push → deploy
```

```yaml
# ci.yml (summary)
on: [pull_request]
jobs:
  test:
    - Install Python deps
    - Run: pytest tests/ --cov=backend --cov-fail-under=70
    - Run: mypy backend/
    - Run: ruff check backend/
  frontend:
    - npm ci
    - npm run type-check
    - npm run lint
```

---

# 🔐 Authentication & Rate Limiting

## JWT Flow

```text
1. User POSTs credentials to /auth/login
2. Backend verifies password hash (bcrypt)
3. Backend issues:
     access_token  — short-lived (15 min),  stored in memory/JS
     refresh_token — long-lived (30 days), stored in HttpOnly cookie
4. Client sends access_token in Authorization: Bearer <token>
5. At expiry, client calls /auth/refresh (uses HttpOnly cookie)
6. Backend rotates refresh token and issues new access token
```

## API Key Flow (Developer/Programmatic Access)

```text
1. Authenticated user calls POST /api-keys → receives a raw key once (shown only once)
2. Backend stores SHA-256(raw_key) in api_keys table
3. Developer includes X-API-Key: <raw_key> on requests
4. Backend hashes incoming key and looks up the hash
```

## Rate Limiting Strategy

Using Redis token bucket per user/IP:

```text
Endpoint              Limit
──────────────────────────────────────────────────
POST /simplify        10 requests / minute / user
POST /query           20 requests / minute / user
POST /documents/upload 5 requests / minute / user
All others            100 requests / minute / user
```

Exceeded limits return:

```json
HTTP 429 Too Many Requests
{
  "detail": "Rate limit exceeded. Try again in 45 seconds.",
  "retry_after": 45
}
```

## Security Checklist

- [x] Passwords hashed with **bcrypt** (cost factor 12)
- [x] API keys stored as **SHA-256 hashes** only
- [x] JWT signed with **HS256** using a strong secret
- [x] **CORS** restricted to known origins
- [x] **Input validation** via Pydantic on all request bodies
- [x] **File type validation** (MIME check + extension check)
- [x] **SQL injection** prevented via SQLAlchemy ORM (parameterized)
- [x] **Gemini API key** never exposed to frontend
- [x] **`.env` in `.gitignore`**
- [x] Dependency **security scanning** via `pip-audit` in CI
- [x] **HTTPS** enforced in production (Nginx / cloud provider)

---

# 🧪 Testing Strategy

## Test Structure

```text
tests/
├── conftest.py              # Shared fixtures: test DB, mock Gemini, mock SLM
├── unit/                    # Fast, isolated, no external I/O
│   ├── test_clause_classifier.py
│   ├── test_entity_extractor.py
│   ├── test_meaning_validator.py
│   └── test_rag_retriever.py
├── integration/             # Tests actual DB + API (uses test DB)
│   ├── test_simplification_api.py
│   ├── test_auth_api.py
│   └── test_document_api.py
└── e2e/                     # Full pipeline tests (may call real Gemini on staging)
    └── test_full_pipeline.py
```

## Running Tests

```bash
# All tests
pytest tests/ -v

# Unit only (fast, CI)
pytest tests/unit/ -v

# With coverage report
pytest tests/ --cov=backend --cov-report=html --cov-fail-under=70

# Integration tests (requires running DB)
pytest tests/integration/ -v

# Specific test file
pytest tests/unit/test_clause_classifier.py -v
```

## Coverage Targets

| Layer | Target |
|-------|--------|
| Legal processing (clause, entity, validation) | ≥ 80% |
| API endpoints | ≥ 75% |
| Services | ≥ 70% |
| RAG pipeline | ≥ 70% |
| Overall | ≥ 70% |

## Key Test Cases

```python
# Example: test_clause_classifier.py
def test_obligation_detection():
    text = "අයදුම්කරු විසින් අයදුම්පත ඉදිරිපත් කළ යුතුය."
    result = classify_clause(text)
    assert result.clause_type == "OBLIGATION"
    assert result.confidence >= 0.8

def test_simplification_preserves_deadline():
    original = "නියමිත කාල සීමාව ඇතුළත ලබා නොදුන් විට..."
    simplified = simplify(original)
    validator = MeaningValidator()
    score = validator.validate(original, simplified)
    assert score.dates_preserved is True
    assert score.meaning_score >= 0.85
```

---

# 📈 Scalability Design

## Architecture Scaling Strategy

```text
MVP (Single Server)
  └── All services on one VM / Docker Compose

Phase 2 (Horizontal Scaling)
  ├── Backend → Multiple FastAPI replicas (Gunicorn workers or Cloud Run)
  ├── Postgres → Connection pooling via PgBouncer
  ├── ChromaDB → Dedicated server or Weaviate Cloud
  └── Redis → Upstash or ElastiCache

Phase 3 (High Load)
  ├── Message Queue (Redis Streams / Celery) for async simplification
  ├── SLM inference → dedicated GPU instance or TorchServe
  └── Document processing → background worker pool
```

## Async Processing for Heavy Requests

Long-running simplification jobs are offloaded to background workers:

```text
Client ─── POST /simplify ──► Backend API
                               │
                               ├── Returns: { session_id, status: "pending" }
                               │
                               └── Enqueues job to Redis Stream / Celery
                                        │
                                Worker picks up job
                                        │
                               SLM → RAG → Gemini → Validate
                                        │
                               Updates session in DB (status: "done")
                                        │
Client ─── GET /simplify/{session_id} ──► Returns completed result
```

## Caching Strategy

| Cache Target | TTL | Method |
|---|---|---|
| RAG retrieval results (same query) | 1 hour | Redis |
| Gemini responses (deterministic prompts) | 30 min | Redis |
| User profile data | 5 min | Redis |
| Legal source metadata | 24 hours | Redis |

## Database Optimizations

- All foreign keys are indexed
- `simplification_sessions` is indexed on `(user_id, created_at DESC)` for fast pagination
- `legal_chunks` vector search happens in ChromaDB (not PostgreSQL)
- Use `asyncpg` (async PostgreSQL driver) for non-blocking I/O in FastAPI

---

