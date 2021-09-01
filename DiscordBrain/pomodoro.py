import time
from playsound import playsound
import os
import pyttsx3

testing = True
arpeg = "/home/pi/Stepford/DiscordBrain/media/audio/arpeg.mp3"
engine = pyttsx3.init()

if testing:
    workTime = 5
    breakTime = 3
else:
    workTime = 25 * 60
    breakTime = 25 * 60


print("Hi")


def pomodoroCycle(phase):
    print("Phase "+str(phase))
    print("25 Minute Work Period Starts Now")
    os.system("mpg123 " + arpeg)
    engine.say("Work has resumed, sir.")
    engine.runAndWait()
    time.sleep(workTime)
    os.system("mpg123 " + arpeg)
    engine.say("Take a break, sir.")
    engine.runAndWait()
    print('Break Time Starting Now!')
    time.sleep(breakTime)


def pomodoroTimer():
    for i in range(1, 5):
        pomodoroCycle(i)


pomodoroTimer()
