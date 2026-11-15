from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the chat model the init_chat_model function is a helper function that initializes a chat model ex open ai anthropic etc
model = init_chat_model(
    "gpt-5.6-luna",
    base_url="https://foundrysurajws.services.ai.azure.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Invoke the model
print(model.invoke("What is the capital of France?"))