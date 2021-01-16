import os

import discord
from discord.ext import commands


client = commands.Bot(command_prefix = "-cb ", case_insensitive=True)
print('CatBotCore 1.1-alpha Development Version')

for module in os.listdir('./cogs'):
    if module.endswith('.py'):
        print("loading " + module + "...")
        client.load_extension(f'cogs.{module[:-3]}')
        

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('CatBotCore 1.1-alpha Development Version Testing'))

client.run('Bot_Token')
