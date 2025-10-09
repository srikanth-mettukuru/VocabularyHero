from crewai import Task

def get_glossary_task(agent):
    return Task(
        description=(
            "Create a glossary for the vocabulary words that were generated and used in the story "
            "from the previous tasks. For each word, provide:\n"
            "1. The word\n"
            "2. Its definition in simple language\n"
            "3. How it was used in the story context\n\n"
            "Format the output as a clear, easy-to-read glossary."
        ),
        expected_output="A Markdown glossary with word meanings and their usage in the story.",
        agent=agent
    )
