from googletrans import Translator

# Initialize Translator
translator = Translator()

def translate_script(script: str, target_language: str = "es") -> str:
    """Translate script to target language."""
    try:
        translated = translator.translate(script, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error translating script: {str(e)}"

