import discord 
from discord.ext import commands

# End of Script we run...
TOKEN = open("token.txt","r").readline()

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Back to work, sir.')
    print('--------------------')

# answers with the ms latency
#TEST COMMANDS
@bot.command()
async def ping(ctx):
    await ctx.send(f'PONG! {round (bot.latency * 1000)} ms')

@bot.command()
async def pong(ctx):
    await ctx.send(f'PING! {round (bot.latency * 1000)} ms')




bot.run(TOKEN)