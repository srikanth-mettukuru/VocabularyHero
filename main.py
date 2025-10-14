from crew.words_story_glossary_pipeline import run_words_story_glossary_pipeline

if __name__ == "__main__":
    # Test with 'acc' to reproduce the bug
    results = run_words_story_glossary_pipeline("acc", 6)
    print("\n=== Generator Output ===\n", results["word_list"])
    print("\n=== Writer Output ===\n", results["story_text"])
    print("\n=== Glossary Output ===\n", results["glossary"])
