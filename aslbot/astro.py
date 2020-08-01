import datetime
import random

from astral import LocationInfo, moon
from astral.sun import sun
from discord.ext import commands
from DbHandler import DbHandler
from discord import File as send_file


class AstroCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.city = LocationInfo("Berlin", "Germany", "Europe/Berlin", 52.52, 13.4)
        self.db = DbHandler()

    @commands.command(name='sun', help="Nautischer Sonnenaufgang und -untergang")
    async def sun_command(self, ctx, ):
        s = sun(self.city.observer, date=datetime.datetime.now())
        message = (f"nautischer Sonnenaufgang: {s['sunrise'].strftime(' %H:%M:%S')} :sunrise:\n"
                   f"nautischer Sonnenuntergang: {s['dusk'].strftime(' %H:%M:%S')} :city_sunset:\n")

        await ctx.send(message)

    @commands.command(name='moon', help="Die heutige Mondphase")
    async def moon_command(self, ctx, ):
        mon_phase = moon.phase(datetime.datetime.now())
        if mon_phase < 6.99:
            message = "Aktuell ist Neumond :new_moon:"
        elif 6.99 < mon_phase < 13.99:
            message = "Aktuell ist zunehmender Mond :first_quarter_moon:"
        elif 14 < mon_phase < 20.99:
            message = "Aktuell ist Vollmond :full_moon:"
        else:
            message = "Aktuell ist abnehmender Mond :last_quarter_moon:"

        await ctx.send(message)

    @commands.command(name='sonne', help="Sie wird heute Nacht nicht untergehen\nUnd die Welt zählt laut bis zehn")
    async def rammstein(self, ctx, ):
        await ctx.send("https://www.youtube.com/watch?v=StZcUAPRRac")

    @commands.command(name='lightspeed', help="Wie lange braucht das Licht? Eingabe in km")
    async def lightspeed_calc(self, ctx, distance: str):
        lightspeed_vacum = 299_792_458
        lightspeed_air = 299_705_518
        lightspeed_water = 225_000_000
        lightspeed_glas = 160_000_000
        try:
            distance_float = float(distance) * 1000
            result_calc = ["Das Licht braucht in folgenden Medium so lange (in s):\n",
                           f"Luft: {distance_float / lightspeed_air}\n",
                           f"Vakum: {distance_float / lightspeed_vacum}\n",
                           f"Wasser: {distance_float / lightspeed_water}\n",
                           f"Glas: {distance_float / lightspeed_glas}\n"]
            await ctx.send("".join(result_calc))
        except ValueError:
            await ctx.send("Bitte nur Zahlen!")

    @commands.command(name='star', help="Lustige fun facts.")
    async def star_command(self, ctx, ):
        fun_facts_universium = [
            "Die Galaxie names NGC 4594 wird uach Sombrero-Galaxie genannt blub.",
            "Der Asteroid Vesta hat einen Durchmesser von 530 km. Da ist die Luftlinie zwischen Berlin und Wien.",
            "Dss Volumen des Mondes ist etwa die Größte des pazifischen Ozean.",
            "Auf dem Planeten Jupiter und Saturn regnet es Diamanten.",
            "Die Nasa-Sonde Mars Climate Orbiter stürzte 1999 auf den Roten Planeten, weil die Hersteller das Navigationssystem mit unterschiedlichen Einheiten gefüttert hatten. Die Nasa hatte metrische Einheiten verwendet, die Ingenieure der Firma Lockheed Martin aber mit Fuß statt Meter gerechnet.",
            "Hunderte Fadenwürmer, an denen die Auswirkungen der Schwerelosigkeit erforscht werden sollten, überlebten den Absturz der Raumfähre Columbia.",
            "HAT-P-1b ist der Name eines Planeten, der im Sternbild Eidechse seine Sonne umkreist. Er ist 1,36-mal so groß wie Jupiter, hat aber nur eine Viertel der Dichte von Wasser.",
            "Im All schnarchen Astronauten nicht so laut wie auf der Erde.",
            "Der Olympus Mons auf dem Mars ist an seinem Fuß so groß, dass ein Besucher auf seinem Gipfel nicht wissen würde, dass er auf einem Berg steht, weil der Abhang von der Planetenkrümmung verdeckt wäre.",
        ]
        await ctx.send(fun_facts_universium[random.randrange(0, len(fun_facts_universium))])

    @commands.command(name="ereignisse", help="Tells you interesting astronomical, observable events occuring soon")
    async def get_events(self, ctx, ):
        events = self.db.get_events()
        if not events:
            await ctx.send(
                "There is either nothing interesting to happen or an error occured. When in doubt check logs.")
            return
        string = ""
        for event in events:
            string = string + "Time: " + str(event["time"]) + "\n" + "Object: " + str(
                event["object"]) + "\n" + "Details: " + str(event["details"]) + "\n\n"
        if not string:
            string = "There is either nothing interesting to happen or an error occured. When in doubt check logs."
        with open("events.txt", "w+") as f:
            f.write(string)
        with open("events.txt", "rb") as f:
            await ctx.send("Here are your astronomic events", file=send_file(f, "ereignisse.txt"))


def setup(bot):
    bot.add_cog(AstroCog(bot))
