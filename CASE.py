import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia 
import os
import pyjokes
import random as rm 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Mornin')
    elif hour>=12 and hour<18:
        speak('Afternoon')
    else:
        speak('Evening')    

    speak('This is CASE')
       


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1.0
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f"Coop : {query}\n")

    except Exception:

        speak('Coop it was not clear come again:')
        return "None"
    return query       


if __name__ == "__main__":
   wishMe()
   while True:
    query = takeCommand().lower()
    
    if 'who is' in query:
        speak('Searching')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("according to wikipedia")
        speak(results)

    elif "story of" in query:
        speak("searching for the novel, it might take a while")
        query = query.replace("wikipedia", "")
        novel = wikipedia.summary(query, sentences=5)
        speak ("according to the sources")
        speak(novel)

    elif "tell me a joke" in query:
        speak ("okay, let me thik of one")
        joke = pyjokes.get_joke(language="en" , category="all")
        speak(joke)
    
    elif "tell me a toungue twister" in query:
        speak("okay try this one")
        joke = pyjokes.get_joke(language="en" , category="twister")
        speak(joke)
        
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        speak("opening youtube")
    
    elif 'open google' in query:
        webbrowser.open('google.com')
        speak("opening google")
    
    elif 'messages' in query:
        webbrowser.open('web.whatsapp.com')
        speak("opening whatsapp")
    
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    
    elif 'Photoshop'  in query:
        codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe"
        speak("opening photoshop")
        os.startfile(codePath)
    
    elif 'open code' in query:
        codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        speak("opening VS code")
    
    elif 'open nicepage' in query:
        codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Nicepage\\Nicepage.exe"
        
        
    elif 'lets play' in query:
        if "lets play" == query:
            speak('Lets play Rock peper Scissors')
            if 'ok lets play' in query:
                speak('On the count of three')
                speak('one,two,three')
                options = ["rock","paper","scissor"]
                select = rm.choice(options)
                for val in query:
                    if ('rock' or 'paper' or 'scissor') in query:
                        res=speak(select)
                    elif query == res:
                        speak('its a tie')
                    elif query == "rock" and res== "paper":
                        speak ("i win")
                    elif query == "paper" and res == "scissor":
                        speak("i win")
                    elif query == "scissor" and res == "rock":
                        speak ("i win")
                    elif query == "rock" and res == "scissor":
                        speak ("you win")
                    elif query == "paper" and res == "rock":
                        speak ("you win")
                    elif query == "scissor" and res == "paper":
                        speak ("you win")
                
    elif 'stop' in query:
        speak("Signing of for now, see you soon Coop")
        break            