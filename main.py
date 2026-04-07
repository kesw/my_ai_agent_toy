import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# --- 1. 工具設定 (維持原樣) ---
class MySearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = "搜尋網路以獲取最新資訊。"
    def _run(self, query: str) -> str:
        search = DuckDuckGoSearchRun()
        return search.run(query)

search_tool = MySearchTool()

# --- 2. 定義 Agent 團隊 ---

# Agent 1: 搜查官 (負責跑腿找資料)
researcher = Agent(
    role='技術搜查官',
    goal='針對 {topic} 搜尋最深入、最新的技術資訊',
    backstory='你是一位資深調查員，能從海量資訊中去蕪存菁，提供準確的數據。',
    llm="groq/llama-3.3-70b-versatile",
    tools=[search_tool],
    verbose=True
)

# Agent 2: 專業主編 (負責整合與文案)
editor = Agent(
    role='科技專欄主編',
    goal='將搜查官提供的原始資料，彙整成一份專業且易懂的繁體中文報告',
    backstory='你擅長捕捉技術重點，並以優雅、專業的口吻撰寫文章，確保內容符合讀者需求。',
    llm="groq/llama-3.3-70b-versatile",
    verbose=True,
    allow_delegation=False # 主編不需要再叫別人做事了
)

# --- 3. 定義任務清單 ---

# 任務 1: 搜集資料
research_task = Task(
    description='調查 {topic} 的最新三大發展，並提供具體的細節與來源。',
    expected_output='一份包含原始數據與趨勢的調查草稿。',
    agent=researcher
)

# 任務 2: 編輯報告 (設定 context，讓主編參考搜查官的成果)
edit_task = Task(
    description='根據搜查官提供的草稿，撰寫成一份結構清晰、口吻專業的繁體中文技術報告。',
    expected_output='一份美觀的 Markdown 格式繁體中文報告，包含標題、前言、三大重點與結語。',
    agent=editor,
    context=[research_task] # 重要！這行讓任務串連起來
)

# --- 4. 組建團隊並執行 ---
crew = Crew(
    agents=[researcher, editor],
    tasks=[research_task, edit_task],
    process=Process.sequential, # 循序執行：先搜查 -> 再編輯
    verbose=True
)

print("### 🚀 AI 團隊開始運作... ###")
result = crew.kickoff(inputs={'topic': '2026年 AI Agent 產業趨勢'})

print("\n\n--- 最終產出的專業報告 ---")
print(result)