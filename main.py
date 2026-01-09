# langchain is a high-level framework for building applications powered by language models.
# from langchain_core.messages import HumanMessage
# langgraph is a framework for building AI agents using a graph-based approach.
# from langgraph.prebuilt import create_react_agent
# dotenv is used to load environment variables from a .env file.

from dotenv import load_dotenv
#read environment variables.
import os
#make HTTP requests (calling OpenRouter API).
import requests
#convert Python objects into JSON format strings and vice versa.
import json

# Load environment variables from .env file
load_dotenv()

#@tool
#def calculator(a: float, b: float) -> str:
#   """Useful for performing basic arithmetic calculations with numbers"""
#    print("Tool has been called.")
#    return f"The sum of {a} and {b} is {a + b}"


# If API key is missing, stop the program
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OpenRouter API key is not set. Please add it to your environment variables.")

# Function to call OpenRouter API directly using requests
def call_openrouter_api(user_input):
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    # Free AI model hosted on OpenRouter
    MODEL = "tngtech/deepseek-r1t2-chimera:free"
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        raise ValueError("OpenRouter API key is not set. Please add it to your environment variables.")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        #sending JSON data
        "Content-Type": "application/json",
    }

    payload = {
        # AI model to use
        "model": MODEL,
        # Chat messages sent to the model
        "messages": [
            {"role": "user", "content": user_input} # Message is from user | user's text input
        ]
    }

    response = requests.post(url=API_URL, headers=headers, data=json.dumps(payload)) # Convert Python dict → JSON

    # Convert response JSON into Python dictionary
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")

#main function
def main():
    """
    Main chat loop:
    - Takes user input
    - Sends it to OpenRouter
    - Prints AI response
    """

  #  tools = [calculator]
  # agent_executor = create_react_agent(model, tools)


    print("Welcome. I am your AI Agent. Type 'exit' to quit.")
    print("You can ask questions or chat with me")

    # Infinite loop, chat running until user exits
    while True:
        #get user inputs
        user_input = input("You: ")
        #user exit condition
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Send user input to OpenRouter API
            response = call_openrouter_api(user_input)
            #print agent response
            print("Agent:", response["choices"][0]["message"]["content"])
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
