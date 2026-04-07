import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

# 1. 基礎設定
# 請確定這裡填入的是你在 Groq 官網申請到的 gsk_ 開頭的那串
load_dotenv()
# os.environ["GROQ_API_KEY"] = "API_KEY_GOES_HERE"  # 替換成你的 API Key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# 2. 定義模型（加上 groq/ 前綴）
# 注意：如果你剛安裝完 litellm，這裡就能正常運作了
my_llm = "groq/llama-3.3-70b-versatile"

# 3. 創造 Agent
researcher = Agent(
  role='AI 新聞偵探',
  goal='找出關於 {topic} 的最新三大消息',
  backstory='你是一位熱愛科技的偵探，最擅長在網路上挖掘最新資訊。',
  llm=my_llm,
  verbose=True,
  allow_delegation=False # 先關閉「委派功能」，跑起來更穩定
)

# 4. 定義任務
task = Task(
  description='請列出三個關於 {topic} 的最新重點。',
  agent=researcher,
  expected_output='三點繁體中文的條列式報告。'
)

# 5. 組建小隊並執行
crew = Crew(
    agents=[researcher], 
    tasks=[task]
)

print("### 正在啟動 AI Agent，請稍候... ###")
result = crew.kickoff(inputs={'topic': 'AI Agent 2026 最新趨勢'})

# print("\n\n--- 這是你的 Agent 跑出來的成果 ---")
# print(result)