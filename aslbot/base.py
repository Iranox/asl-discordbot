from discord.ext import commands
import discord

import logging


class BaseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            logging.info("Role: get")
            role_to_set = discord.utils.get(member.guild.roles(), name="Zwergplanet")
            logging.info("Role: got")
            logging.info("Role: " + str(role_to_set))
            await member.add_roles(role_to_set)
        except Exception as e:
            logging.error(str(e))

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(str(self.bot.user) + " is ready")


def setup(bot):
    bot.add_cog(BaseCog(bot))
