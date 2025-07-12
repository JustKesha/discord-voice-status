import speech_recognition as sr

def record_audio(
        duration_sec: float = 5.0, 
        source: sr.Microphone = sr.Microphone(),
        recognizer: sr.Recognizer = sr.Recognizer()
    ) -> sr.AudioData:
    with source as s:
        return recognizer.record(s, duration=duration_sec)