# 初始化（如果尚未 init）
git init

# 建立 README
echo "# My Codespaces Ready Repo" > README.md

# 建立資料夾與檔案
mkdir -p .devcontainer
# 依你選擇複製 devcontainer.json（方案 A 或 B）
# 若選 B，也要建立 Dockerfile（及可選 setup.sh）

git add .
git commit -m "chore: add minimal devcontainer setup for Codespaces"
git branch -M main
git remote add origin https://github.com/<your-user>/<your-repo>.git
git push -u origin main
