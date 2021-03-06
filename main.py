from turtle import bgcolor
from pip import main
import speech_recognition as sr
import pyttsx3
import webbrowser
import Websites_url
import functions
from tkinter import *
from tkinter import ttk


main_interface = Tk()

#Customize the main window
main_interface.title("SpeechRecognition")
style = ttk.Style(main_interface)
style.configure('TLabel', background='#8963BA', foreground='white')
style.configure('TFrame', background='#611C35')

main_interface.geometry("450x150")
main_interface.resizable(False, False)

main_interface.iconbitmap("./image/microphone.ico")


frm = ttk.Frame(main_interface, padding=10)
frm.grid()
#Quit button+ Start Button + Title
ttk.Label(frm, text="Welcome to SpeechRecognition!").grid(column=10, row=10)
ttk.Button(frm, text="Start Recognition !", command=functions.Recognition).grid(column=10, row=20)
ttk.Button(frm, text="Quit !", command=main_interface.destroy).grid(column=10, row=50)



#inputs 
ttk.Label(frm, text="Keyword").grid(row=30, column=9)
ttk.Label(frm, text="Link").grid(row=30, column=11)
keyword = ttk.Entry(frm)
link = ttk.Entry(frm)
keyword.grid(row=31, column=9)
link.grid(row=31, column=11)
ttk.Button(frm, text="Add Vocal ShortCut!", command=lambda : functions.addShortCut(keyword.get(),link.get()) ).grid(column=10, row=40)



main_interface.mainloop()