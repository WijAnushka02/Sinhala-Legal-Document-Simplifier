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
docker compose up -d oracle chromadb redis
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

# 📚 Documentation

Detailed documentation is maintained in the [`docs/`](./docs/) folder to keep this README concise.

| Document | Description |
|---|---|
| [🔬 Research](./docs/research.md) | Problem Statement, Objectives, and Expected Outcomes |
| [🤖 AI Pipeline](./docs/ai-pipeline.md) | SLM Training, RAG Pipeline, and Evaluation Metrics |
| [🏗️ Architecture Overview](./docs/architecture-overview.md) | System Architecture and Tech Stack |
| [📱 Product Features](./docs/product.md) | Web App, IVR, Security, and Future Enhancements |
|---|---|
| [📁 File Structure](./docs/file-structure.md) | Complete project directory map with descriptions |
| [🗄️ Database Schema](./docs/database-schema.md) | Oracle DB schema, ER diagram, and error codes |
| [🔌 API Endpoints](./docs/api-endpoints.md) | Full REST API reference with request/response examples |
| [🔑 Configuration](./docs/configuration.md) | All environment variables and cloud database options |
| [🐳 Deployment](./docs/deployment.md) | Docker Compose, CI/CD, and production deployment |
| [🔐 Auth & Rate Limiting](./docs/auth-rate-limiting.md) | JWT flow, API keys, Redis rate limiting, security checklist |
| [🧪 Testing](./docs/testing.md) | Test strategy, coverage targets, and example test cases |
| [📈 Scalability](./docs/scalability.md) | Async pipeline, caching strategy, and scaling roadmap |
| [🏗️ Architecture ADR](./docs/architecture.md) | SLM/Gemini routing decision tree and ChromaDB strategy |

---

> **⚠️ Legal Disclaimer**: This system is designed to assist in understanding legal documents. It does not provide legal advice. For legal decisions, always consult official sources or a qualified legal professional.
