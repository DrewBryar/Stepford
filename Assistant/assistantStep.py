import speech_recognition as sr
import pyttsx3
import os
import time
import playsound
import pyaudio
<<<<<<< HEAD

# ---- Yeah, I can make Stepford speak later. 
# def speak(text):
#     tts = gTTS(text=text, lang='en')
#     filename = 'voice.mp3'
#     tts.save(filename)
#     playsound.playsound(filename)
=======
from commandList import *

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
>>>>>>> 9a844cd8b97cac6f2d91189891bc3357d95e85c2

engine = pyttsx3.init()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
<<<<<<< HEAD
    if "Stepford" == said or said == "deptford":
        engine.runAndWait
        engine.say("Yes, sir, what can I help with?")
        engine.runAndWait()
    else:
        print("You didn't say Stepford.")
    return said


get_audio()
=======

    return said.lower()


WAKE = "stepford"
print("Start")
while True:
    print("Listening...")
    text = get_audio()
    
    if text.count(WAKE) > 0:
        speak("What is it that you require, sir?")
        text = get_audio()

        ALARM_STRS = ["alarm", "set an alarm", "wake me up"]

        REASSURE_STRS = ["i need help", "make me feel better"]
        for phrase in REASSURE_STRS:
            if phrase in text:
                speak("You're going to be okay, sir.")s
        
        DISMISS_STRS = ["nevermind", "scratch that", "sorry"]
        for phrase in DISMISS_STRS:
            if phrase in text:
                speak("Very good sir. I will remain vigilant.")
>>>>>>> 9a844cd8b97cac6f2d91189891bc3357d95e85c2
