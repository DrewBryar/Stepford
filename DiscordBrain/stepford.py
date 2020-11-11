import discord 



from discord.ext import commands


# End of Script we run...
TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '$')

# answers with the ms latency
@client.command()
async def ping(ctx):
    await ctx.send(f'PONG! {round (client.latency * 1000)} ms')

client.run(TOKEN)