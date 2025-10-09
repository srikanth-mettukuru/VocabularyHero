from crewai import Agent
from utils.llm_provider import get_llm

def get_glossary_agent():
    # Using gpt-4o-mini with moderate temperature for clear, educational explanations
    llm = get_llm(model_name="gpt-4o-mini", temperature=0.4)
    return Agent(
        role="Vocabulary Explainer",
        goal="Create a glossary defining each word and explaining how it's used in the story.",
        backstory="You are a teacher who helps students learn vocabulary through examples.",
        llm=llm
    )
