import streamlit as st
from diffusers import DiffusionPipeline
import torch
from PIL import Image
# Custom CSS to improve the appearance
st.markdown("""
<style>
    .stApp {
        background-image:linear-gradient(to bottom, #000000 ,#000814 ,#001d3d, #003566);
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

# Initialize the Stable Diffusion pipeline
@st.cache_resource
def load_image_model():
    # Ensure that you are using the correct device (GPU if available)
    pipe = DiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
    if torch.cuda.is_available():
        pipe.to("cuda")
    return pipe

pipe = load_image_model()

# Streamlit interface
st.markdown("<h1 class='main-title'>🖼️ AI Image Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Describe the image you want to create, and the AI will generate it for you.</p>", unsafe_allow_html=True)

# Main interaction area
image_description = st.text_input("🖊️ Describe the image you want to create", 
                                  placeholder="E.g., A sunset over a mountain range")

if st.button("🎨 Generate Image"):
    if image_description.strip():
        with st.spinner("🎨 Generating your image..."):
            st.warning("Image generation may take some time. Please be patient.")  # Display warning message
            try:
                # Generate the image
                image = pipe(image_description).images[0]

                # Display the generated image
                st.image(image, caption="Generated Image", use_column_width=True)

                # Provide download button for the generated image
                img_path = "generated_image.png"
                image.save(img_path)

                with open(img_path, "rb") as file:
                    st.download_button(
                        label="📥 Download Image",
                        data=file,
                        file_name="generated_image.png",
                        mime="image/png"
                    )
            except Exception as e:
                st.error(f"😕 Oops! An error occurred: {str(e)}")
    else:
        st.warning("🤔 Please enter a description for your image.")

# Information sections
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌟 How it works")
    st.markdown("""
    1. 📝 Describe the image you want
    2. 🖱️ Click 'Generate Image'
    3. 🎨 View your AI-generated artwork
    4. 📥 Download and share!
    """)

with col2:
    st.markdown("### 🎨 Tips for great results")
    st.markdown("""
    - Be specific about objects and settings
    - Mention style, genre, or mood
    - Describe the colors and lighting
    """)

# Footer
st.markdown("---")
