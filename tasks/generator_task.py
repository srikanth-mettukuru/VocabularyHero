from crewai import Task

def get_generator_task(agent):
    return Task(
        description="""Your task is to find English words that start with the exact character sequence '{character_sequence}' and are appropriate for Grade {grade_level} students.

🎯 PRIMARY RULE - CHARACTER SEQUENCE MATCHING:
The word must start with EXACTLY '{character_sequence}' - character by character.

Examples:
- If sequence is 'ac': Find words starting with 'ac' like 'actor', 'acid', 'across'
- If sequence is 'acc': Find words starting with 'acc' like 'accept', 'account', 'accurate'  
- If sequence is 'ach': Find words starting with 'ach' like 'achieve', 'ache'
- If sequence is 'acq': Find words starting with 'acq' like 'acquire', 'acquaint'

❌ WRONG: For 'ac' sequence, including words like 'address', 'advance' (these start with 'ad')
❌ WRONG: For 'acc' sequence, including words like 'acquire' (this starts with 'acq')
✅ CORRECT: For 'ac' sequence, words like 'actor', 'across', 'acid'

📚 GRADE-LEVEL VOCABULARY:

**Grades 6-7:** Common everyday words
- Examples: across, actor, action, active, actual
- Focus: Words from children's books, everyday conversation

**Grades 8-9:** Intermediate vocabulary  
- Examples: accurate, accomplish, acknowledge, academic
- Focus: Words from textbooks and young adult literature

**Grades 10-11:** Advanced academic terms
- Examples: accommodate, accountability, accumulate
- Focus: High school literature and academic writing

**Grade 12+:** Sophisticated vocabulary
- Examples: acclimatization, acquiescence, accentuation  
- Focus: College-level and professional vocabulary

🔍 VERIFICATION STEPS:
1. Check each word starts with EXACTLY '{character_sequence}'
2. Verify the word is appropriate for Grade {grade_level}
3. Ensure all words are real, common English words
4. Remove any duplicates

📋 OUTPUT FORMAT:
- If you find 3+ appropriate words: Return JSON array ["word1", "word2", "word3"]
- If fewer than 3 words exist: Return {{"error": "No words found starting with '{character_sequence}' for grade {grade_level}"}}

Find up to 15 words maximum. Focus on educational value and accuracy.""",
        expected_output="A JSON array of common English words that start with the EXACT character sequence, or an error object if insufficient words found",
        agent=agent
    )
