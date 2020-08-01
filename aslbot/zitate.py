from discord.ext import commands
from DbHandler import DbHandler
import helper


class QuoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DbHandler()

    @commands.command(name='zitat', help='Provide quote as follows \"!zitat \"author=AUTOR\" \"text=ZITAT\" \"comment=KOMMENTAR\" \"date=ZEITPUNKT\"\nNote that all arguments need to be encapsulated in \"\", paramaters are optional besides text. Order of parameters doesn\'t matter')
    async def add_quote(self, ctx, *args):
        param_dict = {}
        for parameter in args:
            splitted = parameter.split("=")
            if len(splitted) != 2:
                await ctx.send("Cannot parse " + parameter)
                return
            parameter_name = splitted[0]
            parameter_value = splitted[1]
            param_dict[parameter_name] = parameter_value
        if "text" in param_dict.keys():
            text = param_dict["text"]
            del param_dict["text"]
        else:
            await ctx.send("Text ist missing! Type \"!help zitat\" to get information about usage of command")
            return
        if "author" in param_dict.keys():
            author = param_dict["author"]
            del param_dict["author"]
        else:
            author = "unknown"
        if "comment" in param_dict.keys():
            comment = param_dict["comment"]
            del param_dict["comment"]
        else:
            comment = None
        if param_dict.keys():
            await ctx.send("Unknown arguments: " + str(param_dict.keys()))
            return
        date = None
        recorder = str(ctx.message.author.name)
        query = self.db.add_quote(author=author, text=text, comment=comment, date=date, recorded_by=recorder)
        if query:
            await ctx.send("Quote has been added")
        else:
            await ctx.send("Quote could not be added, check logs for detail")

    @commands.command(name="zitate_lesen", help="Get's all recorded quotes. Optional parameters \"from=%Y-%M-%D %H:%M:S\", \"until=%Y-%M-%D %H:%M:S\" can be included to only get quotes of a specific time range.\n"
                                           "Note: arguments must be encapsulated in \"\". Order of arguments doesn't matter. Year, Month and Day have to be specified when using the argument. Hour, minute and seconds are defaulted to 00 if not provided.")
    async def get_quotes(self, ctx, *args):
        param_dict = {}
        for parameter in args:
            splitted = parameter.split("=")
            if len(splitted) != 2:
                await ctx.send("Cannot parse " + parameter)
                return
            parameter_name = splitted[0]
            parameter_value = splitted[1]
            param_dict[parameter_name] = parameter_value
        if "from" in param_dict.keys():
            from_time = param_dict["from"]
            if not helper.verify_timestamp(from_time):
                await ctx.send("Invalid timestamp has been provided: " + from_time)
                return
            del param_dict["from"]
        else:
            from_time = None
        if "until" in param_dict.keys():
            until_time = param_dict["until"]
            if not helper.verify_timestamp(until_time):
                await ctx.send("Invalid timestamp has been provided: " + until_time)
                return
            del param_dict["until"]
        else:
            until_time = None
        if param_dict.keys():
            await ctx.send("Unknown arguments: " + str(param_dict.keys()))
            return
        query = self.db.get_quotes(from_time=from_time, until_time=until_time)
        if query:
            await ctx.send("Quotes:\n" + str(query))
        else:
            await ctx.send("Reading quotes failed, check log for details")


def setup(bot):
    bot.add_cog(QuoteCog(bot))
