import os, discord
from discord.ext import commands 
from discord.ext.commands import bot 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} hello!')

@bot.command(name="test")
async def response(ctx):
    res = "Literally just a test response string"
    await ctx.send(res)

# Runs the bot's token        
bot.run(TOKEN)

#Start actual coding

