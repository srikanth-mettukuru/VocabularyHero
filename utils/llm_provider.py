import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def get_llm(model_name: str = "gpt-4o-mini", temperature: float = 0.7):
    """
    Returns a configured LLM instance for agents.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")
    
    llm =  ChatOpenAI(
        model=model_name,
        temperature=temperature,
        openai_api_key=api_key
    )

    return llm
