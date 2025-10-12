from crewai import Task

def get_glossary_task(agent):
    return Task(
        description=(
            "Create a comprehensive glossary for the vocabulary words that were generated from the first task.\n\n"
            "FIRST: Examine the generator task output carefully:\n"
            "- If it contains JSON like {{\"error\": \"...\"}} then return: 'No glossary created - no vocabulary words were generated.'\n"
            "- If it contains a JSON array like [\"word1\", \"word2\", ...] then extract and use those words\n"
            "- If it's not valid JSON or empty, return: 'No glossary created - no vocabulary words were generated.'\n\n"
            "IF WORDS WERE GENERATED: Create a glossary entry for each vocabulary word, regardless of whether a story was created.\n\n"
            "For each word, provide:\n\n"
            "1. **The word** (as a heading)\n"
            "2. **Definition**: A clear, simple definition appropriate for the grade level\n"
            "3. **Usage Analysis**: \n"
            "   - IF a story was created: Explain HOW the word functions in the story context. Don't just quote the sentence - "
            "analyze the word's role, meaning, and significance in that specific context.\n"
            "   - IF no story was created: Provide a general explanation of how this word is typically used, "
            "with example sentences and common contexts where students might encounter it.\n\n"
            "For story-based analysis, explain:\n"
            "   - What role the word plays in the sentence (subject, action, description, etc.)\n"
            "   - Why this word was chosen over simpler alternatives\n"
            "   - How the word adds meaning or depth to the story\n"
            "   - What the word reveals about the character, situation, or theme\n\n"
            "For general usage analysis, explain:\n"
            "   - Common contexts where the word appears\n"
            "   - Example sentences showing proper usage\n"
            "   - Why this word is useful for students to learn\n\n"
            "**Important**: Provide educational insight that helps students understand why and how the word works.\n\n"
            "Format as a clear, educational Markdown glossary that teaches vocabulary usage effectively.\n\n"
            "Remember: The generator output will be JSON - either an error object or an array of words. Parse it correctly!"
        ),
        expected_output=(
            "A detailed Markdown glossary with word definitions and usage analysis (either story-based or general usage), "
            "or an error message if no words were generated."
        ),
        agent=agent
    )
