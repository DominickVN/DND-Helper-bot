import discord
from discord.ext import commands
from bot import bot


pengu_user_id = 554390186688118804

reaction_emoji = "🤓"


@bot.event
async def on_message(message):
    if message.author.id == pengu_user_id:
        await message.add_reaction(reaction_emoji)

    await bot.process_commands(message)