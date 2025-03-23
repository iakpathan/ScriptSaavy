import os
import pyttsx3
from datetime import datetime


def generate_voiceover(script_content, language='en', output_dir="voiceover"):
    """Generate voiceover from script content using text-to-speech (TTS)."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    audio_path = f"{output_dir}/voiceover_{timestamp}.mp3"

    # ✅ Initialize text-to-speech engine
    engine = pyttsx3.init()

    # ✅ Set language and speech rate (Optional)
    if language == 'en':
        engine.setProperty('voice', 'english')
    engine.setProperty('rate', 150)

    # ✅ Save the audio file
    engine.save_to_file(script_content, audio_path)
    engine.runAndWait()

    return audio_path
