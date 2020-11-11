import discord 
from discord.ext import commands
import pyttsx3
# End of Script we run...
TOKEN = open("token.txt","r").readline()

bot = commands.Bot(command_prefix = '$')

# Discord.py_______________________________________________
# https://pypi.org/project/discord.py/
# >> pip install discord.py


# TTS______________________________________________________
# https://pypi.org/project/pyttsx3/
# >> pip install pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #The variable in voices represents a male voice (0) and a female voice (1).
# Maybe pursue new voices? They seem to be system dependent.
# __________________________________________________________

# Speech Recognition________________________________________
# https://pypi.org/project/SpeechRecognition/
# >> pip install SpeechRecognition
# __________________________________________________________


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Back to work, sir.')
    print('--------------------')
    engine.say("Ah, good to see you sir.")
    engine.runAndWait()

# answers with the ms latency
#TEST COMMANDS
@bot.command()
async def ping(ctx):
    engine.say("PONG PONG PONG, sir.")
    engine.runAndWait()
    await ctx.send(f'PONG! {round (bot.latency * 1000)} ms')

@bot.command()
async def pong(ctx):
    await ctx.send(f'PING! {round (bot.latency * 1000)} ms')

@bot.command()
async def voice(ctx):
    await ctx.send(f'My volume is at {volume} and the rate is {rate}')


bot.run(TOKEN) 