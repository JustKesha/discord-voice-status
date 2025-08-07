from typing import Any
import speech_recognition as sr

class Default:
    LANGUAGE: str = "en"
    ON_ERROR: Any = ""

def sound_to_text(
        audio_data: sr.AudioData,
        language: str = Default.LANGUAGE,
        method: sr.Recognizer = sr.Recognizer().recognize_google,
        on_error: Any = Default.ON_ERROR
    ) -> str | Any:
    try:
        return method(audio_data, language = language)
    except:
        return on_error

# Just sugar
def stt(audio_data: sr.AudioData, **kwargs) -> str:
    return sound_to_text(audio_data, **kwargs)