import discord
import creds
from discord.ext import commands
from bot import bot

import diceCommands
import spellCommands
import conditionCommands
import pengunerdemoji
import helpfulCommands



intents = discord.Intents.default()  # Create an instance of the default intents
intents.members = True  # Enable the privileged members intent


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

bot.run(creds.TOKEN)
