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
│   ├── api/v1/
│   │   ├── router.py                  # Aggregates all v1 route modules
│   │   ├── auth.py                    # /auth/* endpoints (register, login, refresh)
│   │   ├── documents.py               # /documents/* endpoints (upload, process)
│   │   ├── simplify.py                # /simplify endpoint (core AI pipeline)
│   │   ├── query.py                   # /query endpoint (RAG question answering)
│   │   ├── history.py                 # /history endpoints (user session history)
│   │   ├── api_keys.py                # /api-keys endpoints (developer access)
│   │   └── health.py                  # /health endpoint (liveness + readiness)
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
│   │   ├── user.py                    # SQLAlchemy User ORM model
│   │   ├── document.py                # SQLAlchemy Document ORM model
│   │   ├── session.py                 # 3 normalized session tables
│   │   ├── legal_source.py            # SQLAlchemy LegalSource + LegalChunk ORM
│   │   └── api_key.py                 # SQLAlchemy ApiKey ORM model
│   │
│   └── schemas/
│       ├── auth.py                    # Pydantic request/response schemas for auth
│       └── simplify.py                # Pydantic schemas for simplify + query
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
│       ├── api/client.ts              # Axios instance (auth interceptors + token refresh)
│       ├── store/authStore.ts         # Zustand auth state (JWT token management)
│       ├── types/index.ts             # Shared TypeScript interfaces and types
│       └── pages/
│           ├── HomePage.tsx           # Main simplification interface
│           └── LoginPage.tsx          # User login form
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Dataset exploration and statistics
│   ├── 02_tokenizer_training.ipynb    # Tokenizer development notebook
│   ├── 03_model_training.ipynb        # SLM training experiments
│   ├── 04_rag_experiments.ipynb       # RAG retrieval quality experiments
│   └── 05_evaluation.ipynb            # Full system evaluation notebook
│
├── docs/                              # ← All detailed documentation lives here
│   ├── file-structure.md              # This file — complete project directory map
│   ├── database-schema.md             # Oracle DB schema + ER diagram
│   ├── api-endpoints.md               # Full REST API reference
│   ├── configuration.md               # All environment variables reference
│   ├── deployment.md                  # Docker, CI/CD, and production deployment
│   ├── auth-rate-limiting.md          # JWT flow, API keys, rate limiting
│   ├── testing.md                     # Test strategy, coverage targets, examples
│   ├── scalability.md                 # Scaling strategy and caching design
│   └── architecture.md                # SLM/Gemini routing ADR + ChromaDB strategy
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
