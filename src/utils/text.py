import unicodedata
from typing import Dict

def clean_text(text: str) -> str:
    """Normalize and clean special characters in text."""
    text = unicodedata.normalize('NFKC', text)
    replacements: Dict[str, str] = {
        "‘": "'",
        "’": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "--": "-",
        "…": "...",
        "\u00A0": " ",
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    return text

def mask_word(word: str) -> str:
    """Mask a word, preserving first and last characters."""
    if len(word) <= 2:
        return "*" * len(word)
    return word[0] + "*" * (len(word) - 2) + word[-1]