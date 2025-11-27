
# FastAPI on Codespaces (Image-based) & Render

This repo demonstrates a FastAPI service developed in GitHub Codespaces using an image-only devcontainer (no Dockerfile) and deployed to Render as a Web Service.

## Local (Codespaces)
1. Open this repo in GitHub Codespaces.
2. The devcontainer will install dependencies automatically.
3. Run:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
