import whisper, json, os
import noisereduce as nr
from pydub import AudioSegment
import numpy as np

def transcribe_audio(input_path, output_path):
    os.makedirs("transcripts", exist_ok=True)
    audio = AudioSegment.from_file(input_path)
    samples = np.array(audio.get_array_of_samples())
    reduced_noise = nr.reduce_noise(y=samples, sr=audio.frame_rate)
    clean_audio = audio._spawn(reduced_noise.tobytes())
    clean_audio.export("cleaned.wav", format="wav")

    model = whisper.load_model("base")
    result = model.transcribe("cleaned.wav", word_timestamps=True)

    with open(output_path, "w") as f:
        json.dump(result, f)

if __name__ == "__main__":
    transcribe_audio("data/podcast1.mp3", "transcripts/transcript1.json")
