def clean_text(text):
    text = unicodedata.normalize('NFKC', text)
    replacements = {
        "‘": "'",
        "’": "'",
        """: '"',
        """: '"',
        "–": "-",
        "--": "-",
        "…": "...",
        "\u00A0": " ",  # non-breaking space
        "'": "'"
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    return text