from crewai import Task

def get_glossary_task(agent):
    return Task(
        description=(
            "Create a comprehensive glossary for the vocabulary words that were generated and used in the story "
            "from the previous tasks. For each word, provide:\n\n"
            "1. **The word** (as a heading)\n"
            "2. **Definition**: A clear, simple definition appropriate for the grade level\n"
            "3. **Usage Analysis**: Explain HOW the word functions in the story context. Don't just quote the sentence - "
            "analyze the word's role, meaning, and significance in that specific context. Explain:\n"
            "   - What role the word plays in the sentence (subject, action, description, etc.)\n"
            "   - Why this word was chosen over simpler alternatives\n"
            "   - How the word adds meaning or depth to the story\n"
            "   - What the word reveals about the character, situation, or theme\n\n"
            "**Important**: For 'Usage Analysis', provide educational insight, not just a quote. "
            "Help students understand why and how the word works in context.\n\n"
            "Format as a clear, educational Markdown glossary that teaches vocabulary usage effectively."
        ),
        expected_output=(
            "A detailed Markdown glossary where each entry includes the word, definition, and a thorough "
            "analysis of how the word functions within the story context - explaining its role, significance, "
            "and why it was effective in that particular usage."
        ),
        agent=agent
    )
