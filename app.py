import streamlit as st

# Set page configuration (only once in main.py)
st.set_page_config(page_title="AI Generator App", page_icon="🎵", layout="wide")

# Custom CSS to improve the appearance
st.markdown("""
    <style>
    .stApp {
        background-image:linear-gradient(to bottom, #000000 , #0a0908, #250902, #641220);
        font-family: 'Helvetica', sans-serif;
    }
    .main-title {
        font-size: 3.5rem !important;
        color: #f1faee;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #f1faee;
        text-align: center;
        margin-bottom: 3rem;
    }
    .stButton button {
        background-color: #780116;
        color: white;
        padding: 15px 32px;
        font-size: 1.2rem;
        margin: 10px;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #46494c;
    }
    .section-title {
        color: #fff;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    .section-description {
        color: #ddd;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main page content
st.markdown("<h1 class='main-title'>🎨 AI Music and Image Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Welcome to the AI Generator app! Use the navigation menu to switch between generating music or images based on text prompts.</p>", unsafe_allow_html=True)

# Brief description of each section
st.markdown("### Available Sections:")
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='section-title'>🎵 Music Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-description'>Transform your ideas into music using AI.</div>", unsafe_allow_html=True)
   
    music = st.button("Generate Music")
    if music:
        st.switch_page("pages/Music_Generator.py")

with col2:
    st.markdown("<div class='section-title'>🖼️ Image Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-description'>Generate stunning images from your text descriptions.</div>", unsafe_allow_html=True)
    img = st.button("Generate Images")
    if img:
        st.switch_page("pages/Image_Generator.py")
