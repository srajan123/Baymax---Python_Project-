from bm_caller import *
import time
import os


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
    try:
        print("Recognising...")
        print("You : " + r.recognize_google(audio))
        return (r.recognize_google(audio)).lower()
    except sr.UnknownValueError:
        return 'None'


while True:
    speech = command()
    if "wake" in speech or "up" in speech or "wakeup" in speech:
        break
os.system('python baymax.py')
