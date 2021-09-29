import random
import wikipedia
from bm_utility import *
from bm_caller import *
import os

i = 0

if __name__ == "__main__":
    speak("Hi! I am Bay max. At your service sir.")
    while True:
        if i >= 2:
            i = 0
            des = warn()
            if des:
                sys.exit()
        else:
            speech = command().lower()
            if speech == 'none':
                i += 1
            else:
                i = 0
                if "hi" in speech or "hai" in speech or "hay" in speech or "hello" in speech or "whatsapp" in speech or "how are you" in speech:
                    greeting()

                elif "play music" in speech:
                    dir = "F:\\Soothing Songs"
                    songs = os.listdir(dir)
                    rd = random.choice(songs)
                    os.startfile(os.path.join(dir, rd))
                    # os.system('TASKKILL /F /IM vlc.exe')

                elif "bye" in speech or "goodbye" in speech:
                    speak("Have a great day! Good Bye!")
                    #os.system('pythonw bg.py')
                    sys.exit()

                elif "tell time" in speech or "what is time" in speech or "time now" in speech or "clock" in speech:
                    tell_time()
                elif "sleep" in speech:
                    os.system('python bg.py')
                elif "ip address" in speech:
                    ip = get("https://api.ipify.org").text
                    speak("Sir your IP address is " + ip)

                elif "open google" in speech or "google" in speech or "search google" in speech:
                    print(speech)
                    speech = speech.replace("google", "")
                    speech = speech.replace("open", "")
                    speech = speech.replace("search", "")
                    speech = speech.replace("go", "")
                    speech = speech.replace("to", "")
                    query = sanitize(speech)
                    print(query)
                    if speech == "" or speech == " ":
                        speak('Ok,what would you like to search on Google sir!')
                        query = command()
                    search_google(query)

                elif ("who is" in speech) or ("wikipedia" in speech) or ("what is" in speech) or ("who are" in speech) or ("what are" in speech) or ("search" in speech):
                    speak("Let me dig the Internet for you")
                    speech = speech.lower()
                    speech = speech.replace("wikipedia", "")
                    speech = speech.replace("search", "")
                    speech = speech.replace("baymax", "")
                    speech = speech.replace("jarvis", "")
                    speech = sanitize(speech)
                    try:
                        search_result = wikipedia.summary(speech, sentences=2)
                        speak("Here what I hunt down for you in web forest!")
                        speak(search_result)
                    except Exception:
                        speak("Looks like no great results Found! Would you like me to search on google ?")
                        speechs = command()
                        if ("yes" in speechs) or ("sure" in speechs) or ("yep" in speechs) or ("indeed" in speechs) or (
                                "why not" in speechs) or ("go" in speechs) or ("yeah" in speechs):
                            search_google(speech)

                elif "open youtube" in speech:
                    webbrowser.open("www.youtube.com")

                elif "open mail" in speech:
                    webbrowser.open("https://outlook.office.com/mail/inbox")

                else:
                    speak("Sorry, Unable to recognise your command now, As I am still learning.")
