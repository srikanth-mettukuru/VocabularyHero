from crewai import Agent
from utils.llm_provider import get_llm

def get_writer_agent():
    # Using gpt-4o for superior creative writing capabilities
    llm = get_llm(model_name="gpt-4o", temperature=0.8)
    return Agent(
        role="Creative Writer",
        goal="Write engaging, age-appropriate stories that use all provided words naturally.",
        backstory="You are a creative author who writes educational stories for children and teens.",
        llm=llm
    )