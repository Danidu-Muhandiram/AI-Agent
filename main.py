# langchain is a high-level framework for building applications powered by language models.
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
# langgraph is a framework for building AI agents using a graph-based approach.
from langgraph.prebuilt import create_react_agent
# dotenv is used to load environment variables from a .env file.
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools=tools)

    print("Welcome. I am your AI Agent. Type 'exit' to quit.")
    print("You can ask questions or chat with me")

    while True:
