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

#main function
def main():
    '''create a language model object, so ChatOpenAI connects to the openAI's chat model. temperaure means 
    how models responds to inputs, higher temperature means more creative responses, lower means more focused and accurate'''

    model = ChatOpenAI(temperature=0)

    #create a empty lst of tools
    tools = []

    #create a react agent using the model and langgrapgh, agent can think and decide and respond accordingly
    agent_executor = create_react_agent(model, tools=tools)

    #basic welcome message
    print("Welcome. I am your AI Agent. Type 'exit' to quit.")
    print("You can ask questions or chat with me")

    #use true, so will continue until user types exit
    while True:
        #get user inputs
        user_input = input("You: ")
        #user exit condition
        if user_input == "exit":
            print("Goodbye!")
            break

        #prints agent without going to the next line
        print("Agent: ", end="")
        #send user messages to the agent, HumanMessage wraps user text in a message object
        #.stream() returns output piece by piece (chunks)
        #enable real-time response streaming
        for chunk in agent_executor.stream({
    "messages": [HumanMessage(content=user_input)]}):
            
            #check if chunk has agent and messages
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    #print message content without going to next line
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
 