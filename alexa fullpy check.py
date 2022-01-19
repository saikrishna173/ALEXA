import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random

listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print("listening....")
        listner.adjust_for_ambient_noise(source)
        voice=listner.listen(source)
        global command 
        command=listner.recognize_google(voice)
        command=command.lower()
        if "jarvis" in command:
            command=command.replace("jarvis","")        
            
        return command
def run_alexa():
    command=take_command()
    print(command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing "+song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("current time is "+time)

    elif "who is" in command:
        person=command.replace("who is ","")
        info=wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "what is" in command:
        person=command.replace("what is ","")
        info=wikipedia.summary(person, 1)
        print(info)
        talk(info)    

    elif "what do you mean by" in command:
        person=command.replace("what do you mean by ","")
        info=wikipedia.summary(person, 1)
        print(info)
        talk(info)    

    elif "date" in command:
        x = datetime.datetime.now()
        print(x)
        talk(x)              
    elif "who created you" in command:
        talk("MASTER SAI KRISHNA ")
    elif "tell me a story" in command:
        talk("here is a short story")
        Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
        character = [' there lived a king.',' there was a man named Jack.',' there lived a farmer.']
        once = [' One day', ' One full-moon night']
        story_plot = [' he was passing by',' he was going for a picnic to ']
        place = [' the mountains', ' the garden']
        second_character = [' he saw a man', ' he saw a young lady']
        age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
        work = [' searching something.', ' digging a well on roadside.']
        talk(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(once)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "hello" in command:
        talk("hello from the other side")
    elif "hi" in command:
        talk("hello")
    elif "bhai" in  command:
        talk("bye bye  it was nice talking to you")
    elif "thank you" in command:
        talk("YOUR WELCOME")
    elif "good morning" in command:
        talk("very good morning have a nice day")
    elif "good night" in command:
        talk("good night and sweet dreams")
        talk("have an excellent day ahead")
    else:
        talk("please say the command again")
        

        
while True:
 run_alexa()