from langchain.agents import initialize_agent
from langchain.tools import DuckDuckGoSearchResults

from app.ai.models import LangChainModels
from app.ai.tools import SearchTool, ChatTool


class LangChainAgent:
    def __init__(self, openai_api_key: str):
        self.models = LangChainModels(openai_api_key)
        self.llm_chatgpt_cheap = self.models.get_llm_chatgpt_cheap()
        self.llm_chatgpt = self.models.get_llm_chatgpt()
        self.search_tool = SearchTool(self.llm_chatgpt_cheap)
        self.chat_tool = ChatTool(self.llm_chatgpt)

        self.tools = [self.search_tool, self.chat_tool]
        self.agent = self._initialize_agent()

    def _initialize_agent(self):
        return initialize_agent(self.tools, self.llm_chatgpt, agent_type="zero-shot-react-description", verbose=True)

    def run_agent(self, input_text: str):
        """Run the agent with the given input text"""
        return self.agent.run(input_text)
