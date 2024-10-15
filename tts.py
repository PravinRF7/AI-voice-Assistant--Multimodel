from gtts import gTTS

def text_to_speech(text, file_path):
    audio_obj = gTTS(text=text, lang='en', slow=False)
    audio_obj.save(file_path)
    return file_path
