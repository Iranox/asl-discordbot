import datetime
import random

from datetime import datetime


from discord.ext import commands

class ProgrammCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.programm = ("Hier steht ihr programm",)
        self.password = "5mal4plus5ergibt25"

    @commands.command(name='new', help="Setzt neues Programm (passwort geschützt)")
    async def sun_command(self, ctx, password, *programm ):
        if password == self.password and password:
            await ctx.send("programm ist gesetzt.")
            self.programm = " ".join(programm).split(";")
        else:
            await ctx.send("password wrong")

    @commands.command(name='programm', help="Zeigt programm")
    async def get_programm_command(self, ctx ):
            await ctx.send("\n".join(self.programm))



def setup(bot):
    bot.add_cog(ProgrammCog(bot))
