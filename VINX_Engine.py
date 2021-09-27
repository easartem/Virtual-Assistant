import speech_recognition as sr
import pyttsx3
import VINX_Utils as util

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
        self.speak("Démarrage de l'assistant") 

        '''Speech-To-Text recognizer'''
    
    
    # Methods - Behaviours 

    '''Text-To-Speech engine'''
    def speak(self, text):
        print("Entering self-made speak function")
        self.engine.say(text)
        self.engine.runAndWait()

    '''Text-To-Speech engine''' 
    def listen(self):
        print("Vinx is listenning...")
        # get audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source)
            
        # try to use Google's speech recognition API to convert audio to text
        try:
            speech = r.recognize_google(audio, language="fr-FR") #'en-in' if necessary
            print("You said : ", speech, "\n")
            self.speak("Tu as dit")
            self.speak(speech)

        except sr.UnknownValueError:
            print("Ai couldn't understant what you said")
            self.speak("Je n'ai pas compris, pouvez-vous répéter")
            return "None"
        except sr.RequestError as e:
            print("Ai couldn't request results; {0}".format(e))
            return "None"
        return speech

    '''Text-To-Speech engine'''
    def runAssistant(self):
        txt = self.listen()
        #self.speak(txt)
        if "heure" in txt:
            self.speak("Vous avez utilisé le mot heure")
            current_time = util.get_time()
            self.speak("il est " + current_time)
        elif "cherche" in txt:
            self.speak("Vous avez utilisé le mot cherche")
        else:
            self.speak("Je n'ai pas compris, pouvez vous-répéter ?")



