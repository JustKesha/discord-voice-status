from typing import Literal

CensorMode = Literal["full", "first_last", "first_visible"]

def censor_word(word: str, mode: str = "first_last") -> str:
    match mode:
        case "full":
            return "*" * len(word)
        case "first_last_visible":
            if len(word) <= 2:
                return "*" * len(word)
            return word[0] + "*" * (len(word) - 2) + word[-1]
        case "first_visible":
            if not word:
                return ""
            return word[0] + "*" * (len(word) - 1)
        case _:
            raise ValueError(f"Unknown mode: {mode}. Valid modes: {', '.join(CensorMode.__args__)}")