from ai.llms import OpenAI
from ai.agents import initialize_agent, Tool
from ai.agents import AgentExecutor


class LangChainModels:
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key
        # ChatGPT better version (higher quality)
        self.llm_chatgpt = OpenAI(api_key=openai_api_key, model="gpt-4")
        self.llm_chatgpt_cheap = OpenAI(
            api_key=openai_api_key, model="gpt-3.5-turbo")  # ChatGPT cheaper version

    def get_llm_chatgpt(self):
        return self.llm_chatgpt

    def get_llm_chatgpt_cheap(self):
        return self.llm_chatgpt_cheap
