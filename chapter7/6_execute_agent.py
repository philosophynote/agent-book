from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_tavily import TavilySearch
from langfuse import get_client
from langfuse.langchain import CallbackHandler
from langchain.agents import create_agent

# 環境変数の読み込み
from dotenv import load_dotenv

load_dotenv()


langfuse = get_client()


prompt_template = langfuse.get_prompt("ai-agent", type="chat", label="latest")
temperature = prompt_template.config["temperature"]

langchain_prompt = ChatPromptTemplate(prompt_template.get_langchain_prompt())
messages = langchain_prompt.invoke({"city": "横浜"})

llm = init_chat_model(
    model=prompt_template.config["model"],
    model_provider="bedrock_converse",
    temperature=temperature,
)
tools = [TavilySearch(max_results=2, topic="general")]
# ReactAgentの実行
agent = create_agent(llm, tools=tools)

langfuse_handler = CallbackHandler()
response = agent.invoke(messages, config={"callbacks": [langfuse_handler]})
response["messages"][-1].pretty_print()
