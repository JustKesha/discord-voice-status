import speech_recognition as sr

class Default:
    ON_STT_ERROR = ""

def sound_to_text(
        audio_data: sr.AudioData,
        method: sr.Recognizer = sr.Recognizer().recognize_google,
        on_error: str = Default.ON_STT_ERROR
    ) -> str:
    try:
        return method(audio_data)
    except:
        return on_error

def stt(audio_data: sr.AudioData, **kwargs) -> str:
    return sound_to_text(audio_data, **kwargs)