# We're trying to keep thes Bluetooth speaker awake by consistently forcing it to play silence.
import time
from playsound import playsound
# To make sure this is working, we'll substitute a beep for the silent mp3.
testingEnvironment = True
silence = "/home/pi/Stepford/media/1-second-of-silence.mp3"
beepNoise = '/home/pi/Stepford/media/beep-08b.mp3'
minuteInterval = 3


while True:
    playsound(silence)
    time.sleep(minuteInterval*60)

