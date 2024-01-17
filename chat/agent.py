from langchain.agents import AgentExecutor, Tool
from langchain.agents.format_scratchpad import \
    format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.render import format_tool_to_openai_function

from .llm import llm
from .tools import (ChatGPTTool, DatabaseSearchTool, GoogleSearchTool,
                    PlaylistSearchTool)

tools: list[Tool] = [
    ChatGPTTool(),
    DatabaseSearchTool(),
    PlaylistSearchTool(),
    GoogleSearchTool(),
]


def get_agent_executor():
    """Get the agent"""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a very useful assistant. Your task will be to asnswer the users question. Be very friendly and professional.",
            ),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    functions = [format_tool_to_openai_function(t) for t in tools]

    llm_with_tools = llm.bind(functions=functions)

    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor
