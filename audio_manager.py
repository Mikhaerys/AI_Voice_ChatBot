import whisper
import pyttsx3


class AudioManager:
    def __init__(self):
        self.model = whisper.load_model("tiny")
        self.engine = pyttsx3.init()

    def audio2text(self, audio_file):
        result = self.model.transcribe(audio_file)
        return result["text"]

    def text2audio(self, text):
        self.engine.say(text)
        self.engine.save_to_file(text, "output.mp3")
        self.engine.runAndWait()
