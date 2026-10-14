
import speech_recognition as sr
import webbrowser
import os

recognizer = sr.Recognizer()


def speak(text):
    print("Jarvis:", text)
    os.system(f'say -v Samantha "{text}"')


def processCommand(c):
    print("Command received:", c)

    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=2
                )

            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Hanji Soyab ji")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(
                        source,
                        timeout=2,
                        phrase_time_limit=4
                    )

                command = recognizer.recognize_google(audio)
                processCommand(command)

        except Exception as e:
            print("Error:", e)
