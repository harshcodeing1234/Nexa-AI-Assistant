import pyttsx3


def speak(text, speed=130):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    # Female voice find karne ki koshish
    female_voice = None
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            female_voice = voice.id
            break

    # Voice set karo
    if female_voice:
        engine.setProperty('voice', female_voice)
    else:
        # Agar female na mile to second voice try karo
        engine.setProperty('voice', voices[1].id)

    # Speed slow set karo
    engine.setProperty('rate', speed)

    engine.say(text)
    engine.runAndWait()


# Main block
if __name__ == "__main__":
    message = "Hello Harsh, i am Zira! How can i help you."
    speak(message, speed=120)