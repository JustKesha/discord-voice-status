import speech_recognition as sr

class Default:
    RECORD_DURATION: float = 5.0 # Seconds

def record_audio(
        duration_sec: float = Default.RECORD_DURATION, 
        source: sr.Microphone = sr.Microphone(),
        recognizer: sr.Recognizer = sr.Recognizer()
    ) -> sr.AudioData:
    with source as s:
        return recognizer.record(s, duration=duration_sec)