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

    @commands.command(name='blau', help="Blau wie das Meer")
    async def blau(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=TgDXGQYib8k")

    @commands.command(name='trap', help="Admiral Ackbar sagt:")
    async def trap(self, ctx):
        await ctx.send("https://giphy.com/gifs/Z1LYiyIPhnG9O")

    @commands.command(name='darkside', help="Dark site of the force")
    async def darkside(self, ctx):
        await ctx.send("https://gph.is/VxbsSv")

def setup(bot):
    bot.add_cog(FunCog(bot))
