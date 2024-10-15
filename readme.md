


# Multimodal RAG with Whisper, Llava, and Gradio

This project is a multimodal Retrieval-Augmented Generation (RAG) application that utilizes OpenAI's Whisper for speech recognition, Llava for image-to-text processing, and Gradio for a user-friendly web interface. Users can interact with the app by uploading an image and providing a voice input. The application will generate a detailed description of the image based on the voice input and then convert the response to audio output.

## Features

- **Speech Recognition**: Converts audio input to text using OpenAI's Whisper model.
- **Image Analysis**: Processes images and generates descriptive text with Llava's image-to-text model.
- **Text-to-Speech**: Converts generated text back into audio using Google Text-to-Speech (gTTS).
- **User Interface**: Easy-to-use web interface powered by Gradio.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project_folder
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## Usage

To run the application, navigate to the `project_folder` directory and run:

```bash
python app.py
```

This will launch a Gradio interface where you can:
1. Upload an image.
2. Provide a voice prompt or question about the image.
3. Receive a text description and audio response.

### Example
- Upload an image file and ask, “What is the color of the microphone in the image?”
- The application will process the image, generate a response, and play the audio answer.

## Modules

- **`app.py`**: The main application script that imports and uses functions from the other modules. It also defines the Gradio interface.
- **`img2txt.py`**: Contains the `img2txt()` function that uses Llava's image-to-text model to analyze the image and generate descriptive text.
- **`transcribe.py`**: Contains the `transcribe()` function that transcribes audio input to text using OpenAI's Whisper.
- **`tts.py`**: Contains the `text_to_speech()` function that converts text to audio output using gTTS.
- **`logger.py`**: Contains the `writehistory()` function for logging input history for analysis or debugging.

## Dependencies

The application uses the following Python libraries:
- `transformers==4.37.2`
- `bitsandbytes==0.41.3`
- `accelerate==0.25.0`
- `whisper`
- `gradio`
- `gTTS`
- `nltk`

All dependencies are listed in `requirements.txt` for easy installation. Install them with:
```bash
pip install -r requirements.txt
```

## Notes

- Ensure you have an active internet connection for downloading models and accessing the Gradio interface.
- The application requires a CUDA-enabled GPU for optimal performance with Whisper and Llava models.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) - for speech recognition
- [Llava](https://huggingface.co/llava-hf/llava-1.5-7b-hf) - for image-to-text processing
- [Gradio](https://gradio.app/) - for the web interface
- [gTTS](https://pypi.org/project/gTTS/) - for text-to-speech conversion

---

**Happy coding!**
```

Replace `<repository-url>` with your repository link if this is going to be hosted on a platform like GitHub.