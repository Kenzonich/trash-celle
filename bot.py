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
        await ctx.send(trash + " ini dapat di daur ulang")
    elif trash == "kertas":
        await ctx.send(trash + " ini dapat di daur ulang")
    elif trash == "kaca":
        await ctx.send(trash + " ini dapat di daur ulang")
    elif trash == "logam":
        await ctx.send(trash + " ini dapat di daur ulang")
    elif trash == "elektronik":
        await ctx.send(trash + " ini dapat di daur ulang")
    else:
         await ctx.send(trash + " ini tidak dapat di daur ulang")

bot.run("")
