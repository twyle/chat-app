from typing import Optional

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools import BaseTool, Tool
from langchain_community.utilities.google_search import GoogleSearchAPIWrapper


class GoogleSearchTool(BaseTool):
    name = "google_search"
    description = """
    useful when you need to to search for the latest information from the web. Use 
    this more when the latest information is requiredand the query is a generic 
    question.
    """

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        search = GoogleSearchAPIWrapper()
        return search.run(query=query)

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError()
