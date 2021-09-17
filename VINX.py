import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3
import datetime

print("Opening script...")


#-----------------------------Script----------------------------------------------

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Bonjour le monde!')
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

#-----------------------------GUI-------------------------------------------------

''' Main Window'''
root = Tk()
root.title("My virtual assistant")
#root.geometry("500x100") #Width x Height

''' Background Picture'''
bg_pic = ImageTk.PhotoImage(Image.open("vinx_mic_off.png"))
bg_label = Label(image=bg_pic)
bg_label.pack()

''' SCRIPT'''
def activateAI():
    return 

''' Button Start'''
btn_start = Button(root, text="Activer", command=activateAI)
btn_start.place(x=0,y=0)


root.mainloop()