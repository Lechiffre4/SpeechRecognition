import speech_recognition as sr
import pyttsx3
import webbrowser
import Websites_url


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("You said : {}".format(text))
        text = text.lower()
        
    except:
        print("Sorry could not recognize what you said")

    for site in Websites_url.websites:
        if site in text:
            webbrowser.open(Websites_url.websites[site], new=1)
