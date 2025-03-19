from scipy.io.wavfile import write
import sounddevice as sd
import numpy as np
import whisper
import pyttsx3
import os


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

    def record_audio(self, filename, duration=5, fs=44100):
        print("Recording...")
        recording = sd.rec(int(duration * fs),  samplerate=fs,
                           channels=2, dtype=np.int16)
        sd.wait()  # Wait until recording is finished
        if not os.path.exists("Inputs"):
            os.makedirs("Inputs")
        write(os.path.join("Inputs", filename), fs,     recording)
        print(f"Recording saved as {filename}")
