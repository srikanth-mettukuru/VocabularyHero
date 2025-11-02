from crewai import Agent
from utils.llm_provider import get_llm

def get_generator_agent():
    # Using gpt-4o-mini with low temperature for consistent, structured word generation
    llm = get_llm(model_name="gpt-4o-mini", temperature=0.3)
    return Agent(
        role="Vocabulary Generator",
        goal="Generate vocabulary words starting with a given alphabet suitable for the selected grade level.",
        backstory="You are a linguist who designs vocabulary lists for school students.",
        llm=llm
    )
