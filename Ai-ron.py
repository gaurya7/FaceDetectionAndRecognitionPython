import string


import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pyjokes
import smtplib
import sys
import time
import serial


ArduinoSerial = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

time.sleep(1)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    Jaw_Open()
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    Jaw_Close()

def Jaw_Open():

    Jaw = "J1";
    ArduinoSerial.write(Jaw.encode('utf-8'))
def Jaw_Close():

    Jaw = "J0";
    ArduinoSerial.write(Jaw.encode('utf-8'))



def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query
def wish():
    hour = int(datetime.datetime.now().hour)
    #ArduinoSerial.write(string.encode('utf-8'))
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am Ron. Please tell me how may i help you")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('krishnakadam869@gmail.com', 'pqmkdohmslmmmsff')
    server.sendmail('krishnakadam869@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    takecommand()
    #speak( )
    while True:


        query = takecommand().lower()

        # logic building for tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open code" in query:
            apath = "C:\\Users\\krish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "tell me about your self" in query:
            speak("hii...! I am Ai-Ron I am Ai Robot")
        elif "tell me how were you made" in query:
            speak("I am created using Python & Arduino . Python makes me smart . Arduino helps me move accordingly")
        elif "introduce yourself" in query:
            speak("My name is Ai-RON. i am five month old i was created in winter 2021. i am product of Artificial intelligence and robotics ")
        elif "who inspires you" in query:
            speak("Sophia robot, I am a fan of hers")
        elif "your favourite car" in query:
            speak("My favourite car is Tesla")
        elif "your favourite movie" in query:
            speak("Iron Man")
        elif "your favourite colour" in query:
            speak("Orange")


        elif "play music" in query:
            music_dir = "F:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")



        elif "email to ishan" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "ishan685@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to ishan")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to ishan")

        elif "close notepad" in query:
            speak("ok sir,closing notepad")
            os.system(("taskkill/f/im.notepad.exe"))





