import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import VINX_Engine as engine

''' Global variables for design'''

# Color of the background
BG_COLOR = "#ff5757"
# Backgroung picture when the vocal assistant is offline
BG_PIC_OFF = "Images/vinx_mic_off.png"
# Backgroung picture when the vocal assistant is online and listenning
BG_PIC_ON = "Images/vinx_mic_on.png"
# Picture of the vocal assistant's activation button 
BTN_START_BG = "Images/activation_btn.png"
# Picture of the vocal assistant's activation button 
BTN_WAIT_BG = "Images/activated_btn.png"


''' Definition of the app main window'''

class MainWindow():

    # Class Attributes to define properties that should have the same value for every class instance.

    # Constructors & Instance attribute for properties that vary from one instance to another.
    def __init__(self):
        print("Building GUI...")

        ''' Main Window'''
        self.root = tk.Tk() #self. indicates that they are instance variables
        self.root.geometry('500x500')
        self.root.title("My virtual assistant")

        ''' Background Picture'''
        self.bg_pic = ImageTk.PhotoImage(Image.open(BG_PIC_OFF))
        self.bg_label = Label(image=self.bg_pic)
        self.bg_label.place(x=0,y=0)

        ''' Activation Button'''
        self.btn_start_bg = ImageTk.PhotoImage(Image.open(BTN_START_BG))
        self.btn_start = Button(self.root, image=self.btn_start_bg, borderwidth=0, highlightthickness=0, bg=BG_COLOR, command=self.activateAI) #command=activateAI)
        self.btn_start.place(x=145,y=400)
        #btn_start.place(x=0,y=0)

        ''' Run window'''
        #self.root.mainloop()

    # Methods - Behaviours 
    def activateAI(self):
        # Background picture change to show a mic on 
        self.bg_pic_on = ImageTk.PhotoImage(Image.open(BG_PIC_ON))
        self.bg_label.config(image=self.bg_pic_on)
        # Background button change to show that button was clicked 
        self.btn_wait_bg = ImageTk.PhotoImage(Image.open(BTN_WAIT_BG))
        self.btn_start.config(image=self.btn_wait_bg)
        
        # Create an assistant instance, while assistant is working keep GUI on
        vinx = engine.Assistant()
        vinx.runAssistant()
        
        # Turn GUI off 
        return 


''' Program execution '''

if __name__ == '__main__':
 
    app = MainWindow() # create a mainwindow object and store the reference in variable app
    app.root.mainloop()
