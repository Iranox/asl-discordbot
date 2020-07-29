# bot.py
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")


bot.load_extension("aslbot.astro")
bot.load_extension("aslbot.programm")
bot.load_extension("aslbot.fun")
bot.load_extension("aslbot.dice")

print(TOKEN)
bot.run(TOKEN)
