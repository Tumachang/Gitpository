# FastAPI on GitHub Codespaces / Dev Containers

## Quick Start

1. Open in GitHub Codespaces (or locally with Dev Containers extension).
2. After container builds, install deps (auto via postCreateCommand).
3. Run:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
