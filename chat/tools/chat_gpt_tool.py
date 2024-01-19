from typing import Optional

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool

from ..llm import llm


class ChatGPTTool(BaseTool):
    name = "chat_gpt_search"
    description = """
    useful when you need to to search for information older than two years by querying chatgpt. 
    Use this tool more if the user request is a generic question and is requesting information from 
    earlier than two years ago. Use this more if the request 
    requires information from more than two years ago.
    """

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        template: str = """
        You are a very usefule search assistant. Your task is to find a very useful and satisfying answer 
        to the user question.

        User question: {query}
        """
        prompt = PromptTemplate.from_template(template=template)
        prompt_formatted_str = prompt.format_prompt(query=query)
        return llm.invoke(prompt_formatted_str)

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError()
