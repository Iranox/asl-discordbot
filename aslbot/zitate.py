from discord.ext import commands
from discord import File as send_file
from datetime import datetime, timedelta
import os
from DbHandler import DbHandler
import helper


class QuoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DbHandler()

    @commands.command(name='zitat', help='Gib das Zitat wie folgt an: \"!zitat \"author=AUTOR\" \"text=ZITAT\" '
                                         '\"comment=KOMMENTAR\" \"date=ZEITPUNKT\"\nWichtig: Alle Parameter müssen '
                                         'mit \"\" umfasst werden. Alle Parameter außer text sind optional. Die '
                                         'Reihenfolge der Parameter spielt keine Rolle.')
    async def add_quote(self, ctx, *args):
        param_dict = {}
        for parameter in args:
            splitted = parameter.split("=")
            if len(splitted) != 2:
                await ctx.send("Ich verstehe nicht: " + parameter)
                return
            parameter_name = splitted[0]
            parameter_value = splitted[1]
            param_dict[parameter_name] = parameter_value
        if "text" in param_dict.keys():
            text = param_dict["text"]
            del param_dict["text"]
        else:
            await ctx.send("Das Zitat fehlt! Schreibe \"!help zitat\" um zu erfahren, wie man das Kommando benutzt")
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
            await ctx.send("Unbekannter Parameter: " + str(param_dict.keys()))
            return
        date = None
        recorder = str(ctx.message.author.name)
        query = self.db.add_quote(author=author, text=text, comment=comment, date=date, recorded_by=recorder)
        if query:
            await ctx.send("Zitat wurde hinzugefügt :)")
        else:
            await ctx.send("Zitat konnte nicht hinzugefügt werden. Fehlerbeschreibung ist in den Logs :(")

    @commands.command(name="zitate_lesen", help="Zeigt alle archivierten Zitate an. Optional kann mit \"from=%Y-%M-%D "
                                                "%H:%M:S\", \"until=%Y-%M-%D %H:%M:S\" die Zeitspanne der Zitate, "
                                                "die angezeigt werden sollen, eingeschränkt werden.\nWichtig: Alle "
                                                "Parameter müssen in \"\" eingefasst sein. Die Reihenfolge der "
                                                "Parameter spielt keine Rolle. Wenn ein Parameter benutzt wird, "
                                                "müssen Jahr, Monat und Tag eingegeben werden, Stunde, Minute und "
                                                "Sekunde werden auf 0 gesetzt, wenn nicht angegeben.")
    async def get_quotes(self, ctx, *args):
        param_dict = {}
        for parameter in args:
            splitted = parameter.split("=")
            if len(splitted) != 2:
                await ctx.send("Ich verstehe nicht: " + parameter)
                return
            parameter_name = splitted[0]
            parameter_value = splitted[1]
            param_dict[parameter_name] = parameter_value
        if "from" in param_dict.keys():
            from_time = param_dict["from"]
            if not helper.verify_timestamp(from_time):
                await ctx.send("Ungültiger Zeitstempel: " + from_time)
                return
            del param_dict["from"]
        else:
            from_time = datetime.now() - timedelta(days=1)
        if "until" in param_dict.keys():
            until_time = param_dict["until"]
            if not helper.verify_timestamp(until_time):
                await ctx.send("Ungültiger Zeitstempel: " + until_time)
                return
            del param_dict["until"]
        else:
            until_time = None
        if param_dict.keys():
            await ctx.send("Unbekannter Parameter: " + str(param_dict.keys()))
            return
        query = self.db.get_quotes(from_time=from_time, until_time=until_time)
        if query:
            text = str(query)
            if len(text) > 1800:
                with open("zitate.txt", "w+") as f:
                    f.write(text)
                with open("zitate.txt", "rb") as f:
                    await ctx.send("Hier sind die Zitate :)", file=send_file(f, "zitate.txt"))
                os.remove("zitate.txt")
                return
            await ctx.send("Zitate:\n" + str(query))
        else:
            await ctx.send("Kann die Zitate nicht anezigen. Fehlerbeschreibung in den Logs :(")

    @commands.command(name="alle_zitate_lesen", help="Zeigt alle archivierten Zitate an. Optional kann mit "
                                                     "\"from=%Y-%M-%D %H:%M:S\", \"until=%Y-%M-%D %H:%M:S\" die "
                                                     "Zeitspanne der Zitate, die angezeigt werden sollen, "
                                                     "eingeschränkt werden.\nWichtig: Alle Parameter müssen in \"\" "
                                                     "eingefasst sein. Die Reihenfolge der Parameter spielt keine "
                                                     "Rolle. Wenn ein Parameter benutzt wird, müssen Jahr, "
                                                     "Monat und Tag eingegeben werden, Stunde, Minute und Sekunde "
                                                     "werden auf 0 gesetzt, wenn nicht angegeben.")
    async def get_all_quotes(self, ctx, *args):
        param_dict = {}
        for parameter in args:
            splitted = parameter.split("=")
            if len(splitted) != 2:
                await ctx.send("Ich verstehe nicht: " + parameter)
                return
            parameter_name = splitted[0]
            parameter_value = splitted[1]
            param_dict[parameter_name] = parameter_value
        if "from" in param_dict.keys():
            from_time = param_dict["from"]
            if not helper.verify_timestamp(from_time):
                await ctx.send("Ungültiger Zeitstempel: " + from_time)
                return
            del param_dict["from"]
        else:
            from_time = None
        if "until" in param_dict.keys():
            until_time = param_dict["until"]
            if not helper.verify_timestamp(until_time):
                await ctx.send("Ungültiger Zeitstempel: " + until_time)
                return
            del param_dict["until"]
        else:
            until_time = None
        if param_dict.keys():
            await ctx.send("Unbekannter Parameter: " + str(param_dict.keys()))
            return
        query = self.db.get_quotes(from_time=from_time, until_time=until_time)
        if query:
            text = str(query)
            if len(text) > 1800:
                with open("zitate.txt", "w+") as f:
                    f.write(text)
                with open("zitate.txt", "rb") as f:
                    await ctx.send("Hier sind die Zitate :)", file=send_file(f, "zitate.txt"))
                os.remove("zitate.txt")
                return
            await ctx.send("Zitate:\n" + str(query))
        else:
            await ctx.send("Kann die Zitate nicht anezigen. Fehlerbeschreibung in den Logs :(")

    @commands.command(name="man_munkelt",
                      help="Verwende wie folgt: !man_munkelt \"dass, der Bot jetzt auch munkeln kann!\"")
    async def add_munkel(self, ctx, *args):
        if len(args) != 1:
            await ctx.send("Falsche Benutzung, gebe !help man_munkelt ein, um zu erfahren, wie das Kommando benutzt "
                           "wird")
            return
        query = self.db.insert_munkel(args[0])
        if not query:
            await ctx.send("Konnte nicht munkeln, näheres in den Logs :(")
        else:
            await ctx.send("Erfolgreich gemunkelt :)")

    @commands.command(name="gemunkelt", help="Zeigt alles, was so gemunkelt wird. Mit \"von=timestamp\" und "
                                             "\"bis=timestamp\" kann der Zeitraum eingeschränkt werden. Beide "
                                             "Parameter sind optional, sofern \"von\" nicht gesetzt ist, "
                                             "werden automatisch nur die letzten 24Std gelesen.")
    async def read_munkels(self, ctx, *args):
        param_dict = {}
        for parameter in args:
            splitted = parameter.split("=")
            if len(splitted) != 2:
                await ctx.send("Ich verstehe nicht: " + parameter)
                return
            parameter_name = splitted[0]
            parameter_value = splitted[1]
            param_dict[parameter_name] = parameter_value
        if "von" in param_dict.keys():
            from_time = param_dict["von"]
            if not helper.verify_timestamp(from_time):
                await ctx.send("Ungültiger Zeitstempel: " + from_time)
                return
            del param_dict["von"]
        else:
            from_time = None
        if "bis" in param_dict.keys():
            until_time = param_dict["bis"]
            if not helper.verify_timestamp(until_time):
                await ctx.send("Ungültiger Zeitstempel: " + until_time)
                return
            del param_dict["bis"]
        else:
            until_time = None
        if param_dict.keys():
            await ctx.send("Unbekannter Parameter: " + str(param_dict.keys()))
            return
        query = self.db.read_munkel(time_from=from_time, time_until=until_time)
        if query:
            text = str(query)
            if len(text) > 1800:
                with open("munkel.txt", "w+") as f:
                    f.write(text)
                with open("munkel.txt", "rb") as f:
                    await ctx.send("Es wird gemunkelt, dass... :)", file=send_file(f, "munkel.txt"))
                os.remove("munkel.txt")
                return
            await ctx.send("Man munkelt, dass...\n" + str(query))
        else:
            await ctx.send("Kann nicht sagen, was gemunkelt wird. Fehlerbeschreibung in den Logs :(")


def setup(bot):
    bot.add_cog(QuoteCog(bot))
