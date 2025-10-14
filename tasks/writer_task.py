from crewai import Task

def get_writer_task(agent):
    return Task(
        description=(
            "Using the vocabulary words from the previous task, write an engaging story suitable for grade {grade_level} students.\n\n"
            "FIRST: Examine the generator task output carefully:\n"
            "- If it contains JSON like {{\"error\": \"...\"}} then return: 'No story created - no vocabulary words were generated.'\n"
            "- If it contains a JSON array like [\"word1\", \"word2\", ...] then extract and use those words\n"
            "- If it's not valid JSON or empty, return: 'No story created - no vocabulary words were generated.'\n\n"
            "IF WORDS WERE GENERATED: Make sure to use ALL the generated words naturally in the context of the story.\n\n"
            "IMPORTANT: Adjust the story length based on the number of words:\n"
            "- If 1-3 words: Write 2-3 sentences (50-80 words)\n"
            "- If 4-8 words: Write a short paragraph (80-150 words)\n"
            "- If 9-15 words: Write a full short story (150-200 words)\n\n"
            "Focus on creating an age-appropriate, engaging narrative that uses each vocabulary word meaningfully.\n\n"
            "Remember: The generator output will be JSON - either an error object or an array of words. Parse it correctly!"
        ),
        expected_output="A cohesive story that uses all provided words, or an error message if no words were generated.",
        agent=agent
    )
