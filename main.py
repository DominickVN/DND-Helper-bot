import discord
import creds
from discord.ext import commands
from bot import bot

import diceCommands
import spellCommands
import conditionCommands
import pengunerdemoji
import helpfulCommands
import calculator
import initiative_tracker
import npc_generator
# import classCommands



intents = discord.Intents.default()
intents.members = True


#commands for testing
@bot.command()
async def test(ctx):
    await ctx.send("`Bot is working!`")
#commands for testing



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

bot.run(creds.TOKEN)
