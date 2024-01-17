from dotenv import load_dotenv
load_dotenv()
import chainlit as cl
from chat.agent import get_agent_executor


@cl.on_chat_start
async def start():
    cl.user_session.set('agent', get_agent_executor())

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()
    query: str = message.content
    agent_executor = cl.user_session.get('agent')
    msg.content = agent_executor.invoke({"input": query})['output']
    await msg.update()