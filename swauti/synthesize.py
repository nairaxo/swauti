from transformers import pipeline
import scipy
import torchaudio
from speechbrain.pretrained import SepformerSeparation as separator
from shialifube import transliterate
import tempfile

class Synthesizer:
    def __init__(self):
        self.synthesiser = pipeline("text-to-speech", model="nairaxo/mms-tts-zdj", device=0)
        self.model_enh = separator.from_hparams(source="speechbrain/sepformer-wham16k-enhancement", savedir='pretrained_models/sepformer-wham16k-enhancement')

    def generate_and_enhance_audio(self, text, script_choice):
        if script_choice == "arabic":
            text = transliterate(text)

        speech = self.synthesiser(text)
        sampling_rate = speech["sampling_rate"]

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as original_file:
            original_output = original_file.name
            scipy.io.wavfile.write(original_output, rate=sampling_rate, data=speech["audio"][0])

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as enhanced_file:
            enhanced_output = enhanced_file.name
            est_sources = self.model_enh.separate_file(path=original_output)
            torchaudio.save(enhanced_output, est_sources[:, :, 0].detach().cpu(), sampling_rate)

        return original_output, enhanced_output