from pip import main
import speech_recognition as sr
import pyttsx3
import webbrowser
import Websites_url
import functions
from tkinter import *
from tkinter import ttk


main_interface = Tk()
frm = ttk.Frame(main_interface, padding=10)
frm.grid()
ttk.Label(frm, text="Welcome to SpeechRecognition!").grid(column=10, row=10)
ttk.Button(frm, text="Start Recognition !", command=functions.Recognition).grid(column=10, row=20)
ttk.Button(frm, text="Quit !", command=main_interface.destroy).grid(column=30, row=100)

ttk.Label(frm, text="Keyword").grid(row=30, column=9)
ttk.Label(frm, text="Link").grid(row=30, column=11)

keyword = ttk.Entry(frm)
link = ttk.Entry(frm)
ttk.Button(frm, text="Add Vocal ShortCut!", command=functions.Recognition).grid(column=10, row=40)
main_interface.mainloop()