import os

def filter(text):
    print("Filter module started")
    print("Locating wordlist...")
    base_dir = os.path.dirname(__file__)
    wordlist_path = os.path.join(base_dir, 'wordlists_slur', 'wordlist_en.txt')
    print("Wordlist found")
    print("Making list of banned words..")
    with open(wordlist_path, 'r', encoding='utf-8') as f:
        banned_words = [line.strip().lower() for line in f if line.strip()]
        print("Made list of banned words")
    print("Preparing filter...")
    text = text.replace("’", "'").lower()
    text = text.lower
    print("Filter prepared")
    print("Filtering...")
    if any(word in text for word in banned_words):
        print("Possible violation detected!")
        return False
    else
        print("Text passed succesfully!")
        return True  