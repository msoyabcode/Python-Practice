import speech_recognition as sr

recognizer = sr.Recognizer()

print("Speak now...")

with sr.Microphone() as source:
    audio = recognizer.listen(
        source,
        timeout=None,
        phrase_time_limit=5
    )

print("Audio captured!")

try:
    text = recognizer.recognize_google(
        audio,
        language="en-IN"
    )
    print("You said:", text)
except Exception as e:
    print("Error:", e)
