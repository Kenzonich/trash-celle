import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def check(ctx, trash):
    if trash == "plastik":
        await ctx.send(trash + "ya sampah ini dapat di daur ulang karena termasuk  jenis sampah anorganik ")
    elif trash == "kertas":
        await ctx.send(trash + " ya sampah ini dapat di daur ulang karena termasuk  jenis sampah anorganik")
    elif trash == "kaca":
        await ctx.send(trash + "ya sampah ini dapat di daur ulang karena termasuk  jenis sampah anorganik" )
    elif trash == "logam":
        await ctx.send(trash + " ya sampah ini dapat di daur ulang karena termasuk  jenis sampah anorganik")
    elif trash == "elektronik":
        await ctx.send(trash + "ya sampah ini dapat di daur ulang karena termasuk  jenis sampah anorganik ")
    else:
         await ctx.send(trash + "ya sampah ini dapat di daur ulang karena termasuk  jenis sampah anorganik ")

bot.run("")
