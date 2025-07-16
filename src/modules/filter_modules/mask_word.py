def mask_word(word):
    if len(word) <= 2:
        return "*" * len(word)
    return word[0] + "*" * (len(word) - 2) + word[-1]