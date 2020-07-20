import datetime
import random

from datetime import datetime


from discord.ext import commands

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='party', help="party hard")
    async def sun_command(self, ctx):
        await ctx.send("https://tenor.com/view/party-hard-harrypotter-alan-rickman-dumbledore-gif-4934551")



def setup(bot):
    bot.add_cog(FunCog(bot))
