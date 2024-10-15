from img2txt import img2txt
from transcribe import transcribe
from tts import text_to_speech
from logger import writehistory
import gradio as gr

def process_inputs(audio_path, image_path):
    speech_to_text_output = transcribe(audio_path)
    chatgpt_output = img2txt(speech_to_text_output, image_path)
    processed_audio_path = text_to_speech(chatgpt_output, "Temp3.mp3")
    return speech_to_text_output, chatgpt_output, processed_audio_path

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="ChatGPT Output"),
        gr.Audio("Temp.mp3")
    ],
    title="Learn OpenAI Whisper: Image processing with Whisper and Llava",
    description="Upload an image and interact via voice input and audio response."
)

iface.launch(debug=True)
