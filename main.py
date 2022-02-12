import speech_recognition as sr
import pyttsx3
import webbrowser


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("You said : {}".format(text))
        text.lower()
        
    except:
        print("Sorry could not recognize what you said")

    if "youtube" in text:
        print("Je lance youtube")
        webbrowser.open('https://www.youtube.com', new=1)
    elif "twitch" in text:
        print("Je lance youtube")
        webbrowser.open('https://www.twitch.tv', new=1)
