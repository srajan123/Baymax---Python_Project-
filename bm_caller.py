import pyttsx3
import speech_recognition as sr
from datetime import datetime as dt
import sys
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_id_Brian22 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Brian22"
engine.setProperty('voice', voice_id_Brian22)


def speak(audio):
    engine.say(audio)
    print("Baymax : " + audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 2
        audio = r.listen(source, timeout=None, phrase_time_limit=3.5)
    try:
        print("Recognising.....")
        print("You : " + r.recognize_google(audio, language='en-in'))
        return (r.recognize_google(audio)).lower()
    except sr.UnknownValueError:
        speak("Unable to catch!")
        return 'None'


def greeting():
    hour = dt.now().hour
    day = dt.today().strftime("%A")
    year = dt.today().year
    time = dt.now().time().strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        wish = "Good Morning sir! Looks like a fresh start today! Everyday is a new beginning. Take a deep breath, smile and start again."
    elif hour > 12 and hour <= 18:
        wish = "Good Evening! How was you day sir!"
    else:
        wish = "Good Night Sir! I know you are exhausted but it’s a long night. So, you’ll have plenty of time to sleep and to dream. Good night my friend. Have a sound sleep!"
    speak(wish + " It's " + day + " today." + " And current time is " + time)

def tell_time():
    time = dt.now().time().strftime("%I:%M %p")
    speak("Current time is " + time)


def warn():
    speak("Seems liken no more command for me. Shall I got to sleep now")
    speechs = command()
    if ("yes" in speechs) or ("sure" in speechs) or ("yep" in speechs) or ("indeed" in speechs) or ("why not" in speechs) or ("go" in speechs) or ("yeah" in speechs):
        speak("Okay, In case you need anything, just say wake-up and I am ready at your service sir")
        os.system('pythonw bg.py')
        return True
    else:
        speak("seems you don't allow me to sleep. So how may I help you sir now?")
