import discord 
from discord.ext import commands
import pyttsx3
from playsound import playsound
import os

# End of Script we run...
TOKEN = open("token.txt","r").readline()

bot = commands.Bot(command_prefix = 'Stepford, please ')

# TTS______________________________________________________
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# __________________________________________________________

# Speech Recognition________________________________________
# >> pip install SpeechRecognition
# __________________________________________________________

arpeg = "media/audio/arpeg.mp3"


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Back to work, sir.')
    print('--------------------')
    os.system("mpg123 " + arpeg)
    engine.say("Sir, I am here to help.")
    engine.runAndWait()

# answers with the ms latency
#TEST COMMANDS
@bot.command()
async def ping(ctx):
    await ctx.send(f'PONG! {round (bot.latency * 1000)} ms')
    engine.say("PING! PING! PING! PING! Indeed")
    engine.runAndWait()

@bot.command()
async def pong(ctx):
    await ctx.send(f'PING! {round (bot.latency * 1000)} ms')

@bot.command()
async def love(ctx):
    await ctx.send(f'I will let him know.')
    engine.say("Sir, your lovely girlfriend is thinking about you.")
    engine.runAndWait()

@bot.command()
async def GETDOWN(ctx):
    engine.say("@@@@@@@@@@@@@@@@@@@@@@@")
    engine.runAndWait()

bot.run(TOKEN) 