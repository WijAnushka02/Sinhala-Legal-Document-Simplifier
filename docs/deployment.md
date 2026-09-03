# 🐳 Docker & Deployment

## Docker Compose Services

```yaml
# docker-compose.yml summary

services:

  postgres:                    # PostgreSQL 16
    image: postgres:16-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports: ["5432:5432"]

  chromadb:                    # ChromaDB vector database
    image: chromadb/chroma:latest
    volumes:
      - chroma_data:/chroma/chroma
    ports: ["8001:8000"]

  redis:                       # Redis for rate limiting + caching
    image: redis:7-alpine
    ports: ["6379:6379"]

  backend:                     # FastAPI application
    build: ./backend
    depends_on: [postgres, chromadb, redis]
    env_file: .env
    ports: ["8000:8000"]
    volumes:
      - ./uploads:/app/uploads
      - ./training/checkpoints:/app/checkpoints:ro

  frontend:                    # Vite + React (production build served by Nginx)
    build: ./frontend
    ports: ["80:80"]
    depends_on: [backend]
```

### Start Development Infrastructure

```bash
# Start only databases (backend runs locally)
docker compose up -d postgres chromadb redis

# Start full stack (all services)
docker compose up -d
```

---

## Production Deployment Options

### Option 1 — Self-Hosted VPS / Cloud VM

```bash
docker compose -f docker-compose.yml up -d
```

Recommended: add Nginx reverse proxy with SSL termination in front.

### Option 2 — Cloud Platform

| Service | Recommended Provider |
|---|---|
| Backend (FastAPI) | Google Cloud Run / Railway / Render |
| Frontend (React) | Vercel / Netlify / Cloudflare Pages |
| Database | Supabase / Neon / AWS RDS |
| Vector DB | ChromaDB (self-hosted) or Weaviate Cloud |
| Cache (Redis) | Upstash Redis / Redis Cloud |

---

## GitHub Actions CI/CD

```text
.github/workflows/
  ├── ci.yml          # On PR: lint + type-check + run tests
  └── deploy.yml      # On push to main: build → push → deploy
```

### CI Pipeline (`ci.yml`)

```yaml
on: [pull_request]
jobs:
  backend:
    steps:
      - pip install -r requirements.txt
      - pytest tests/ --cov=backend --cov-fail-under=70
      - mypy backend/
      - ruff check backend/
  frontend:
    steps:
      - npm ci
      - npm run type-check
      - npm run lint
```

### Security Scanning

```bash
# Check for known vulnerabilities in Python dependencies
pip-audit -r requirements.txt
```

---

## Backend Dockerfile (reference)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```
