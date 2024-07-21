# module used :
# setuptools , speechrecognition , pyaudio

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import datetime



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d7d165d9eff948bda3ef6e067cfd36ee"


voices = engine.getProperty('voices')
custom_voice_id = voices[1].id  # Replace 1 with the index of the desired voice from the list
engine.setProperty('voice', custom_voice_id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    current_hour = datetime.datetime.now().hour
    
    if 0 <= current_hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    
    greeting += " Sir How can I assist you today?"
    speak(greeting)



def ask_about_day():
    speak("By the way, how's your day going?")




def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com/")
    elif "open leetcode" in c.lower():
        webbrowser.open("https://www.leetcode.com/")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com/")
    elif "open spotify" in c.lower():
        webbrowser.open("https://www.spotify.com/")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://www.chatgpt.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])


if __name__ == "__main__":
    speak("  Initializing Jarvis....")
    greet_user()
    ask_about_day()
    while True:
        # Obtaining Audio from the microphone 
        r = sr.Recognizer()
        
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source , timeout = 2,  phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yaaah")
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source , timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Jarvis Error: {0}".format(e))