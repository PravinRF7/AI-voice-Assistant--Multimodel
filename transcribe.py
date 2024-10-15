import whisper
import torch

model = whisper.load_model("medium", device="cuda" if torch.cuda.is_available() else "cpu")

def transcribe(audio):
    if not audio:
        return ''
    
    audio_data = whisper.load_audio(audio)
    audio_data = whisper.pad_or_trim(audio_data)
    mel = whisper.log_mel_spectrogram(audio_data).to(model.device)
    result = whisper.decode(model, mel)
    return result.text
