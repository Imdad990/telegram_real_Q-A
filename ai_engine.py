import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

chat_model = ChatOpenAI(
    model_name="openai/gpt-3.5-turbo",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base=OPENROUTER_API_BASE,
)

def get_bot_reply(user_input: str) -> str:
    try:
        messages = [HumanMessage(content=user_input)]
        response = chat_model(messages)
        return response.content
    except Exception as e:
        return "Sorry, an error occurred while contacting the AI."
