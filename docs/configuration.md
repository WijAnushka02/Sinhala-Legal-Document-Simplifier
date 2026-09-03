# 🔑 Configuration Reference

Copy `.env.example` to `.env`. **Never commit `.env` to Git.**

```bash
cp .env.example .env
```

---

## All Environment Variables

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
# Option A: Docker Compose (default)
# ============================================================
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=sinhala_legal_db
POSTGRES_USER=legal_user
POSTGRES_PASSWORD=change_me_secure_password
DATABASE_URL=postgresql+asyncpg://legal_user:change_me_secure_password@localhost:5432/sinhala_legal_db

# Option B: Cloud-managed (Supabase / Neon / Railway) — uncomment and fill:
# DATABASE_URL=postgresql+asyncpg://user:password@db.supabase.co:5432/postgres?ssl=require

# ============================================================
# VECTOR DATABASE — ChromaDB
# ============================================================
CHROMA_HOST=localhost
CHROMA_PORT=8001
CHROMA_COLLECTION_PREFIX=legal_   # Per-domain: legal_consumer_law, legal_labour_law, etc.

# ============================================================
# CACHE — Redis (rate limiting and session caching)
# ============================================================
REDIS_URL=redis://localhost:6379/0

# ============================================================
# GEMINI API  ← keep secret, backend-only
# ============================================================
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-pro

# ============================================================
# JWT AUTHENTICATION
# ============================================================
JWT_SECRET_KEY=another-long-random-secret-different-from-app-secret
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=15
JWT_REFRESH_TOKEN_EXPIRE_DAYS=30

# ============================================================
# RATE LIMITING (Redis sliding window, per user/IP per minute)
# ============================================================
RATE_LIMIT_SIMPLIFY_PER_MINUTE=10
RATE_LIMIT_QUERY_PER_MINUTE=20
RATE_LIMIT_UPLOAD_PER_MINUTE=5
RATE_LIMIT_DEFAULT_PER_MINUTE=100

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

## Cloud Database Options

### Option A — Docker Compose (Local / Self-hosted)
The default `DATABASE_URL` in `.env.example` works with `docker compose up`.

### Option B — Supabase
1. Create a project at [supabase.com](https://supabase.com)
2. Copy the **Connection string** (URI format) from Project Settings → Database
3. Set `DATABASE_URL=postgresql+asyncpg://...?ssl=require`

### Option C — Neon
1. Create a database at [neon.tech](https://neon.tech)
2. Use the provided connection string with `sslmode=require`

### Option D — Railway
1. Create a PostgreSQL service at [railway.app](https://railway.app)
2. Copy the `DATABASE_PUBLIC_URL` from the service variables

---

## Generating Strong Secrets

```bash
# Python (recommended)
python -c "import secrets; print(secrets.token_urlsafe(48))"

# OpenSSL
openssl rand -base64 48
```

Use **different values** for `APP_SECRET_KEY` and `JWT_SECRET_KEY`.
