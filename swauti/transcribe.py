from transformers import pipeline

class Transcriber:
    def __init__(self):
        self.model_roman = pipeline("automatic-speech-recognition", model="nairaxo/whisper-shikomori-latin")
        self.model_arabic = pipeline("automatic-speech-recognition", model="nairaxo/whisper-shikomori-arabic")

    def transcribe(self, audio, model_choice):
        if model_choice == "roman":
            return self.model_roman(audio)["text"]
        else:
            return self.model_arabic(audio)["text"]