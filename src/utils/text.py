def mask_word(word: str) -> str:
    """Mask a word, preserving first and last characters."""
    if len(word) <= 2:
        return "*" * len(word)
    return word[0] + "*" * (len(word) - 2) + word[-1]