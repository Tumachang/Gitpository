
# Dev Containers 官方 Python 基底映像（含 VS Code 相容設定）
FROM mcr.microsoft.com/devcontainers/python:3.12

# 安裝常用工具
USER root
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      curl git build-essential && \
    rm -rf /var/lib/apt/lists/*

# 設定工作目錄（與 devcontainer.json 對應）
WORKDIR /workspaces

# 切回非 root 使用者（與 base image 預設相容）
USER vscode
