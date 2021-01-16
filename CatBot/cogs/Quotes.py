import random

import discord
from discord.ext import commands

client = discord.Client()


class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #don't forget ()
    @commands.command()
    async def quote(self, ctx, Qnum='none'):

            if Qnum == 'none':
                f = open(
                    r'C:\Users\Catst\Desktop\Coding\Code\Python\CatBotCore2\cogs\data\quotes.txt')
                random_lines = random.choice(f.readlines())
                await ctx.send(random_lines)
                f.close()

            else:
                with open(r'C:\Users\Catst\Desktop\Coding\Code\Python\CatBotCore2\cogs\data\quotes.txt') as f:
                    read = f.read()
                    array = read.split('\n')

                    if int(Qnum) > len(array):
                        quote = "IndexError: list index out of range ¯\_(ツ)_/¯ (that means choose another number dummy)"
                    else:
                        quote = array[int(Qnum)-1]
                        
                await ctx.send(quote)

def setup(bot):
    bot.add_cog(Quotes(bot))
    print('Quotes.py Setup Complete')
