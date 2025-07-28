from pathlib import Path
from typing import Callable, Union
from utils import censor_word, CensorMode

class Default:
    LANGUAGE: str = "en"
    CENSOR_MODE: CensorMode = "first_last_visible"
    CENSOR_METHOD: Callable[[str], str] = lambda word: censor_word(word, Default.CENSOR_MODE)
    FILTER_LISTS_PATH: Path = Path(__file__).parent / "filter_lists"
    FILTER_LIST_PREFIX: str = "wordlist_"
    FILTER_LIST_FORMAT: str = ".txt"
    FILTER_LIST_ENCODING: str = "utf-8"

def get_filter_list_path(
        language: str = Default.LANGUAGE,
        directory: Path = Default.FILTER_LISTS_PATH,
        prefix: str = Default.FILTER_LIST_PREFIX,
        format: str = Default.FILTER_LIST_FORMAT
        ) -> Path:
    return directory / f"{prefix}{language}{format}"

def clean_filter_line(line: str) -> Union[str, None]:
    clean = line.strip().lower()
    return clean or None

def load_filter_words(
        language: str = Default.LANGUAGE,
        encoding: str = Default.FILTER_LIST_ENCODING,
        **kwargs
        ) -> set[str]:
    text = get_filter_list_path(language, **kwargs).read_text(encoding)
    words = {
        word
        for line in text.split('\n')
        if (word := clean_filter_line(line))
        }
    return words

def apply_filter(
        text: str,
        filter_words: set[str],
        censor_method: Callable[[str], str] = Default.CENSOR_METHOD
        ) -> str:
    for word in filter_words:
        if word in text:
            text = text.replace(word, censor_method(word))
    return text

def filter(
        text: str,
        language: str = Default.LANGUAGE,
        censor_mode: CensorMode = Default.CENSOR_MODE,
        **kwargs
        ) -> str:
    censor_method = lambda word: censor_word(word, censor_mode)
    words = load_filter_words(language, **kwargs)
    text = apply_filter(text, words, censor_method)
    return text
