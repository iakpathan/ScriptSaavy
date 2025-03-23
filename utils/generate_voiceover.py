from gtts import gTTS # type: ignore
import os


def generate_voiceover(script_content, language, output_dir="voiceover"):
    """
    Generate a voiceover audio file from the script content.

    Args:
        script_content (str): The text content of the script.
        language (str): The language code for text-to-speech (e.g., 'en', 'hi').
        output_dir (str): The directory where the audio file will be saved.

    Returns:
        str: Path to the generated audio file.
    """

    # ✅ Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Define the audio file name
    audio_filename = "voiceover.mp3"
    audio_path = os.path.join(output_dir, audio_filename)

    try:
        # ✅ Generate the audio using gTTS
        tts = gTTS(text=script_content, lang=language, slow=False)
        
        # ✅ Save the generated audio to the specified path
        tts.save(audio_path)

        return audio_path

    except Exception as e:
        raise Exception(f"Failed to generate voiceover: {str(e)}")
