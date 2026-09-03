# 🇱🇰 LankaServe AI

### Multilingual AI-Powered Public Information Assistant for Sri Lanka

> **Making essential public information easier to access — through Web, AI, and Voice.**

LankaServe AI is a multilingual AI-powered public information assistant designed to help Sri Lankan citizens access government, public-service, and sector-specific information through **Web and telephone-based interfaces**.

The system combines a **Small Language Model (SLM)**, **Gemini API**, **Retrieval-Augmented Generation (RAG)**, and an **IVR/DTMF-style navigation system** inspired by the way customers interact with telephone-based customer service systems.

Users can select their preferred language, choose a relevant service sector, and ask for or retrieve information using either a web interface or a phone-based menu.

The initial focus is on **Sinhala**, with support planned for **Tamil and English**.

---

## 📌 Problem Statement

Many citizens need information about government services, public institutions, procedures, eligibility requirements, documents, deadlines, and other essential services.

However, accessing this information can be difficult because:

* Government information is distributed across many websites and documents.
* Official documents often contain complex administrative and legal language.
* Information may not be easy to understand for ordinary citizens.
* Not everyone is comfortable navigating websites or mobile applications.
* Citizens may have limited access to reliable digital services.
* Sinhala and Tamil information access can be more challenging than English.
* Users often need to search through lengthy documents to find a single piece of information.
* Traditional telephone services usually depend on fixed menus and do not provide intelligent language understanding.

This creates a gap between **available information** and **accessible information**.

LankaServe AI aims to reduce this gap by providing a simple, multilingual interface that allows citizens to access verified public information using either a **web interface or a telephone-based interaction system**.

---

# 💡 Proposed Solution

LankaServe AI provides a unified AI-based platform where a user can:

1. Select a preferred language.
2. Select a relevant service sector.
3. Ask a question or select a service.
4. Retrieve information from verified sources.
5. Receive an easy-to-understand response.
6. Continue asking follow-up questions where supported.
7. Access the same service through Web or IVR/DTMF.

### Example

A user calls the LankaServe AI service.

```text
Welcome to LankaServe AI.

Select your language:

1. සිංහල
2. தமிழ்
3. English
```

The user presses:

```text
1
```

Then:

```text
ඔබට අවශ්‍ය සේවා අංශය තෝරන්න.

1. රජයේ සේවා
2. සෞඛ්‍ය සේවා
3. අධ්‍යාපන සේවා
4. රැකියා හා කම්කරු සේවා
5. නීතිමය තොරතුරු
6. වෙනත් සේවා
```

The user presses:

```text
5
```

The system can then provide options such as:

```text
නීතිමය තොරතුරු සඳහා,

1. පාරිභෝගික අයිතිවාසිකම්
2. කම්කරු නීති
3. රජයේ නීතිමය සේවා
4. වෙනත්
```

The user can then ask a question through supported voice interaction or select a predefined service.

---

# 🎯 Main Objectives

### 1. Improve Public Information Accessibility

Make important public information easier to find and understand.

### 2. Support Local Languages

Provide Sinhala-first access while designing the architecture for Tamil and English.

### 3. Develop a Small Language Model

Train a lightweight language model specifically for the target domain and Sinhala-language requirements.

### 4. Provide Reliable AI Responses

Use RAG and verified sources to reduce hallucinations and unsupported answers.

### 5. Provide Multiple Access Methods

Provide the same information through:

* Web application
* AI conversational interface
* IVR
* DTMF/number-based navigation

### 6. Improve Information Understanding

Convert complex government, administrative, and legal information into simpler language without changing important information.

---

# 🧠 Research Component

The main research contribution of this project is the development and evaluation of a **Small Language Model for Sinhala public-service information processing**.

Instead of depending entirely on a large commercial model, LankaServe AI will investigate whether a smaller domain-focused model can effectively perform tasks such as:

* Sinhala text understanding
* Question classification
* Intent detection
* Information extraction
* Query reformulation
* Legal/administrative text simplification
* Public-service question answering
* Response validation

The SLM can be trained using a curated dataset containing Sinhala public-service and administrative information.

---

# 🤖 Role of Gemini API

Gemini API will be used as a supporting AI component within the system.

It will **not replace the research SLM**.

Possible Gemini responsibilities include:

* Natural-language understanding
* Response generation
* Complex query interpretation
* Document understanding
* Query expansion
* Summarization
* Answer validation
* Comparing SLM and Gemini responses
* Generating training-data candidates
* Supporting multilingual responses

The Gemini API supports API-key authentication and can be integrated using Google's SDKs or REST APIs. API credentials should remain on the backend and be stored through environment variables such as `GEMINI_API_KEY`.

For example:

```text
User Question
      ↓
Small Language Model
      ↓
RAG Retrieval
      ↓
Gemini API
      ↓
Response Validation
      ↓
Final Answer
```

This creates a **hybrid AI architecture** rather than simply building a wrapper around Gemini.

---

# 📚 Retrieval-Augmented Generation

LankaServe AI will use **RAG** to retrieve relevant information from trusted sources before generating an answer.

### Knowledge Sources

The initial knowledge base can contain:

* Government publications
* Government circulars
* Acts and regulations
* Ministry information
* Department information
* Official service instructions
* Public-service documents
* Official forms
* Government FAQs
* Other verified public information

Where possible, information should originate from official government sources.

### RAG Pipeline

```text
Official Documents
        ↓
Document Processing
        ↓
Text Extraction
        ↓
Chunking
        ↓
Embedding Generation
        ↓
Vector Database
        ↓
User Query
        ↓
Semantic Retrieval
        ↓
Relevant Information
        ↓
SLM / Gemini
        ↓
Validated Response
```

---

# 🏗️ System Architecture

```text
                              ┌─────────────────────┐
                              │        USER         │
                              └──────────┬──────────┘
                                         │
                    ┌────────────────────┼────────────────────┐
                    │                    │                    │
                    ▼                    ▼                    ▼
          ┌────────────────┐   ┌─────────────────┐   ┌─────────────────┐
          │  Web Interface │   │   Mobile/Web    │   │  Telephone/IVR  │
          │     React      │   │    Interface    │   │   DTMF System   │
          └───────┬────────┘   └────────┬────────┘   └────────┬────────┘
                  │                     │                     │
                  └─────────────────────┼─────────────────────┘
                                        ▼
                              ┌─────────────────────┐
                              │    API Gateway      │
                              │      FastAPI        │
                              └──────────┬──────────┘
                                         │
                    ┌────────────────────┼────────────────────┐
                    │                    │                    │
                    ▼                    ▼                    ▼
          ┌────────────────┐   ┌─────────────────┐   ┌─────────────────┐
          │ Language       │   │ Intent / Sector │   │ User Query      │
          │ Detection      │   │ Classification  │   │ Processing       │
          └───────┬────────┘   └────────┬────────┘   └────────┬────────┘
                  │                     │                     │
                  └─────────────────────┼─────────────────────┘
                                        ▼
                              ┌─────────────────────┐
                              │   Small Language    │
                              │       Model         │
                              │   Sinhala-focused   │
                              └──────────┬──────────┘
                                         │
                          ┌──────────────┴──────────────┐
                          │                             │
                          ▼                             ▼
                ┌──────────────────┐          ┌──────────────────┐
                │       RAG        │          │   Gemini API     │
                │ Knowledge Base   │          │                  │
                └────────┬─────────┘          └────────┬─────────┘
                         │                             │
                         ▼                             │
                ┌──────────────────┐                  │
                │ Vector Database  │                  │
                │ FAISS / Chroma   │                  │
                └────────┬─────────┘                  │
                         │                             │
                         └──────────────┬──────────────┘
                                        ▼
                              ┌─────────────────────┐
                              │ Response Validation │
                              │                     │
                              │ • Factuality       │
                              │ • Source Check      │
                              │ • Entity Check      │
                              │ • Number Check      │
                              │ • Meaning Check     │
                              └──────────┬──────────┘
                                         │
                                         ▼
                              ┌─────────────────────┐
                              │ Final Response      │
                              │                     │
                              │ Sinhala / Tamil /   │
                              │ English             │
                              └─────────────────────┘
```

---

# ☎️ IVR / DTMF Architecture

The telephone interface will follow a **number-based navigation model** similar to conventional customer-service systems.

```text
                User Calls Service
                       │
                       ▼
              ┌─────────────────┐
              │   IVR Gateway   │
              └────────┬────────┘
                       │
                       ▼
             Select Preferred Language
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Sinhala          Tamil         English
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                Select Sector
                       │
       ┌───────────────┼────────────────┐
       ▼               ▼                ▼
   Government       Healthcare       Education
       │               │                │
       └───────────────┼────────────────┘
                       ▼
                 Select Service
                       │
                       ▼
                  User Query
                       │
                       ▼
              AI Processing Layer
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
         SLM                       RAG
          │                         │
          └────────────┬────────────┘
                       ▼
                  Gemini API
                       │
                       ▼
               Response Validation
                       │
                       ▼
                 Voice Response
                       │
                       ▼
                     User
```

---

# 🔢 DTMF Interaction Example

```text
CALL
 │
 ▼
Language Selection
 │
 ├── 1 → Sinhala
 ├── 2 → Tamil
 └── 3 → English
          │
          ▼
Sector Selection
 │
 ├── 1 → Government Services
 ├── 2 → Healthcare
 ├── 3 → Education
 ├── 4 → Employment
 ├── 5 → Legal Information
 └── 6 → Other
          │
          ▼
Service Selection
          │
          ▼
AI Processing
          │
          ▼
Information Retrieval
          │
          ▼
Voice Response
```

This allows users who may not be comfortable with websites or smartphone applications to access the same information through a telephone.

---

# 🧩 Core System Components

## 1. Language Detection

Detect the user's preferred language and route the request to the appropriate processing pipeline.

Supported languages:

```text
Sinhala
Tamil
English
```

---

## 2. Sector Classification

The system categorizes user requests into relevant service sectors.

Example:

```text
Government Services
Healthcare
Education
Employment
Legal Information
Social Services
Transport
Other Public Services
```

The initial MVP should focus on a small number of sectors rather than attempting to cover every public service.

---

## 3. Intent Detection

The system identifies what the user is trying to accomplish.

Example:

```text
User:
"උප්පැන්න සහතිකයක් ලබා ගන්නේ කොහොමද?"

Intent:
BIRTH_CERTIFICATE_APPLICATION
```

Another example:

```text
User:
"රැකියා විරහිත ප්‍රතිලාභ ලබාගන්න පුළුවන්ද?"

Intent:
UNEMPLOYMENT_BENEFIT_ELIGIBILITY
```

---

# 🧠 Small Language Model Pipeline

```text
Public Service Documents
          │
          ▼
      Data Cleaning
          │
          ▼
     Sinhala Tokenization
          │
          ▼
      Dataset Creation
          │
          ▼
   Model Pre-training
          │
          ▼
    Domain Fine-tuning
          │
          ▼
   Evaluation & Testing
          │
          ▼
      SLM Deployment
```

### Possible Training Tasks

The model can be trained for:

* Text classification
* Intent classification
* Question answering
* Information extraction
* Text simplification
* Query understanding
* Response generation

---

# 📊 Dataset Structure

Example:

```json
{
  "language": "si",
  "sector": "government_services",
  "intent": "birth_certificate",
  "question": "උප්පැන්න සහතිකයක් ලබා ගන්නේ කෙසේද?",
  "context": "Official government information...",
  "answer": "අදාළ කාර්යාලය හරහා නියමිත ක්‍රියාපටිපාටිය අනුව අයදුම් කළ යුතුය.",
  "source": "Official Government Source"
}
```

Additional metadata can include:

```text
Document ID
Source URL
Publication Date
Last Verified Date
Sector
Service
Language
Entities
Requirements
Fees
Processing Time
Conditions
Exceptions
```

---

# 🔍 Information Verification

Since this system deals with public and potentially legal information, reliability is an important part of the research.

The system should validate:

### Entity Preservation

```text
Original:
Department of Immigration

Response:
Department of Immigration
```

### Number Preservation

```text
Original:
Rs. 5,000

Response:
Rs. 5,000
```

### Date Preservation

```text
Original:
30 September 2026

Response:
30 September 2026
```

### Condition Preservation

```text
Original:
Applicants must submit the application within 30 days.

Response:
The application must be submitted within 30 days.
```

The system should avoid changing:

* Dates
* Numbers
* Fees
* Eligibility conditions
* Requirements
* Obligations
* Exceptions
* Names of institutions
* Important procedures

---

# 🛠️ Technology Stack

## Artificial Intelligence / Machine Learning

* Python
* PyTorch
* Hugging Face Transformers
* SentencePiece / BPE Tokenizer
* Scikit-learn
* Gemini API
* RAG
* Sentence Embeddings
* FAISS / ChromaDB

## Backend

* Python
* FastAPI
* Pydantic
* REST API
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
* OCR for scanned documents where required

## Voice / Telephone Layer

* IVR
* DTMF
* SIP/Telephony integration
* Speech-to-Text
* Text-to-Speech

The exact telephony provider/integration can be selected during implementation based on available SLT-MOBITEL services and API/telephony access.

## DevOps

* Git
* GitHub
* Docker
* GitHub Actions
* Google Colab / GPU environment
* Linux

---

# 🏛️ High-Level Architecture

```text
                         LANKASERVE AI
                              │
       ┌──────────────────────┼──────────────────────┐
       │                      │                      │
       ▼                      ▼                      ▼
     WEB APP               IVR/DMTF             FUTURE APP
       │                      │                      │
       └──────────────────────┼──────────────────────┘
                              ▼
                       FastAPI Backend
                              │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
           Language        Intent         Query
           Detection      Detection      Processing
                │             │             │
                └─────────────┼─────────────┘
                              ▼
                     Small Language Model
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
               RAG                     Gemini API
                │                           │
                ▼                           │
          Vector Database                   │
                │                           │
                └─────────────┬─────────────┘
                              ▼
                     Response Validation
                              │
                              ▼
                     Multilingual Response
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
              Web Text                 Voice Output
```

---

# 🔐 Security Considerations

The system will process potentially sensitive user queries and therefore security will be considered throughout development.

### API Security

* API authentication
* Rate limiting
* Input validation
* CORS configuration
* Secure API endpoints

### Gemini API Key

The Gemini API key must **never be placed inside the React frontend or committed to GitHub**.

Use:

```env
GEMINI_API_KEY=your_api_key_here
```

and keep `.env` excluded through `.gitignore`.

Gemini's current documentation recommends environment variables for API keys and provides mechanisms for restricting and securing keys.

### Additional Security

* HTTPS
* Secure database credentials
* Secret management
* Logging without exposing sensitive user information
* Input sanitization
* Access control
* Abuse/rate-limit protection

---

# 📱 Web Application Features

### User Interface

```text
┌─────────────────────────────────────┐
│          🇱🇰 LankaServe AI          │
│                                     │
│  Select Language                    │
│                                     │
│  [ සිංහල ] [ தமிழ் ] [ English ]  │
│                                     │
│  Select Service                     │
│                                     │
│  [ Government ]                     │
│  [ Healthcare ]                     │
│  [ Education ]                      │
│  [ Employment ]                     │
│  [ Legal ]                          │
│                                     │
│  Ask your question...               │
│                                     │
│              [ Ask ]                │
└─────────────────────────────────────┘
```

### Response Interface

```text
Question
   ↓
AI Answer
   ↓
Relevant Source
   ↓
Important Information
   ↓
Related Questions
```

---

# 📞 Telephone Interface

The telephone version will provide:

* Language selection
* Sector selection
* Service selection
* DTMF navigation
* Voice prompts
* AI-generated responses
* Repeat option
* Return to previous menu
* Transfer/escalation option where applicable

Example:

```text
Press 1 → Sinhala
Press 2 → Tamil
Press 3 → English

Press 1 → Government Services
Press 2 → Healthcare
Press 3 → Education
Press 4 → Employment
Press 5 → Legal Information
```

---

# 🔄 Complete Request Flow

```text
                  USER
                   │
                   ▼
            Select Language
                   │
                   ▼
            Select Sector
                   │
                   ▼
             Enter Query
                   │
                   ▼
          Language Detection
                   │
                   ▼
           Intent Detection
                   │
                   ▼
          Query Understanding
                   │
                   ▼
        ┌──────────────────────┐
        │ Small Language Model │
        └──────────┬───────────┘
                   │
                   ▼
              RAG Search
                   │
                   ▼
          Retrieve Verified Data
                   │
                   ▼
             Gemini API
                   │
                   ▼
         Response Generation
                   │
                   ▼
       Meaning / Fact Validation
                   │
                   ▼
       ┌───────────┴───────────┐
       ▼                       ▼
   Web Response            Voice Response
```

---

# 📈 Evaluation

The system will be evaluated using both technical and human-centered metrics.

## SLM Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* Perplexity
* Intent classification accuracy

## RAG Evaluation

* Retrieval accuracy
* Context relevance
* Answer faithfulness
* Source attribution
* Hallucination rate

## Language Evaluation

* Semantic similarity
* Sinhala grammatical quality
* Readability
* Translation quality
* Meaning preservation

## Public-Service Evaluation

The system will specifically measure whether critical information is preserved:

```text
Entity Preservation
Number Preservation
Date Preservation
Requirement Preservation
Condition Preservation
Exception Preservation
Procedure Preservation
```

## Human Evaluation

Potential evaluators:

* University students
* Sinhala-speaking users
* Tamil-speaking users
* English-speaking users
* Domain experts where available

Participants can evaluate:

* Ease of understanding
* Accuracy
* Relevance
* Trustworthiness
* Usability
* Response clarity

---

# 🧪 Research Questions

### Primary Research Question

> **How effectively can a domain-focused Small Language Model provide accurate and understandable Sinhala public-service information compared with a general-purpose large language model?**

### Secondary Research Questions

1. How does RAG affect the factual accuracy of Sinhala public-service responses?

2. Can a hybrid SLM + Gemini architecture improve response quality?

3. How effectively can the system preserve critical information such as dates, numbers, conditions, and requirements?

4. Can an IVR/DTMF interface improve accessibility to public information for users who do not rely on web applications?

5. How does multilingual support affect the usability and accuracy of the system?

---

# 🧠 Research Contribution

The main contribution of LankaServe AI is not simply integrating Gemini.

The research focuses on:

```text
          Small Language Model
                   +
        Sinhala NLP Processing
                   +
        Public-Service Dataset
                   +
                 RAG
                   +
             Gemini API
                   +
         Response Validation
                   +
          Web + IVR Access
```

This creates an opportunity to study how **small domain-specific models can work together with large language models and verified knowledge sources** to provide accessible public information.

---

# 🚀 MVP Scope

The first version should remain manageable.

### Phase 1

Focus on:

```text
Language:
Sinhala

Sectors:
1. Government Services
2. Legal/Public Information
3. Employment

Interface:
Web Application

AI:
Small Language Model + RAG + Gemini
```

### Phase 2

Add:

```text
Tamil
English
More sectors
Document upload
Advanced RAG
Improved evaluation
```

### Phase 3

Add:

```text
IVR
DTMF
Speech-to-Text
Text-to-Speech
Telephone-based interaction
```

### Phase 4

Evaluate:

```text
SLM vs Gemini
SLM + RAG
Gemini + RAG
SLM + Gemini + RAG
```

This comparison can become an important part of the research.

---

# 📁 Project Structure

```text
LankaServe-AI/
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
│   └── chunking/
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
├── ivr/
│   ├── menus/
│   ├── dtmf/
│   ├── voice/
│   └── telephony/
│
├── validation/
│   ├── factuality.py
│   ├── entities.py
│   ├── dates.py
│   ├── numbers.py
│   └── meaning.py
│
├── evaluation/
│   ├── accuracy.py
│   ├── readability.py
│   ├── semantic_similarity.py
│   ├── rag_evaluation.py
│   └── human_evaluation.py
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
├── .gitignore
└── LICENSE
```

---

# ⚙️ Example Environment Variables

```env
GEMINI_API_KEY=your_gemini_api_key

DATABASE_URL=your_database_url

VECTOR_DB_PATH=./data/vector_db

MODEL_PATH=./model/checkpoints
```

**Never commit the real `.env` file or API keys to GitHub.**

---

# ⚠️ Responsible AI

LankaServe AI is intended to provide **information and guidance**, not to replace official authorities or qualified professionals.

The system should:

* Clearly identify the source of important information.
* Provide the date when information was last verified.
* Avoid presenting uncertain information as fact.
* Avoid inventing government procedures.
* Preserve important conditions and requirements.
* Allow users to verify information through official sources.
* Clearly indicate when the system cannot confidently answer a question.

For legal information in particular:

> **This system does not provide legal advice. It provides information intended to help users understand publicly available information. Users should consult an appropriate legal professional or official authority for legal decisions.**

---

# 🌍 Future Development

Possible future extensions include:

* Full Sinhala/Tamil/English support
* Government service directory
* Voice-based AI assistant
* WhatsApp integration
* Mobile application
* SMS-based information service
* Accessibility features
* Human-agent escalation
* Personalized service recommendations
* More government sectors
* Real-time government information updates
* Integration with additional public-service systems

---

# 📊 Expected Outcome

The final system will demonstrate a complete AI pipeline:

```text
Public Information
       ↓
Data Collection
       ↓
Sinhala Dataset
       ↓
Small Language Model
       ↓
RAG Knowledge Base
       ↓
Gemini API
       ↓
Response Validation
       ↓
Multilingual AI Assistant
       ↓
Web + IVR/DTMF
```

The project aims to demonstrate that a **small, domain-focused language model combined with retrieval, large-model assistance, and validation mechanisms can provide a practical and accessible public-information service for Sri Lankan users.**

---
