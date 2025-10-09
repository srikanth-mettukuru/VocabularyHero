from crew.words_story_glossary_pipeline import run_words_story_glossary_pipeline

if __name__ == "__main__":
    results = run_words_story_glossary_pipeline("C", 6)
    print("\n=== Generator Output ===\n", results["word_list"])
    print("\n=== Writer Output ===\n", results["story_text"])
    print("\n=== Glossary Output ===\n", results["glossary"])
