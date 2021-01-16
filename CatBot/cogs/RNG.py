import random

import discord
from discord.ext import commands

client = discord.Client()


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def RNG(self, ctx, min, max):
        answer = random.randint(int(min), int(max))
        await ctx.send(answer)

    @commands.command()
    async def CoinFlip(self, ctx):
        answer = random.randint(1, 2)
        if answer == 1:
            answer = 'Heads'
        else:
            answer = 'Tails'
        await ctx.send(answer)


def setup(bot):
    bot.add_cog(Random(bot))
    print('Random.py Setup Complete')
