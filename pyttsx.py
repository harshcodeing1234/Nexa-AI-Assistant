import pyttsx3


def speak(text, speed=130):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    female_voice = None
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            female_voice = voice.id
            break

    if female_voice:
        engine.setProperty('voice', female_voice)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', speed)

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    message = "Hello Harsh, i am Zira! How can i help you."
    speak(message, speed=120)