# bot.py
import os
from dotenv import load_dotenv
from discord.ext import commands
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
FORMAT = "[%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(funcName)s()] %(message)s"
logging.basicConfig(filename='bot.log', level=logging.DEBUG, format=FORMAT)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")


bot.load_extension("aslbot.astro")
bot.load_extension("aslbot.programm")
bot.load_extension("aslbot.fun")
bot.load_extension("aslbot.dice")
bot.load_extension("aslbot.zitate")
bot.load_extension("aslbot.base")

print(TOKEN)
bot.run(TOKEN)
