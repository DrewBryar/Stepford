import discord 
from discord.ext import commands
import pyttsx3
from playsound import playsound
import os

# End of Script we run...
TOKEN = open("token.txt","r").readline()

bot = commands.Bot(command_prefix = 'Stepford, please ')

# Discord.py_______________________________________________
# https://pypi.org/project/discord.py/
# >> pip install discord.py


# TTS______________________________________________________
engine = pyttsx3.init()
voices = engine.getProperty('voices')

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

# __________________________________________________________

# Speech Recognition________________________________________
# >> pip install SpeechRecognition
# __________________________________________________________

arpeg = "media/audio/arpeg.mp3"
applause = "media/audio/applause.mp3"

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

@bot.command()
async def sayAnne(ctx):
    engine.say("This is how I say Ayanne. This is how I say A N.")

    engine.runAndWait()

@bot.command()
async def say(ctx, arg):
    await ctx.send(f'You want me to say "{arg}", sir?')
    os.system("mpg123 " + arpeg)
    engine.say(f"{arg}.")
    engine.runAndWait()

@bot.command()
async def seeVolume(ctx):
    await ctx.send(f'The current volume is {volume}.')

@bot.command()
async def setVolume(ctx, arg):
    arg = float(arg)
    volume = float(engine.getProperty('volume'))
    previousValue = volume
    volume = arg
    if (volume > 1) or (volume < 0):
        volume = previousValue
        await ctx.send(f'I am terribly sorry, but the range must be from 0 to 1.0. Try that first.')
    else:
        engine.setProperty('volume', volume)
        await ctx.send(f'The volume is now at {volume}')
        engine.say(f"Beep beep beep.")
        engine.runAndWait()

@bot.command()
async def seeRate(ctx):
    await ctx.send(f'The current rate is {rate}.')


@bot.command()
async def setRate(ctx, arg):
    arg = int(arg)
    rate = arg
    engine.setProperty('rate', rate)
    await ctx.send(f'The rate is now at {rate}.')
    engine.say(f"Beep beep beep.")
    engine.runAndWait()

@bot.command()
async def congratulate(ctx, arg):
    engine.say(f'I guess {arg} did well, sir. I suppose we celebrate.')
    engine.runAndWait()
    await ctx.send(f'Wow, you sure did it, {arg}! I have never seen any do *it* as much as you have done it, presently. Let us give a hand to {arg}, one more time.')
    os.system("mpg123 " + applause)


@bot.command()
async def helpMe(ctx):
    await ctx.send('**CURRENT COMMANDS**')
    await ctx.send('Thank you for inquiring my current potential abilities. As you have deduced, you can summon me at most times by just saying "Stepford, please ____" (manners are imperative) and I will be at your service.')
    await ctx.send('However, my brain is still working, so my commands are limited. Here are a few to try.')
    await ctx.send('**ping // pong**')
    await ctx.send('-- Makes sure I am working and gives my ping... and pong')
    await ctx.send('**congratulate**')
    await ctx.send('-- Ah, someone has done well? Give them an attaboy from their old pal Stepford. No sarcasm at all. Simply say "Stepford, please congratulate (PERSON NAME HERE)')

@bot.command()
async def introduce(ctx, arg):
    await ctx.send('Ah, thank you sir. My name is Stepford, and starting now, I should be online to help... although I cannot help much at the moment.')
    await ctx.send('I also refuse to be confined in this current channel, and will be summonable in every channel.')
    await ctx.send('Please, mind your manners. I will be doing my best, but I am new. I appreciate any sort of "**limit tests**", but show mercy.')
    await ctx.send('For now, you can find a small list of features by typing "Stepford, please helpMe". Thank you all @here for your time.')
bot.run(TOKEN) 