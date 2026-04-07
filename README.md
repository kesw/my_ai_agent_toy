Markdown
# 🤖 Autonomous Tech-Scout: Multi-Agent AI System

這是一個基於 **CrewAI** 框架開發的自主型 AI 智能體（AI Agent）系統。本專案旨在利用大語言模型 (LLM) 自動化執行複雜的技術調研任務，並輸出結構化的繁體中文分析報告。

---

## 專案亮點 (Project Highlights)
- **Agentic Workflow**: 實踐了「角色設定、任務分配、目標導向」的智能體工作流。
- **High-Speed Inference**: 串接 **Groq Cloud API**，採用最新的 **Llama-3.3-70b** 模型，達成極速的響應回傳。
- **Modular Design**: 採用模組化設計，易於擴充新的 Agent 角色與工具。
- **Security Best Practices**: 使用 `.env` 管理敏感 API 金鑰，並透過 `.gitignore` 確保環境安全性。

## 技術棧 (Tech Stack)
- **核心框架**: [CrewAI](https://www.crewai.com/) (Orchestrating autonomous AI agents)
- **模型介面**: LiteLLM (Universal I/O for LLMs)
- **大語言模型**: Llama-3.3-70b-versatile (via Groq)
- **開發語言**: Python 3.12.0

## 專案結構 (Project Structure)
- `main.py`: 系統核心邏輯，包含 Agent 定義、Task 編排與 Crew 執行。
- `requirements.txt`: 專案所需的依賴套件清單，確保環境一致性。
- `.env`: (未上傳) 存放敏感的 `GROQ_API_KEY`。
- `.gitignore`: 防止虛擬環境 `.venv` 與敏感金鑰上傳至 GitHub。

## 🚀 快速開始 (Quick Start)

### 
1. 複製專案與環境準備
```bash
# 複製專案
git clone [https://github.com/你的帳號名稱/My-First-AI-Agent.git](https://github.com/你的帳號名稱/My-First-AI-Agent.git)
cd My-First-AI-Agent

# 建立並啟動虛擬環境 (建議)
python -m venv .venv
source .venv/bin/activate  # Windows 請用 .venv\Scripts\activate

2. 安裝依賴套件
Bash
pip install -r requirements.txt

3. 設定環境變數
在專案根目錄建立一個 .env 檔案，並填入你的 API Key：
GROQ_API_KEY=你的_GROQ_API_KEY_這裡

4. 運行專案
Bash
python main.py

📈 未來展望 (Future Roadmap)
[ ] 聯網能力：整合 duckduckgo-search 工具，讓 Agent 具備即時搜尋網路資訊的能力。

[ ] 多智能體協作：新增「校稿員 (Reviewer)」角色，提升輸出報告的專業度與準確性。

[ ] Web 介面：使用 Streamlit 建立簡單的 GUI 介面供非技術人員使用。