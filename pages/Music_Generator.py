import streamlit as st
from musicgen import init_musicgen, generate_music
import numpy as np
from scipy.io.wavfile import write

# Custom CSS to improve the appearance
st.markdown("""
<style>
    .stApp {
        background-image:linear-gradient(to bottom, #000000 ,#000814 ,#10002b, #240046);
    }
    .main-title {
        font-size: 3rem !important;
        color: #f1faee;
        text-align: center;
        padding: 1rem 0;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #f1faee;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stTextInput > div > div > input {
        font-size: 1.2rem;
    }
    .generate-button {
        font-size: 1.2rem;
        border-radius: 10px;
        padding: 0.5rem 1rem;
    }
    .info-section {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize the MusicGen model and tokenizer
@st.cache_resource
def load_model():
    return init_musicgen('facebook/musicgen-small')

tokenizer, model = load_model()

# Streamlit interface
st.markdown("<h1 class='main-title'>🎵 AI Music Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Describe the type of music you want, and the AI will generate it for you.</p>", unsafe_allow_html=True)

# Main interaction area
text_input = st.text_input("🖊️ Describe the music you want to create", 
                           placeholder="E.g., A happy pop song with guitar and drums")

if st.button("🎼 Generate Music"):
    if text_input.strip():
        with st.spinner("🎧 Generating your music..."):
            try:
                audio_array = generate_music(text_input, tokenizer, model)
                
                # Convert to int16 and save as WAV file
                audio_int16 = (audio_array * 32767).astype(np.int16)
                write("generated_music.wav", 44100, audio_int16)
                
                st.success("🎉 Your music has been generated successfully!")
                
                # Play the generated audio
                st.audio("generated_music.wav")
                
                # Provide download button
                with open("generated_music.wav", "rb") as file:
                    st.download_button(
                        label="📥 Download Music",
                        data=file,
                        file_name="ai_generated_music.wav",
                        mime="audio/wav"
                    )
            except Exception as e:
                st.error(f"😕 Oops! An error occurred: {str(e)}")
    else:
        st.warning("🤔 Please enter a description for your music.")

# Information sections
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌟 How it works")
    st.markdown("""
    1. 📝 Describe the music you want
    2. 🖱️ Click 'Generate Music'
    3. 🎧 Listen to your AI-created tune
    4. 📥 Download and share!
    """)

with col2:
    st.markdown("### 🎨 Tips for great results")
    st.markdown("""
    - Be specific about instruments
    - Mention genre or mood
    - Describe tempo or rhythm
    - Reference famous artists or songs
    """)

# Footer
st.markdown("---")
