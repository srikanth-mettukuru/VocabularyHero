# VocabularyHero 📚

A vocabulary learning app powered by multiple AI agents that creates personalized stories and glossaries to help students learn new words.

## What It Does

VocabularyHero uses a **multi-agent AI system** to generate:
- **Words** - Up to 15 vocabulary words starting with your chosen letters
- **Story** - A fun story using all the generated words  
- **Glossary** - Simple definitions and examples for each word

## AI Agent Architecture

The app uses **CrewAI** with three specialized agents working together:

1. **Generator Agent** - Finds vocabulary words matching your criteria
2. **Writer Agent** - Creates engaging stories using all the words
3. **Glossary Agent** - Provides clear definitions and context

Each agent has a specific role and they work sequentially to create a complete learning experience.

## Project Structure

```
VocabularyHero/
├── app.py                    # Streamlit web interface
├── main.py                   # Command-line runner
├── requirements.txt          # Dependencies
├── agents/                   # AI agent definitions
│   ├── generator_agent.py    # Word generation agent
│   ├── writer_agent.py       # Story writing agent
│   └── glossary_agent.py     # Glossary creation agent
├── tasks/                    # Task definitions for each agent
│   ├── generator_task.py
│   ├── writer_task.py
│   └── glossary_task.py
├── crew/                     # Main pipeline orchestration
│   └── words_story_glossary_pipeline.py
└── utils/                    # Shared utilities
    └── llm_provider.py       # LLM configuration
```

## Technology Stack

- **CrewAI** - Multi-agent orchestration
- **OpenAI GPT** - Language model backend
- **Streamlit** - Web interface
- **LangChain** - LLM integration

## Example

Input: "ch" + Grade 6
- **Words**: challenge, character, choose, champion...
- **Story**: A creative story using all the words
- **Glossary**: Definitions for each word with examples

Perfect for teachers, students, and anyone wanting to build vocabulary in a fun way using the power of AI agents!