from transformers import AutoTokenizer, AutoModelForTextToWaveform
import torch

def init_musicgen(model_size='facebook/musicgen-small'):
    """
    Initialize the MusicGen model and tokenizer.
    """
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_size)
        model = AutoModelForTextToWaveform.from_pretrained(model_size)
        return tokenizer, model
    except Exception as e:
        print(f"Error loading model or tokenizer: {str(e)}")
        raise e

def generate_music(text_prompt, tokenizer, model):
    """
    Generate music based on the input text prompt using the pre-initialized model.
    """
    print(f"Generating music for prompt: {text_prompt}")
    
    # Tokenize the input text
    inputs = tokenizer(text_prompt, return_tensors='pt')
    
    # Check if inputs are valid
    if 'input_ids' not in inputs or inputs['input_ids'] is None or inputs['input_ids'].size(0) == 0:
        raise ValueError("Tokenized inputs are empty or invalid. Ensure your input prompt is valid.")

    # Generate the music waveform
    with torch.no_grad():
        generated_waveform = model.generate(**inputs)

    return generated_waveform.cpu().numpy().squeeze()