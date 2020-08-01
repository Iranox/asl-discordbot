from discord.ext import commands
import discord

import logging


class BaseCog(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            logging.debug(str(member.name) + " connected")
            await member.create_dm()
            await member.dm_channel.send("Hi " + str(member.name) + ", welcome to the Stars!")
        except Exception as e:
            logging.error(str(e))
        try:
            channel = discord.utils.get(member.guild.channels, name='milkyway')
            await channel.send("Hello " + str(member.name) + ", welcome to the Galaxy!")
        except Exception as e:
            logging.error(str(e))

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(str(self.bot.user) + " is ready")


def setup(bot):
    bot.add_cog(BaseCog(bot))
