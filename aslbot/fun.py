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

    @commands.command(name='hootsforce', help="a music video with submarines fighting an evil wizard... in space")
    async def space_metal(self, ctx):
        await ctx.send("https://gph.is/VxbsSv")

    @commands.command(name='headache', help="...")
    async def star_trek_headache(self, ctx):
        await ctx.send("https://giphy.com/gifs/6OWIl75ibpuFO")

    @commands.command(name='facepalm', help=":person_facepalming: ")
    async def star_trek_facepalm(self, ctx):
        await ctx.send("https://gph.is/2nBvKOZ")

    @commands.command(name='pika', help="pikaCHUUUUUUUUUU")
    async def star_trek_facepalm(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=AjSuZgNgMZc")


def setup(bot):
    bot.add_cog(FunCog(bot))
