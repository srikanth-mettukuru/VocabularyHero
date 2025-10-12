import streamlit as st
from crew.words_story_glossary_pipeline import run_words_story_glossary_pipeline
import json

# Configure Streamlit page
st.set_page_config(
    page_title="Vocabulary Hero",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        font-size: 3rem;
        font-weight: bold;
        margin-top: 1rem;
        margin-bottom: 6rem;
    }
    .section-header {
        color: #A23B72;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #A23B72;
        padding-bottom: 0.5rem;
    }
    .word-list {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E86AB;
    }
    .story-content {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #F18F01;
        line-height: 1.6;
    }
    .glossary-content {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #C73E1D;
    }
    .sidebar-info {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">📚 Vocabulary Hero</h1>', unsafe_allow_html=True)

# Sidebar for user inputs
st.sidebar.markdown("## 🎯 Settings")
st.sidebar.markdown('<div class="sidebar-info">Select your preferences to generate a personalized vocabulary learning experience!</div>', unsafe_allow_html=True)

# Character sequence input
character_sequence = st.sidebar.text_input(
    "📝 Enter Character Sequence:",
    value="ac",  # Default value
    max_chars=3,
    help="Enter 1-3 characters that words should start with (e.g., 'a', 'ac', 'ser')"
).lower().strip()

# Grade level selection with clear grade levels and skill descriptors
grade_options = {
    "📚 Grade 6 (Basic)": 6,
    "📖 Grade 8 (Intermediate)": 8, 
    "🎯 Grade 10 (Advanced)": 10,
    "🏆 Grade 12 (Expert)": 12
}

selected_grade = st.sidebar.selectbox(
    "🎓 Select Grade Level:",
    options=list(grade_options.keys()),
    index=0,  # Default to Grade 6
    help="Choose the grade level appropriate for the student's vocabulary learning goals"
)

grade_level = grade_options[selected_grade]

# Generate button
generate_button = st.sidebar.button(
    "🚀 Generate Vocabulary",
    type="primary",
    use_container_width=True
)

# Info section in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ How it works:")
st.sidebar.markdown("""
1. **Word Generator**: Creates up to 15 vocabulary words
2. **Story Writer**: Crafts an engaging story using all words
3. **Glossary Creator**: Explains each word with context
""")

# Main content area
if generate_button:
    # Input validation
    if not character_sequence or len(character_sequence) == 0:
        st.error("❌ Please enter at least 1 character")
        st.stop()
    
    if not character_sequence.isalpha():
        st.error("❌ Please enter only alphabetic characters (a-z)")
        st.stop()
    
    st.markdown("---")
    
    # Show loading message and run pipeline
    grade_display = selected_grade.split(' ', 1)[1] if ' ' in selected_grade else selected_grade
    with st.spinner(f"🎨 Creating vocabulary for sequence '{character_sequence}' at {grade_display} level..."):
        try:
            # Run the CrewAI pipeline
            results = run_words_story_glossary_pipeline(character_sequence, grade_level)
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("Please check your OpenAI API key and try again.")
            st.stop()
    
    # Parse and validate results (outside the spinner)
    if results["word_list"]:
        try:
            if isinstance(results["word_list"], str):
                word_list = json.loads(results["word_list"])
            else:
                word_list = results["word_list"]
            
            # Check if it's an error response
            if isinstance(word_list, dict) and "error" in word_list:
                st.error(f"❌ {word_list['error']}")
                st.info("💡 **Suggestions:**\n- Try a different character sequence (e.g., 'a', 'an', 'ch')\n- Try a different grade level\n- Use more common letter combinations")
                st.stop()  # Don't show story or glossary
            
            # Check if it's an empty list
            if isinstance(word_list, list) and len(word_list) == 0:
                st.error(f"❌ No words found starting with '{character_sequence}' for grade {grade_level}")
                st.info("💡 **Suggestions:**\n- Try a different character sequence (e.g., 'a', 'an', 'ch')\n- Try a different grade level\n- Use more common letter combinations")
                st.stop()  # Don't show story or glossary
                
        except json.JSONDecodeError:
            st.error("❌ Error parsing word list")
            st.info("💡 Try again with a different character sequence")
            st.stop()
    else:
        st.error(f"❌ No words found starting with '{character_sequence}' for grade {grade_level}")
        st.info("💡 **Suggestions:**\n- Try a different character sequence (e.g., 'a', 'an', 'ch')\n- Try a different grade level\n- Use more common letter combinations")
        st.stop()
    
    # Display results in columns for better layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Word List Section
        st.markdown('<h2 class="section-header">📝 Words </h2>', unsafe_allow_html=True)
        
        # Display words in a nice format
        st.markdown('<div class="word-list">', unsafe_allow_html=True)
        
        # Extract grade level and skill descriptor from selected option
        # Format: "📚 Grade 6 (Basic)" -> "Grade 6 (Basic)"
        grade_display = selected_grade.split(' ', 1)[1] if ' ' in selected_grade else selected_grade
        st.markdown(f"**Starting with '{character_sequence}' - {grade_display}**")
        
        # Create a numbered list of words
        word_display = ""
        for i, word in enumerate(word_list, 1):
            word_display += f"{i}. **{word.capitalize()}**\n"
        
        st.markdown(word_display)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Show word count
        st.info(f"✅ Generated {len(word_list)} word(s)")
    
    with col2:
        # Story Section
        st.markdown('<h2 class="section-header">📖 Story</h2>', unsafe_allow_html=True)
        
        if results["story_text"]:
            if results["story_text"].strip().startswith("No story created"):
                st.info("📝 No story was created because no vocabulary words were found.")
            else:
                # Italicize the vocabulary words in the story
                story_with_italics = results["story_text"]
                
                if results["word_list"]:
                    try:
                        # Get the word list
                        if isinstance(results["word_list"], str):
                            word_list_for_story = json.loads(results["word_list"])
                        else:
                            word_list_for_story = results["word_list"]
                        
                        # Only italicize if we have a proper word list (not error dict)
                        if isinstance(word_list_for_story, list) and len(word_list_for_story) > 0:
                            # Sort words by length (longest first) to avoid partial replacements
                            sorted_words = sorted(word_list_for_story, key=len, reverse=True)
                            
                            # Italicize each vocabulary word in the story
                            import re
                            for word in sorted_words:
                                # Create a regex pattern that matches the word with word boundaries
                                # and handles different capitalizations
                                pattern = r'\b' + re.escape(word.lower()) + r'\b'
                                
                                # Replace with italicized version, preserving original capitalization
                                def replace_func(match):
                                    original_word = match.group(0)
                                    return f"*{original_word}*"
                                
                                story_with_italics = re.sub(pattern, replace_func, story_with_italics, flags=re.IGNORECASE)
                                
                    except (json.JSONDecodeError, ImportError):
                        # If there's any error, just show the original story
                        story_with_italics = results["story_text"]
                
                st.markdown('<div class="story-content">', unsafe_allow_html=True)
                st.markdown(story_with_italics)
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("No story generated")
    
    # Full-width glossary section
    st.markdown('<h2 class="section-header">📚 Glossary</h2>', unsafe_allow_html=True)
    
    if results["glossary"]:
        glossary_content = results["glossary"]
        if glossary_content.strip().startswith("No glossary created"):
            st.info("� No glossary was created because no vocabulary words were found.")
        else:
            # Remove the duplicate "# Vocabulary Glossary" header from the agent output
            if glossary_content.startswith("# Vocabulary Glossary"):
                first_newline = glossary_content.find('\n')
                if first_newline != -1:
                    glossary_content = glossary_content[first_newline + 1:].lstrip()
            
            st.markdown('<div class="glossary-content">', unsafe_allow_html=True)
            st.markdown(glossary_content)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("No glossary generated")


else:
    # Welcome message when no generation has been run
    st.markdown("---")
    st.markdown("### 👋 Welcome to Vocabulary Hero!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📝 Word Generation
        Our AI generates up to 15 educational words starting with your chosen character sequence (1-3 letters), perfectly suited for your selected grade level.
        """)
    
    with col2:
        st.markdown("""
        #### 📖 Story Creation  
        Watch as our creative writer weaves all words into an engaging, age-appropriate story that adapts its length based on the number of words found.
        """)
    
    with col3:
        st.markdown("""
        #### 📚 Glossary Building
        Get clear, simple definitions and see how each word is used in context to enhance understanding and retention.
        """)
    
    st.markdown("---")
    st.info("👈 Use the sidebar to select your preferences and click 'Generate Vocabulary' to begin!")
    
    # Add character sequence examples
    st.markdown("### 💡 Character Sequence Examples:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Single Letters:**
        - `a` → apple, amazing, adventure
        - `b` → banana, beautiful, brave
        - `c` → cat, creative, celebrate
        """)
    
    with col2:
        st.markdown("""
        **Two Letters:**
        - `ch` → challenge, character, choose
        - `th` → think, through, theory
        - `st` → story, student, strong
        """)
    
    with col3:
        st.markdown("""
        **Three Letters:**
        - `str` → strong, structure, strategy
        - `pre` → present, prepare, previous
        - `con` → consider, connect, continue
        """)

# Footer
st.markdown("---")