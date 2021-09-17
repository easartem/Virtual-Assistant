import tkinter as tk
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


BG_COLOR = "#ff5757"
BG_PIC_OFF = "Images/vinx_mic_off.png"
BG_PIC_ON = "Images/vinx_mic_on.png"
BTN_START_BG = "Images/activation_btn.png"

class MainWindow():
    '''Use class attributes to define properties that should have the same value for every class instance. 
    Use instance attributes for properties that vary from one instance to another.'''
    #Class Attributes

    # Constructors & Instance attribute
    def __init__(self):
        print("Building GUI...")

        ''' Main Window'''
        self.root = tk.Tk() #self. indicates that they are instance variables
        self.root.geometry('500x500')
        self.root.title("My virtual assistant")

        ''' Background Picture'''
        bg_pic = ImageTk.PhotoImage(Image.open(BG_PIC_OFF))
        self.bg_label = Label(image=bg_pic)
        self.bg_label.place(x=0,y=0)

        ''' Activation Button'''
        btn_start_bg = ImageTk.PhotoImage(Image.open(BTN_START_BG))
        self.btn_start = Button(self.root, image=btn_start_bg, borderwidth=0, highlightthickness=0, bg=BG_COLOR) #command=activateAI)
        self.btn_start.place(x=145,y=400)
        #btn_start.place(x=0,y=0)

        ''' Run window'''
        self.root.mainloop()

    # Methods - Behaviours 
    def activateAI(self):
        return 


if __name__ == '__main__':
 
    app = MainWindow() # create a mainwindow object and store the reference in variable app
