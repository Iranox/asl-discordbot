import random
from functools import reduce

from discord.ext import commands


def roll_dice(number_of_pipes: int, throws: int) -> [str]:
    return [random.randint(1, number_of_pipes) for _ in range(throws)]


def get_dices_result(number_of_pipes: int, throws: int) -> str:
    dice_throw_result = roll_dice(number_of_pipes, throws)
    dice_throw_result_str = ", ".join((str(i) for i in dice_throw_result))
    dice_throw_sum = reduce(lambda x, y: x + y, dice_throw_result)
    return f"Ergebnis: {dice_throw_result_str}\nSummer:{dice_throw_sum}"


class DiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dsa', help="Wirft 3 W20")
    async def dsa(self, ctx, ):
        await ctx.send(get_dices_result(20, 3))

    @commands.command(name='roll', help="Eingabebeispiel: 2w10")
    async def dice(self, ctx, dice:str):
        dice_values = dice.split("w")
        if len(dice_values) == 2:
            await ctx.send(get_dices_result(int(dice_values[1]), int(dice_values[0])))
        else:
            await ctx.send("Falsche Eingabe")


def setup(bot):
    bot.add_cog(DiceCog(bot))
