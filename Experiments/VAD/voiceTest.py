from gtts import gTTS
import os
import time

tts = gTTS(text = ' Stepford', lang = 'en')
tts.save("good.mp3")
time.sleep(1)
os.system("mpg123 good.mp3")