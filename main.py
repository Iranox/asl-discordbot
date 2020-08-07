# bot.py
import os
from dotenv import load_dotenv
from discord.ext import commands
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
FORMAT = "[%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(funcName)s()] %(message)s"
logging.basicConfig(filename='bot.log', level=logging.INFO, format=FORMAT)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")


bot.load_extension("aslbot.astro")
bot.load_extension("aslbot.programm")
bot.load_extension("aslbot.fun")
bot.load_extension("aslbot.dice")
bot.load_extension("aslbot.zitate")
bot.load_extension("aslbot.base")

while True:
    try:
        bot.run(TOKEN)
    except Exception as e:
        logging.error(str(e))
