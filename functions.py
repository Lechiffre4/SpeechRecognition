
from numpy import add
import speech_recognition as sr
import pyttsx3
import webbrowser
import Websites_url
import io



def Recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="fr-FR")
            text = text.lower()
            
        except:
            return "Sorry, I didn't get that."
    
        for site in Websites_url.websites:
            if site in text:
                webbrowser.open(Websites_url.websites[site], new=1)


def addShortCut(name, link):
    temp_dict = Websites_url.websites
    temp_dict.update({name.lower() : link})
    new_dict = str("websites = " + str(temp_dict))
    with io.open("Websites_url.py", "w", encoding="utf-8") as f:
        f.write(new_dict)

