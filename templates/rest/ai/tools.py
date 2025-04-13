from langchain.agents import Tool
from langchain.tools import DuckDuckGoSearchResults
from langchain.agents import AgentExecutor
from langchain.chains import ConversationChain
from ai.models import LangChainModels


class SearchTool(Tool):
    def __init__(self, llm_chatgpt_cheap):
        self.llm = llm_chatgpt_cheap
        self.search = DuckDuckGoSearchResults()

    def run(self, query: str):
        """Tool for searching with ChatGPT (cheap version)"""
        search_results = self.search.run(query)
        return search_results

    def _run(self, query: str):
        return self.run(query)

    def _arun(self, query: str):
        """Async search (currently not needed but could be used for async search functionality)"""
        return self.run(query)


class ChatTool(Tool):
    def __init__(self, llm_chatgpt):
        self.llm = llm_chatgpt
        self.conversation = ConversationChain(llm=self.llm)

    def run(self, input_text: str):
        """Tool for chatting with ChatGPT (better version)"""
        response = self.conversation.predict(input=input_text)
        return response

    def _run(self, input_text: str):
        return self.run(input_text)

    def _arun(self, input_text: str):
        """Async chat (currently not needed but could be used for async chat functionality)"""
        return self.run(input_text)
