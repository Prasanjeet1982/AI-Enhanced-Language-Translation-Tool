from translate import Translator

def translate_text(source_text, target_language):
    try:
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(source_text)
        return translated_text
    except Exception as e:
        return f"An error occurred: {e}"
