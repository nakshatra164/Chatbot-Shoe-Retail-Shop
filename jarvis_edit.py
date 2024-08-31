#Step 1
import pyttsx3  #Import this module
import datetime
import speech_recognition as sr  #pip install speech Recognization
import wikipedia  # pip install wikipedia
import webbrowser 
import os
import random

#Initiating a voice for Jarvis
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

    speak("I am Jarvis. Please tell me how may I help you")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()




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
        print("Say that again please..")
        return "None"
    return query


def run_program():
    

    wish_me()
    while True:
        query = takeCommand().lower()


    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("Playing music")
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            #print(songs)
            random_number = random.randint(0,12)
            os.startfile(os.path.join(music_dir,songs[random_number]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak("The time is {}".format(strTime))

        elif 'spotify' in query:
            spotify_1 = "C:\\Users\\Nakshatra\\AppData\\Roaming\\Spotify\\Spotify.exe"
            speak("Opening Spotify")
            os.startfile(spotify_1)

        elif 'whatsapp' in query:
            whatsapp = "C:\\Users\\Nakshatra\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak("Opening Whatsapp")
            os.startfile(whatsapp)
        
        elif 'stop the program' in query:
            speak("Okay Bye Bye See you again Later")
            quit()

        elif 'thank you' in query:
            speak("You're Welcome")
        
        elif 'how are you' in query:
            speak("I am fine")



if __name__=="__main__":
    while True:
        query = takeCommand().lower()

        if 'hey jarvis' in query:
            speak("Hello Nax")
            run_program() 