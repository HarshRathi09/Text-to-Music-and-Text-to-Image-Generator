**DEPLOYMENT INSTRUCTIONS**: 
 
This project has been deployed on Hugging Face Spaces.These are the instructions to access and deploy the app:

Prerequisites:
- You need a Hugging Face account to fork or clone the project.
- Familiarity with the Hugging Face Spaces platform, which uses Streamlit for UI and Gradio for model serving.

Access the Deployed App:
To access the already deployed project, simply visit the following link:
https://huggingface.co/spaces/HarshRathi09/Text-to-Music_and_Text-to-Image_Generator on Hugging Face Spaces
You can interact with the app directly via the web interface:
1. Navigate to the text-to-audio or text-to-image page using buttons on the home page. 
2. Enter a text prompt to generate either audio or images.
3. The app will process the input using the underlying models and display the result.
4. You can download the generated music in .wav format or the generated image in .png format.

Deploying the Project on Hugging Face Spaces:
I followed the below steps to deploy this project on hugging face spaces:

1. Create a New Space:
   - Visit Hugging Face Spaces and click “Create new Space”.
   - Select Streamlit as the framework for this project.

2. Upload the Project:
   - I uploaded the project files directly by dragging and dropping them into the Hugging Face Spaces interface.

4. Set up the Environment:
 - Ensure your requirements.txt includes all necessary libraries, such as: streamlit, transformers, torch, numpy, scipy, and diffusers.  
 - Hugging Face Spaces automatically installs the dependencies listed in your requirements.txt file.
   
5. Configure Models:
   - The app loads models from the Hugging Face model hub. Ensure that the models you want to use are publicly available or that you have the necessary access tokens for private models.
   - Example models used: 
     - Music: facebook/musicgen-small
     - Images: stable-diffusion-v1-4

6. Run the App:
   - Once the setup is complete, the app should run automatically. If not, click the “Run” button at the top of your Hugging Face Space.
   - The app will be hosted on a URL like: https://huggingface.co/spaces/your-username/your-space-name

Updating the App:
I had made some changes to the code, pushed the updates to the Hugging Face repository by uploading the updated files manually.
Hugging Face Spaces will automatically rebuild and redeploy the app.

Monitoring and Logs:
Hugging Face Spaces provides an interactive console where you can monitor logs and debug any issues in real-time.
Check the Logs tab in your Space to troubleshoot any potential problems.

**TECHNICAL DOCUMENTATION**: 

Overview

This project consists of two main components:

1. Audio Generation:
Model: Facebook's MusicGen is used for converting text prompts provied by the user into audio.
Output: Generated music is saved as a .wav file, which can be played in the app or downloaded.

2. Image Generation:
Model: The project uses the CompVis/stable-diffusion-v1-4 (or Stable Diffusion) from the Hugging Face model repository for image generation.
Output: Generated images are displayed in the app and can be downloaded in .png format.

Technical Breakdown

1. Model Selection:

   - MusicGen: Chosen for its ability to generate high-quality music based on text prompts. It provides pre-trained models optimized for various music styles.

   - Stable Diffusion : Used for text-to-image generation due to its robust results.

2. Streamlit Integration:

   - Streamlit was chosen for its ease of use and quick deployment capabilities. Its multipage functionality allowed us to easily switch between the two main features: music and image generation.

3. UI Design:

   - The interface is designed to be minimal yet visually appealing, with custom CSS for a polished look. Users are guided step-by-step to enter their prompts and receive outputs.   


Core Libraries

Streamlit: Used for building the user interface.

Diffusers: For loading and running the text-to-image diffusion models.

Transformers: Used for loading and running the MusicGen model.

Torch: Backend for handling model inference and GPU acceleration.

Scipy: For handling .wav file outputs from the MusicGen model.

File Structure:

├── requirements.txt          # Python dependencies

├── main.py                   # Main entry point for the Streamlit app

├── musicgen.py 

├── pages/                     # subdirectory  consisting of Music_Generator.py (Music generation page) and Image_Generator.py (Image generation page) 
   
    ├── Music_Generator.py     # Music generation page
   
    ├── Image_Generator.py     # Image generation page
├── README.md                 
               
Model Loading

Both the MusicGen and Image Generation models are loaded using the Hugging Face from_pretrained() function. This allows for easy integration with the Hugging Face model repository.

How It Works

Audio Generation:
Users provide a text prompt describing the type of audio they want.
The MusicGen model processes this input and generates a waveform that is converted into a .wav file.
The audio can be played within the app or downloaded.

Image Generation:
Users enter a description of the image they want.
The DiffusionPipeline model is used to convert this text into an image using the selected diffusion model (e.g., Stable Diffusion).
The generated image is displayed and can be downloaded.

**CHALLENGES FACED**:

1. Model Availability:
Some models were unavailable or private, so alternative models had to be identified. One of the other challenges was finding the correct model (Stable Diffusion and MusicGen) for the given task and making sure it was open source.

2. Model Inference Time:
Generating images using large image generation models can be time-consuming. These models took a while to produce output because they were directly accessed from Hugging Face without being downloaded to the local system, as they are quite large. To address this, we added informative messages to the user interface to let users know that the process might take a few seconds.


**APPROACH**:

Problem Statement: The objective was to develop a user-friendly web interface enabling users to generate various outputs from text-based machine learning models. The main challenge was to seamlessly integrate these models into an intuitive  web interface for easy input. My primary model is a text-to-audio generation model. Moreover, I have also developed a text-to-image generation model and integrated both into a multi-page Streamlit application. 


Streamlined UI: The project focuses on keeping the interface simple and intuitive. Users can easily switch between music and image generation using a multi-page layout in Streamlit. Custom CSS was applied to ensure the interface is visually appealing.

Modular Code: The project is broken into separate components for music and image generation, allowing for easy maintenance and future scalability.

Error Handling: Each component includes error handling to manage potential issues with model loading, inference, or file handling. Users are notified if something goes wrong, ensuring a smooth experience.

**ADDITIONAL NOTES**

Future Improvements:

1. Quantization: We plan to implement quantized models to achieve faster inference and reduce memory usage. This improvement will be particularly beneficial for resource-intensive image-generation models.

2. Feedback Mechanism: Implementing user feedback mechanisms to improve generated content.

3. Integration with cloud services: Integrating with cloud services for faster model inference and improved scalability.

**REFRENCES**:

Hugging Face Models

Diffusers Library Documentation

MusicGen

Stable Diffusion
