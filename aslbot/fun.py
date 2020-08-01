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
        ]
        await ctx.send(old_school[random.randrange(0, len(old_school))])

    @commands.command(name='kill', help="Mörderspiel!!")
    async def kill(self, ctx):
        await ctx.send("https://i.kinja-img.com/gawker-media/image/upload/vodrkg3c4sr2d17gacwm.jpg")

    @commands.command(name='challenge', help="Was ist die heutige Challenge?")
    async def challenge(self, ctx):
        dt = datetime.datetime.today()
        chal = [
                "Sich auf das ASL freuen",
                "Sich auf das ASL freuen",
                "Sich auf das ASL freuen",
                "Finde einen Astro-Gegenstand und mache ein Foto davon!",
                "Irgendwo hinfahren zum Sterne gucken (Challenge bis zum Ende des ASLs)",
                "ASL-Trauertag (dem nicht-digital-Camp hinterhertrauern)",
                "Kalenderblatt zum Sammeln malen!",
                "Eine Rakete für das nächste ASL basteln (Challenge bis zum Endes des ASLs)"
            ]
        await ctx.send(chal[dt.day])


def setup(bot):
    bot.add_cog(FunCog(bot))
