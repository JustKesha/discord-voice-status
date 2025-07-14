import os
from .filter_modules import clean_text, mask_word

def filter(text, language):
    base_dir = os.path.dirname(__file__)
    wordlist_path = os.path.join(base_dir, 'wordlists_slurs', f'wordlist_{language}.txt')

    with open(wordlist_path, 'r', encoding='utf-8') as f:
        banned_words = [line.strip().lower() for line in f if line.strip()]

    text_clean = clean_text(text)
    lowered = text_clean.lower()

    masked_text = text_clean

    for word in banned_words:
        if word in lowered:
            censored = mask_word(word)
            masked_text = masked_text.replace(word, censored)
            masked_text = masked_text.replace(word.capitalize(), censored)
            masked_text = masked_text.replace(word.upper(), censored)

    return masked_text