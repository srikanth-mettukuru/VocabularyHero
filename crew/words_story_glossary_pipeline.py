from crewai import Crew, Process
from agents.generator_agent import get_generator_agent
from agents.writer_agent import get_writer_agent
from agents.glossary_agent import get_glossary_agent
from tasks.generator_task import get_generator_task
from tasks.writer_task import get_writer_task
from tasks.glossary_task import get_glossary_task

def run_words_story_glossary_pipeline(character_sequence: str, grade_level: int):
    # --- Initialize agents ---
    generator_agent = get_generator_agent()
    writer_agent = get_writer_agent()
    glossary_agent = get_glossary_agent()

    # --- Initialize tasks ---
    generator_task = get_generator_task(generator_agent)
    writer_task = get_writer_task(writer_agent)
    glossary_task = get_glossary_task(glossary_agent)

    # --- Create the crew ---
    crew = Crew(
        agents=[generator_agent, writer_agent, glossary_agent],
        tasks=[generator_task, writer_task, glossary_task],
        process=Process.sequential,
        verbose=True
    )

    # --- Execute the crew with inputs ---
    inputs = {
        "character_sequence": character_sequence,
        "grade_level": grade_level
    }
    
    result = crew.kickoff(inputs=inputs)
    
    # --- Extract outputs from individual tasks ---
    # After crew execution, each task has its output available
    word_list = generator_task.output.raw if generator_task.output else None
    story_text = writer_task.output.raw if writer_task.output else None
    glossary = glossary_task.output.raw if glossary_task.output else None
    
    return {
        "word_list": word_list,
        "story_text": story_text,
        "glossary": glossary
    }
