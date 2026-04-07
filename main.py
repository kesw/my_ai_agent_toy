import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool # 引入 BaseTool
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# 1. 定義一個自定義工具類別 (這就是資工系的專業寫法！)
class MySearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = "當你需要搜尋網路以獲取最新資訊時非常有用。"

    def _run(self, query: str) -> str:
        # 這裡呼叫真正的搜尋功能
        search = DuckDuckGoSearchRun()
        return search.run(query)

# 2. 實例化你的工具
search_tool = MySearchTool()

# 3. 交給 Agent
researcher = Agent(
    role='資深技術分析師',
    goal='搜尋關於 {topic} 的最新趨勢',
    backstory='你擅長從網路搜尋結果中提取關鍵資訊。',
    llm="groq/llama-3.3-70b-versatile",
    tools=[search_tool], 
    verbose=True
)

# 4. 定義任務
research_task = Task(
  description='使用搜尋工具，針對 {topic} 進行深入調查，並列出三個最關鍵的最新發展。',
  agent=researcher,
  expected_output='一份包含來源參考的繁體中文趨勢簡報。'
)

# 5. 組建 Crew 並執行
crew = Crew(
  agents=[researcher],
  tasks=[research_task],
  verbose=True
)

print("### Agent 正在上網連線中... ###")
result = crew.kickoff(inputs={'topic': 'AI Agent News?'})

print("\n\n--- 聯網搜尋結果 ---")
print(result)