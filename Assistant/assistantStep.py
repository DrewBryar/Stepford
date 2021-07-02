import speech_recognition as sr
import pyttsx3
import os
import time
import playsound
import pyaudio

# ---- Yeah, I can make Stepford speak later. 
# def speak(text):
#     tts = gTTS(text=text, lang='en')
#     filename = 'voice.mp3'
#     tts.save(filename)
#     playsound.playsound(filename)

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
    if "Stepford" == said or said == "deptford":
        engine.runAndWait
        engine.say("Yes, sir, what can I help with?")
        engine.runAndWait()
    else:
        print("You didn't say Stepford.")
    return said


get_audio()