import random

import discord
from discord.ext import commands

client = discord.Client()


class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open(r"cogs\data\quotes.txt") as f:
            self.quote = f.read()
        self.array = self.quote.splitlines()

    #don't forget ()
    @commands.command()
    async def quote(self, ctx, Qnum='none'):

            if Qnum == 'none':
                random_lines = random.choice(self.array)
                await ctx.send(random_lines)
            else:
                    if int(Qnum) > len(self.array):
                        quote = "IndexError: list index out of range ¯\_(ツ)_/¯ (that means choose another number dummy)"
                    else:
                        quote = self.array[int(Qnum)-1]
                        
            await ctx.send(quote)



def setup(bot):
    bot.add_cog(Quotes(bot))
    print('Quotes.py Setup Complete')
