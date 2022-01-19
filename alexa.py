import speech_recognition as sr 
import pyttsx3 
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
def talk (text):
    engine.say(text)
    engine.runAndWait()
    
myjoke= pyjokes.get_joke(language="en",category="neutral")
#talk(myjoke)

def take_command():
    command=''
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis','')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
        
while True:
    run_alexa()

