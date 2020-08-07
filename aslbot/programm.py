from datetime import datetime
from discord.ext import commands

from DbHandler import DbHandler


class ProgrammCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DbHandler()

    @commands.command(name='new', help="Setzt neues Programm (nur berechtigte Benutzer)")
    @commands.has_role("Leiter")
    async def sun_command(self, ctx, *programm):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        program = " ".join(programm)
        author = ctx.message.author.name
        query = self.db.set_program(author=author, program=program, date=date)
        if query:
            await ctx.send("Programm ist gesetzt.")
        else:
            await ctx.send("Programm konnte nicht gesetzt werden. Überprüfe Logs.")

    @commands.command(name='programm', help="Zeigt Programm")
    async def get_programm_command(self, ctx):
        program = self.db.get_program()
        await ctx.send(program)


def setup(bot):
    bot.add_cog(ProgrammCog(bot))
