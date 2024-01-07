
from googletrans import Translator

def translate_to_english(word):
    translator = Translator()
    translation = translator.translate(word, src='fa', dest='en')
    return translation.text

persian_word = "سلام"
english_translation = translate_to_english(persian_word)
print(english_translation)