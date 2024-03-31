import speech_recognition as sr
import pyttsx3
import speech as sp
import GetInput as gI

def recognizer():
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = r.listen(mic)

                text = r.recognize_google(audio)
                text = text.lower()
                return text
        except sr.UnknownValueError:
            r = sr.Recognizer()
            continue


def starting():
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = r.listen(mic)

                text = r.recognize_google(audio)
                text = text.lower()
                if text == "jarvis" or text == "hey jarvis":
                    sp.speak("What can I do for you today?")
                    return True
        except sr.UnknownValueError:
            r = sr.Recognizer()
            continue
def selection():
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = r.listen(mic)

                text = r.recognize_google(audio)
                text = text.lower()
                print(text)
                if "can you play" in text:
                    sp.speak("playing")
                    return
                elif "that's all" in text or "turn off" in text or text == "that will be all":
                    return "off"
                elif text == "scream":
                    sp.speak("AAAAAAAAAAAOOOOOAAAAAAAAAAAOOAOAOAOAOAAAOOOOOOOOOAOAOAOAOAOAOAOOAOAOAOAAAAAAAAOAOAOAOAAAAAAAAAAAA")
                    return
                else:
                    result = gI.createRespone(text)
                    sp.speak(result)
                    return
        except sr.UnknownValueError:
            r = sr.Recognizer()
            continue