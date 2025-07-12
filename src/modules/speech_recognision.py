import speech_recognition as sr

def sound_to_text(
        audio_data: sr.AudioData,
        method: sr.Recognizer = sr.Recognizer().recognize_google,
        on_error: str = ""
    ) -> str:
    try:
        return method(audio_data)
    except:
        return on_error

def stt(audio_data: sr.AudioData, **kwargs) -> str:
    return sound_to_text(audio_data, **kwargs)