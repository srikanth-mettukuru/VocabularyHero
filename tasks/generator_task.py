from crewai import Task

def get_generator_task(agent):
    return Task(
        description="Generate a list of 10-15 English words starting with the letter '{alphabet}' that are educational and age-appropriate for grade {grade_level} students. Focus on words that are commonly used in school texts, enhance vocabulary, and are useful in writing and reading. Include a mix of nouns, verbs, and adjectives. Return the words as a JSON list.",
        expected_output="A JSON list of words, e.g. ['adventure', 'amazing', 'anchor']",
        agent=agent,
        output_key="word_list"
    )
