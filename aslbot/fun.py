from discord.ext import commands
import random
import datetime

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

    @commands.command(name='darkside', help="Dark side of the force")
    async def darkside(self, ctx):
        await ctx.send("https://gph.is/VxbsSv")

    @commands.command(name='hootsforce', help="A music video with submarines fighting an evil wizard... in space")
    async def space_metal(self, ctx):
        await ctx.send("https://gph.is/VxbsSv")

    @commands.command(name='headache', help="...")
    async def star_trek_headache(self, ctx):
        await ctx.send("https://giphy.com/gifs/6OWIl75ibpuFO")

    @commands.command(name='facepalm', help=":person_facepalming: ")
    async def star_trek_facepalm(self, ctx):
        await ctx.send("https://gph.is/2nBvKOZ")

    @commands.command(name='pika', help="pikaCHUUUUUUUUUU")
    async def pika(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=AjSuZgNgMZc \n Music are like knights. they must be coverd in metal")

    @commands.command(name='pinguin', help="PINGUUUUUIIIIIIIN!")
    async def pinguin(self, ctx):
        await ctx.send("PINGUUIIN!!!!!!")

    @commands.command(name='hallo', help="HAAAAALLLOOOOOO!!!!!!!")
    async def hallo(self, ctx):
        await ctx.send("https://vega-astro.de/wp-content/uploads/2020/01/Lucia.jpg \n HAAAAALLLOOOOOO @all")

    @commands.command(name='damals', help="Früher im ASL war alles besser...")
    async def damals(self, ctx, ):
        old_school = [
            "Man fühlt sich schon besser, wenn man ein großes Teleskop hat, das ist ähnlich wie bei Autos - Jan",
            "Ich habe immer Pyrowatte in der Brusttasche, damit es cool aussieht, wenn ich mal von einer Kugel getroffen werde - Thomas",
            "Alles ist eine Nebelmaschine, wenn man es nur falsch genug bedient - Ines",
            "Mein Bedürfnis nach Koffein ist größer als mein Geschmackssinn - Stefan",
            "Unsere Sonne kreist auch um etwas. Vielleicht ist sie auch ein Planet - Enzo",
            "https://vega-astro.de/wp-content/uploads/2020/02/Startseite5.jpg",
            "https://vega-astro.de/wp-content/uploads/2020/01/WasBietenWir.jpg",
            "https://vega-astro.de/wp-content/uploads/photo-gallery/imported_from_media_libray/Gesus_231-scaled.jpg?bwg=1579449084",
            "https://vega-astro.de/wp-content/uploads/photo-gallery/imported_from_media_libray/Gesus_14-scaled.jpg?bwg=1579449084",
            "https://vega-astro.de/wp-content/uploads/photo-gallery/imported_from_media_libray/Gesus_283-scaled.jpg?bwg=1579449084",
            "https://vega-astro.de/wp-content/uploads/photo-gallery/imported_from_media_libray/Lukas-Weis_p_0011-scaled.jpg?bwg=1579449084",
            "Das habe ich am ASL vermisst. Flache Witze und kein Tee. - Sahra",
            "Es geht los, wenn sie wegrennt. - Jona beim Raketenstart",
            "Du bist der Kaffee meines Lebens! - Sven",
            "Ich weiß nicht, ob ich in den letzten zwölf Jahren überhaupt irgendjemanden umgebracht habe. - Fabi",
            "Lasagne für 80 Leute... Das kriegen wir nicht gebacken... - Küchenfee",
            "Mmmmh, meine Lieblingsgeschmacksrichtung. Chemie! - Paul",
            "Eisfeld ist Europa-Kaff, wahrscheinlich weil se dort letztes Jahr den Euro eingeführt haben - Flo",
            "Alle Gesetze sind gleich für einen Beobachter im Ruhestand. - Adrien",
            "Göthe, wen möchtest du heute verdichten? – Wolfsrunde",
            "Einzelne Teile der Katze messen sich gegenseitig – Stefan",
            "Wer beim ASL-Film mitspielt, hat die Kontrolle über sein ASL verloren. - Sebastian",
            "Gib ihm ein Stopschild, dann hat er einen Anhaltspunkt. - Michi",
            "Ja... Nein, da haben wir ein Speeddating, ähh, -leiting! - Io",
            "Manchen Sachen sind so offensichtlich schlecht, dass man sie erst gar nicht machen muss. – Jonathan",
            "Die Aufgabe der Leiter im ASL ist es, die Grenze zwischen Spaß und Verantwortungslosigkeit auszutesten. - Eric",
            "Ich schlafe immer mit einem Messer unter dem Kopf, für den Fall, dass jemand mit einem Kuchen vorbeikommt - Hannah",
            "Wer will eine Fleischwunde? - Io",
            "So viele Fragen, auf die nicht mal die Physiker keine logische Antwort haben - Vanessa",
            "Ich fühle mich wie ein Nazi, ich krieg’ immer auf die Fresse - Ayan",
            "Aus großer Schubkraft folgt große Verantwortung - Eric",
            "Kostet das was, oder kann man sich das irgendwo herunterladen? - Chiara",
            "Flo hat doch immer Thermit dabei. - Laura",
            "Am besten, ihr nutzt die Pause zum Pausemachen. - Fabi",
            "Leider haben wir keinen mit Lungenentzündung hier. - Aliona",
            "Zwischendurch wirds noch laut knallen – das ist dann Flo. - Sonja",
            "Das ist mir zu nerdig. Sprechen wir über Star Wars. - Phillip",
            "2009: Der Beweis, dass Fernsehreporter nicht wissen, was ein Bose-Einstein-Kondensat ist, wurd erbracht!"
        ]
        await ctx.send(old_school[random.randrange(0, len(old_school))])

    @commands.command(name='kill', help="Mörderspiel!!")
    async def kill(self, ctx):
        await ctx.send("https://i.kinja-img.com/gawker-media/image/upload/vodrkg3c4sr2d17gacwm.jpg")

    @commands.command(name='challenge', help="Was ist die heutige Challenge?")
    async def challenge(self, ctx):
        dt = datetime.datetime.today()
        challenges = {
            3: "Was verbindet uns alle? Die Astronomie natürlich! Der erste Tageschallange ist es einen Gegenstand bei euch Zuhause zu finden der etwas mit Astronomie zu tun hat und ein Bild davon zu posten!",
            4: "Heute und die nächsten 2 Wochen wollen wir gemeinsam die Sterne Beobachten! Macht ein Foto davon, damit wir sie alle sammeln können und so zusammen schauen können! (Challange läuft bis zum Ende des Camps!)",
            5: "ASL-Trauertag: Das ASL ist dieses Jahr nur digital und das ist schade! Macht ein Bild das zeigt wie ihr das ASL vermisst!",
            6: "Die Zeitung braucht eure Hilfe! Malt ein Kalenderblatt zum Sammeln!",
            7: "Was darf in keinem guten ASL fehlen? Raketen! Bastelt also eine Rakete die ihr im nächsten ASL starten lassen könnt und präsentiert sie uns per Bild! (Zum gemeinsamen Basteln könnt ihr euch in der Werkstatt treffen und da auch ein paar Anleitungen finden) (Challange läuft bis zum Ende des Camps)",
            8: "Was passiert am 7ten Tag im ASL? Natürlich der Wandertag! Also geht wandern, schickt uns ein tolles Bild davon, und wenn ihr wollt gleich noch eure Route mit dazu!",
            9: "Heute wollen wir den Sonnenaufgang sehen! Und nach klassischer ASL-sitte lässt sich der natürlich am Besten fotografieren wenn man bis dahin wach geblieben ist!",
            10: "Für ein richtiges ASL-Feeling ist der Süßigkeitenkommunismus essentiell! Also kauft euch Süßigkeiten und teilt sie mit jemandem! (und sehen wollen wir das natürlich auch!)",
            11: "Heute sollt ihr Teebeutel jonglieren! Warum? - falsche Frage, ihr wollt wissen wie viele! Und darauf ist die Antwort: mindestens drei, für weitere gibts Bonuspunkte! (Den Beweis dürft ihr entweder als Foto oder als gif liefern :) )",
            12: "ASL-Feiertag!: Das ASL ist toll und das nächste ist nur noch 354 Tage von uns entfernt! Zeigt uns wie ihr euch auf das nächste ASL freut!",
            13: "Dem heutigen Challenge werden sich nur die mutigsten unter euch sich stellen! Kauft Sauerkrautsaft und trinkt ihn! (Natürlich brauchen wir für so eine Heldentat auch ein Beweisbild...)",
            14: "Um die letzte Nacht wie gewohnt durchmachen zu können sind Durchhaltevermögen und natürlich auch der klassische Kaffee oder Tee absolut unverzichtbar! Deswegen wollen wir heute ein Bild von eurem treuen Heißgetränk das euch wach hält!"
        }
        await ctx.send(challenges[dt.day])


def setup(bot):
    bot.add_cog(FunCog(bot))
