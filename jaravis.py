# from gettext import install
from cgitb import text
from unicodedata import category
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import subprocess



def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing...")
            data=recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print(" Not Understanding ")


def texttospeech(x):
    
    engine= pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate= engine.getProperty('rate')
    engine.setProperty('rate',60)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':

    texttospeech("Welcome to Commander")
    subprocess.call(["afplay","/Users/suhanisehgal/Downloads/track_welcome.wav"])

    while True:
        data1=sptext().lower()

        if "exit" in data1:
            texttospeech("OK, getting closed")
            break

        elif "your name" in data1:
            name="my name is google."
            print(name)
            texttospeech(name)

        elif "old are you" in data1:
            age="I am two months old."
            texttospeech(age)

        elif "your age" in data1:
            age="I am two months old."
            texttospeech(age)
        
        elif "time" in data1:
            time=datetime.datetime.now().strftime("%I %M %p")
            print(time)
            texttospeech(time)

        elif "open google" in data1:
            webbrowser.open("https://www.google.com/")
            texttospeech("OK")

        elif "calendar" in data1:
            webbrowser.open("https://calendar.google.com/")
            texttospeech("OK")

        elif "open youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
            texttospeech("OK")
        
        elif "spotify" in data1:
            webbrowser.open("https://www.spotify.com/")
            texttospeech("OK")
        
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(category="neutral")
            print(joke_1)
            texttospeech(joke_1)

        elif "play song" in data1:
            subprocess.call(["afplay","/Users/suhanisehgal/Downloads/track_sound.wav"])
    
    subprocess.call(["afplay","/Users/suhanisehgal/Downloads/track_exit.wav"])
    print("Thanks!")
        
  