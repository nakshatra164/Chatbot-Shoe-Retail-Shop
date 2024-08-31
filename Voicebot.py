#Step 1

import pyttsx3  #Import this module
import datetime
import speech_recognition as sr  #pip install speech Recognization
import wikipedia  # pip install wikipedia
import os
import random
import pyautogui #pip install pyautogui


#check_open_file = False

#Initiating a voice for Assistant
engine = pyttsx3.init('sapi5')  #to take inbuilt voice available in windows
#Getting Properties of voices prestored in the PC
voices = engine.getProperty('voices')  #voices avai;lable in comp
#print(voices[1].id) #Female voice - voices[1]  Male voice - voices[0]
#Setting voice
engine.setProperty('voice',voices[1].id)  


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour==0 and hour<12:
        speak("Good Morning")
    
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Welcome to shoe tex. We are here to provide you with multiple options For your every day style.How can I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-IN")
        print("User said: {}\n".format(query))

    except Exception as e:
        print(e)
        speak("Say that again please..")
        return "None"
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()




    
    
    
    
    
    
    
    
'''from dis import disco
from re import search
from urllib import request
import webbrowser 
import requests
from bs4 import BeautifulSoup  #pip install bs4'''
