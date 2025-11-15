from langfuse import get_client
from dotenv import load_dotenv

load_dotenv()

langfuse = get_client()

content = "{{city}}の人口は？"

# Langfuseのプロンプトテンプレートを作成する
langfuse.create_prompt(
    name="ai-agent",
    type="chat",
    prompt=[{"role": "user", "content": content}],
    config={
        "model": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        "temperature": 1,
    },
)
