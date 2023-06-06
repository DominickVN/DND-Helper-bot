import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", case_insensitive=False, intents = discord.Intents.all() )