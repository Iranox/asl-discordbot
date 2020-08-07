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
            "Die Galaxie names NGC 4594 wird auch Sombrero-Galaxie genannt.",
            "Der Asteroid Vesta hat einen Durchmesser von 530 km. Da ist die Luftlinie zwischen Berlin und Wien.",
            "Dss Volumen des Mondes ist vergleichbar mit der Größe des pazifischen Ozean.",
            "Auf dem Planeten Jupiter und Saturn regnet es Diamanten.",
            "Die Nasa-Sonde Mars Climate Orbiter stürzte 1999 auf den Roten Planeten, weil die Hersteller das Navigationssystem mit unterschiedlichen Einheiten gefüttert hatten. Die Nasa hatte metrische Einheiten verwendet, die Ingenieure der Firma Lockheed Martin aber mit Fuß statt Meter gerechnet.",
            "Hunderte Fadenwürmer, an denen die Auswirkungen der Schwerelosigkeit erforscht werden sollten, überlebten den Absturz der Raumfähre Columbia.",
            "HAT-P-1b ist der Name eines Planeten, der im Sternbild Eidechse seine Sonne umkreist. Er ist 1,36-mal so groß wie Jupiter, hat aber nur eine Viertel der Dichte von Wasser.",
            "Im All schnarchen Astronauten nicht so laut wie auf der Erde.",
            "Der Olympus Mons auf dem Mars ist an seinem Fuß so groß, dass ein Besucher auf seinem Gipfel nicht wissen würde, dass er auf einem Berg steht, weil der Abhang von der Planetenkrümmung verdeckt wäre.",
            "Das Sternbild Schild (südlich des Schwanes) ist dem Wappen des polnischen Königs Jan III. Sobieski gewidmet, der die Stadt Wien von türkischen Belagerern befreite.",
            "Der Mars Rover Curiosity war darauf programmiert, jedes Jahr sich selber Happy Birthday zu singen.",
            "Nur unser Heimatplanet Erde im Sonnensystem ist nach keiner Gottheit benannt.",
            "Auf der Venus regnet es Schwefelsäure.",
            "Auf dem kleinsten Saturnmond Mimas ist die Gravitation so gering, dass ein erwachsener Mensch aus dem Stand über 70 m hoch springen könnte",
            "Der größte Meteorit aus Deutschland lag jahrelang dekorativ im Garten und dann im Kleiderschrank, bis er dieses Jahr wissenschaftlich untersucht worden ist.",
            "Der Kern des Jupiters ist heißer als die Oberfläche unserer Sonne.",
            "Wer seine eigene Nichtigkeit im Universum visualisiert haben möchte, sollte sich das Video 'Powers of Ten' auf Youtube ansehen.",
            "Würde man die körpereigene DNA komplett entrollen, würde sie bis zum Pluto reichen... 6 mal hin und zurück (über 54 Millionen Kilometer)."
            "Wir sind alle aus Sternenstaub (den Fusionsüberresten alter Sonnen, die vor Milliarden Jahren verbrannten und explodierten).",
            "Die Datenmenge für das erste Bild eines Schwarzen Loches (im Herzen der Galaxie Messier 87) betrug über 3500 Terabyte an Rohdaten. Das sind gut 70.000 mal alle ASL Filme.",
            "Ein Jahr auf der Venus dauert 224 Erdtage. Ein Tag auf der Venus dauert 243 Erdtage. Somit ist ein Tag länger als ein Jahr auf diesem Planeten.",
            "Es gibt schätzungsweise 300 Trilliarden Sterne im Universum (3x10^23) (grob gerundet und geschätzt), was mehr ist als Sandkörner auf der Erde existieren.",
            "Das ASL ist das einzige kosmische Ereignis, was jährlich eine Unzahl junger Menschen um ihren Schlaf, Verstand und Süßigkeitenvorrat bringt.",
            "Astronauten müssen tatsächlich auf Bohnen verzichten, da Raumanzüge nicht für ausreichenden Gasaustausch konzipiert sind.",
            "Ein Venusjahr ist kürzer als ein Venustag.",
            "Da der Mond keine (nennenswerte) Athmosphäre hat, bleiben Fusspuren dort sehr Lange sichtbar.",
            "Die Chance binnen eines Jahres von einem Stück Weltraummüll erschlagen zu werden, liegt bei eins zu einer Milliarde",
            "Astronauten der ISS sehen täglich 15 Sonnenauf- und -untergänge.",
            "Die Milchstraße wiegt neuesten Messungen zu Folge ca 960 Milliarden Sonnenmassen.",
            "Auf dem Mond liegen tatsächlich zwei Golfbälle rum.",
            "In Chile kann man Wein kaufen, der Milliarden Jahre altes Meteoritengestein enthält.",
            "Der Asteroid Chariklo hat saturnähnliche Ringe im Miniaturformat.",
            "Der Exoplanet 55 Cancri e ist höchstwahrscheinlich von Graphit und Diamanten bedeckt.",
            "Auf dem Exoplaneten HD 189733b regnet es vermutlich Glas.",
            "In Australien sieht der Mond für Europäer um 180° gedreht aus.",
            "Hunderte Fadenwürmer, an denen die Auswirkungen der Schwerelosigkeit erforscht werden sollten, haben den Absturz der Raumfähre Columbia überlebt.",
            "Hartnäckigen Gerüchten zufolge hat sich ein amerikanisches Astronauten-Paar 1996 wissenschaftlich mit Sex in der Schwerelosigkeit beschäftigt. Demnach seien vier Stellungen für die Bedingungen im Weltall geeignet. Die Nasa dementiert.",
            "In der Schwerelosigkeit haben Astronauten oft verstopfte Nasen. Der Rotz fließt nicht ab.",
            "Die Milchstraße hat eine Begleitergalaxie namens \"Sextans Dwarf\"",
            "Asien ist flächenmäßig größer als der Mond.",
            "Sonnenuntergänge erscheinen auf dem Mars bläulich.",
            "Die Entdeckung des Pluto ist erst ein drittel Plutojahr her.",
            "Am 2.11.2000 waren zuletzt alle lebenden Menschen auf der Erde. Seit dem ist die ISS permanent bemannt.",
            "Von 1781 bis 1850 nannte man Uranus noch George.",
            "Der ursprünglich für eine Missionsdauer von 90 Tagen konzipierte Mars-Rover Opportunity verrichte seinen Dienst tatsächlich 15 Jahre lang.",
            "Es is anatomisch unmöglich in der Schwerelosigkeit zu rülpsen.",
            "Die Entdekcung des Planeten Uranus im Jahr 1781 fand noch vor der Entdeckung der Antarktis im Jahr 1820 statt."
        ]
        await ctx.send(fun_facts_universium[random.randrange(0, len(fun_facts_universium))])

    @commands.command(name="ereignisse", help="Listet interessante astronomische Ereignisse auf, die in nächster Zeit "
                                              "zu sehen sind.")
    async def get_events(self, ctx, ):
        events = self.db.get_events()
        if not events:
            await ctx.send(
                "Entweder es gibt demnächst nichts interessantes oder irgendwas ist schief gelaufen :(")
            return
        string = ""
        for event in events:
            string = string + "Time: " + str(event["time"]) + "\n" + "Object: " + str(
                event["object"]) + "\n" + "Details: " + str(event["details"]) + "\n\n"
        if not string:
            string = "Entweder es gibt demnächst nichts interessantes oder irgendwas ist schief gelaufen :("
        with open("events.txt", "w+") as f:
            f.write(string)
        with open("events.txt", "rb") as f:
            await ctx.send("Hier sind die spannenden Ereignisse!", file=send_file(f, "ereignisse.txt"))


def setup(bot):
    bot.add_cog(AstroCog(bot))
