# bot.py
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")



@bot.command()
async def load(ctx, extension):
    bot.load_extension("aslbot.astro")
    await ctx.send(f'Loaded "{extension}"')
    print(f'Loaded "{extension}"')

    return

bot.load_extension("aslbot.astro")
bot.load_extension("aslbot.programm")
bot.load_extension("aslbot.fun")

print(TOKEN)
bot.run(TOKEN)
