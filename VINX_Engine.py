import speech_recognition as sr
import pyttsx3
import datetime

print("Opening script...")



''' Definition of the vocal assistant'''

class Assistant():
    # Skill 1 : Assistant can listen (Speech-To-Text library : speech_recognition)
    # Skill 2 : Assistant can talk (Text-To-Speech library : pyttsx3)
    # Skill 3 : Assistan can interpret (ML)
    # Skill 4 : Assistant can answer (ML & utils functions)

    # Constructors & Instance attribute for properties that vary from one instance to another.
    def __init__(self):

        '''Text-To-Speech engine'''
        print("Starting VINX...")
        self.engine  = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        pyttsx3.speak("Démarrage de l'assistant")

        '''Speech-To-Text engine'''
        print("Vinx is listenning...")
    
    
    # Methods - Behaviours 
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()