from transformers import pipeline, BitsAndBytesConfig
import re
from PIL import Image

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

model_id = "llava-hf/llava-1.5-7b-hf"
pipe = pipeline("image-to-text", model=model_id, model_kwargs={"quantization_config": quantization_config})

def img2txt(input_text, input_image):
    image = Image.open(input_image)
    prompt_instructions = f'''
    Act as an expert in imagery descriptive analysis, using as much detail as possible from the image, respond to the following prompt: {input_text}
    '''
    prompt = f"USER: <image>\n{prompt_instructions}\nASSISTANT:"
    outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 200})
    
    if outputs and "generated_text" in outputs[0]:
        match = re.search(r'ASSISTANT:\s*(.*)', outputs[0]["generated_text"])
        return match.group(1) if match else "No response found."
    return "No response generated."
