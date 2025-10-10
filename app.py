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

# Alphabet selection
alphabet = st.sidebar.selectbox(
    "📝 Choose Starting Letter:",
    options=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    index=0,  # Default to 'A'
    help="Select the letter that all vocabulary words should start with"
)

# Grade level selection
grade_level = st.sidebar.selectbox(
    "🎓 Select Grade Level:",
    options=list(range(6, 13)),  # 6 to 12
    index=0,  # Default to grade 6
    help="Choose the appropriate grade level for vocabulary difficulty"
)

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
1. **Word Generator**: Creates some vocabulary words
2. **Story Writer**: Crafts an engaging story using all words
3. **Glossary Creator**: Explains each word with context
""")

# Main content area
if generate_button:
    st.markdown("---")
    
    # Show loading message
    with st.spinner(f"🎨 Creating vocabulary for letter '{alphabet}' at grade {grade_level} level..."):
        try:
            # Run the CrewAI pipeline
            results = run_words_story_glossary_pipeline(alphabet, grade_level)
            
            # Display results in columns for better layout
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Word List Section
                st.markdown('<h2 class="section-header">📝 Words </h2>', unsafe_allow_html=True)
                
                if results["word_list"]:
                    # Parse the word list if it's a JSON string
                    try:
                        if isinstance(results["word_list"], str):
                            word_list = json.loads(results["word_list"])
                        else:
                            word_list = results["word_list"]
                        
                        # Display words in a nice format
                        st.markdown('<div class="word-list">', unsafe_allow_html=True)
                        st.markdown(f"**Starting with '{alphabet}' - Grade {grade_level}**")
                        
                        # Create a numbered list of words
                        word_display = ""
                        for i, word in enumerate(word_list, 1):
                            word_display += f"{i}. **{word.capitalize()}**\n"
                        
                        st.markdown(word_display)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Show word count
                        st.info(f"✅ Generated {len(word_list)} words")
                        
                    except json.JSONDecodeError:
                        st.error("Error parsing word list")
                        st.text(results["word_list"])
                else:
                    st.warning("No words generated")
            
            with col2:
                # Story Section
                st.markdown('<h2 class="section-header">📖 Story</h2>', unsafe_allow_html=True)
                
                if results["story_text"]:
                    # Italicize the vocabulary words in the story
                    story_with_italics = results["story_text"]
                    
                    if results["word_list"]:
                        try:
                            # Get the word list
                            if isinstance(results["word_list"], str):
                                word_list = json.loads(results["word_list"])
                            else:
                                word_list = results["word_list"]
                            
                            # Sort words by length (longest first) to avoid partial replacements
                            sorted_words = sorted(word_list, key=len, reverse=True)
                            
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
                # Remove the duplicate "# Vocabulary Glossary" header from the agent output
                glossary_content = results["glossary"]
                if glossary_content.startswith("# Vocabulary Glossary"):
                    # Find the first line break and remove everything before it
                    first_newline = glossary_content.find('\n')
                    if first_newline != -1:
                        glossary_content = glossary_content[first_newline + 1:].lstrip()
                
                st.markdown('<div class="glossary-content">', unsafe_allow_html=True)
                st.markdown(glossary_content)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("No glossary generated")                
                        
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("Please check your OpenAI API key and try again.")

else:
    # Welcome message when no generation has been run
    st.markdown("---")
    st.markdown("### 👋 Welcome to Vocabulary Hero!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📝 Word Generation
        Our AI-powered app generates 10-15 educational  words starting with your chosen letter, perfectly suited for your selected grade level.
        """)
    
    with col2:
        st.markdown("""
        #### 📖 Story Creation  
        Watch as our creative writer weaves all words into an engaging, age-appropriate story that brings learning to life.
        """)
    
    with col3:
        st.markdown("""
        #### 📚 Glossary Building
        Get clear, simple definitions and see how each word is used in context to enhance understanding and retention.
        """)
    
    st.markdown("---")
    st.info("👈 Use the sidebar to select your preferences and click 'Generate Vocabulary' to begin!")

# Footer
st.markdown("---")