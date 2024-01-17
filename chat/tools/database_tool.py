import os
from typing import Optional

from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.sql_database import SQLDatabase
from langchain.tools import BaseTool
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import OpenAI

from ..llm import llm


class DatabaseSearchTool(BaseTool):
    name = "search_database"
    description = """
    useful when you need to search for information from a local database especially about youtube 
    videos.
    """

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
        db = SQLDatabase.from_uri(SQLALCHEMY_DATABASE_URI)
        toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))
        agent_executor = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
        )
        agent_executor.run(query)

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError()
