from dotenv import load_dotenv
load_dotenv()
from chat.agent import get_agent_executor
import sys


print('############Chat-app############')
while True:
    prompt: str = 'Enter the query or q to quit: '
    query: str = input(prompt)
    if not query:
        print('You have to enter a query')
    elif query.lower().strip() in ['q', 'quit']:
        sys.exit(0)
    else:
        res: str = get_agent_executor().invoke({"input": query})['output']
        print(res)