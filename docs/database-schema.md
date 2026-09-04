# 🗄️ Database Schema

Oracle DB is used as the primary relational database. ChromaDB is used as the vector database (separate service).

> **Note**: The ORM models in `backend/models/` use a **normalized 3-table design** for simplification sessions, which supersedes the flat schema shown below. See `backend/models/session.py` for the production schema.

## Entity Relationship Overview

```text
users ──< api_keys
users ──< simplification_sessions
users ──< uploaded_documents
simplification_sessions >── uploaded_documents
simplification_sessions ──< session_results          (1-to-1)
simplification_sessions ──< session_extracted_facts  (1-to-many)
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
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id             UUID REFERENCES users(id) ON DELETE SET NULL,
    filename            TEXT NOT NULL,
    file_path           TEXT NOT NULL,               -- server-side storage path or S3 key
    extracted_text_path TEXT,                        -- path to extracted text file (not content)
    mime_type           VARCHAR(100),
    file_size_bytes     BIGINT,
    language            VARCHAR(10) DEFAULT 'si',
    legal_category      VARCHAR(100),
    status              VARCHAR(50) DEFAULT 'pending', -- pending | processing | ready | failed
    created_at          TIMESTAMPTZ DEFAULT NOW()
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
    updated_at      TIMESTAMPTZ DEFAULT NOW(),
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
    updated_at      TIMESTAMPTZ DEFAULT NOW(),
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_chunks_source ON legal_chunks(source_id);
CREATE INDEX idx_chunks_chroma ON legal_chunks(chroma_doc_id);

-- ============================================================
-- SIMPLIFICATION SESSIONS  (core session — immutable input + status)
-- ============================================================
CREATE TABLE simplification_sessions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id         UUID REFERENCES users(id) ON DELETE SET NULL,
    document_id     UUID REFERENCES uploaded_documents(id) ON DELETE SET NULL,
    input_text      TEXT,                  -- pasted text input (if no doc upload)
    original_text   TEXT,                  -- the exact text that was processed
    language        VARCHAR(10) DEFAULT 'si',
    legal_category  VARCHAR(100),
    question        TEXT,                  -- optional user question
    status          VARCHAR(50) DEFAULT 'pending', -- pending | processing | done | error
    error_message   TEXT,
    error_code      VARCHAR(50),           -- structured error taxonomy
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_sessions_user    ON simplification_sessions(user_id);
CREATE INDEX idx_sessions_status  ON simplification_sessions(status);
CREATE INDEX idx_sessions_created ON simplification_sessions(created_at DESC);

-- ============================================================
-- SESSION RESULTS  (AI output — written once when done)
-- ============================================================
CREATE TABLE session_results (
    session_id          UUID PRIMARY KEY REFERENCES simplification_sessions(id) ON DELETE CASCADE,
    simplified_text     TEXT,
    meaning_score       FLOAT,             -- 0.0 – 1.0
    processing_time_ms  INTEGER,
    slm_used            BOOLEAN DEFAULT FALSE,
    rag_used            BOOLEAN DEFAULT FALSE,
    gemini_used         BOOLEAN DEFAULT FALSE,
    created_at          TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- SESSION EXTRACTED FACTS  (one row per fact — fully extensible)
-- ============================================================
CREATE TABLE session_extracted_facts (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id  UUID NOT NULL REFERENCES simplification_sessions(id) ON DELETE CASCADE,
    fact_type   VARCHAR(50) NOT NULL,  -- entity|condition|obligation|exception|date|number|clause_type
    fact_value  JSONB NOT NULL,
    preserved   BOOLEAN
);

CREATE INDEX idx_facts_session  ON session_extracted_facts(session_id);
CREATE INDEX idx_facts_type     ON session_extracted_facts(fact_type);

-- ============================================================
-- SESSION SOURCES  (which legal sources were retrieved by RAG)
-- ============================================================
CREATE TABLE session_sources (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id      UUID NOT NULL REFERENCES simplification_sessions(id) ON DELETE CASCADE,
    source_id       UUID NOT NULL REFERENCES legal_sources(id),
    chunk_id        UUID REFERENCES legal_chunks(id),
    relevance_score FLOAT,             -- cosine similarity score 0-1
    rank            SMALLINT           -- retrieval rank (1 = most relevant)
);

CREATE INDEX idx_session_sources_session ON session_sources(session_id);
```

## Error Code Taxonomy

| Code | Meaning |
|---|---|
| `GEMINI_TIMEOUT` | Gemini API did not respond within 30s |
| `GEMINI_RATE_LIMIT` | Gemini API quota exceeded |
| `GEMINI_CONTENT_FILTERED` | Gemini refused to process content |
| `GEMINI_FALLBACK` | Gemini failed; SLM result used instead |
| `SLM_INFERENCE_ERROR` | SLM forward pass failed |
| `OCR_FAILURE` | Could not extract text from image PDF |
| `PDF_CORRUPT` | PDF file could not be read |
| `RAG_NO_RESULTS` | No relevant chunks found in vector store |
| `VALIDATION_FAILED` | Meaning score below minimum threshold |
| `INTERNAL_ERROR` | Unexpected server error |
