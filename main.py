import discord
from discord.ext import commands
from bot import bot

import diceCommands
import spellcommands
import conditionCommands
import pengunerdemoji



intents = discord.Intents.default()  # Create an instance of the default intents
intents.members = True  # Enable the privileged members intent

TOKEN = 'MTExNDM3OTMzMjQzODE5NjI3OA.Gd_Ha5.ZnP0-nNNndRyEUwL908EwdOkqx_gkdcBJIZaL8'


#commands for testing
@bot.command()
async def test(ctx):
    await ctx.send("`Bot is working!`")

@bot.command()
async def hello(ctx):
    await ctx.send("`Hello, I'm your Discord bot!`")

@bot.command()
async def greet(ctx, member: discord.Member):
    await ctx.send(f"`Hello, `{member.mention}`!`")
#commands for testing



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

bot.run(TOKEN)
