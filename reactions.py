import discord
from discord.ext import commands
from bot import bot
import asyncio

intents = discord.Intents.default()
intents.reactions = True


@bot.command()
async def movie_time(ctx):
    message = await ctx.send("React with 🎦 to join Movie Time! @everyone")

    await message.add_reaction('🎦')

    def check(reaction, user):
        return str(reaction.emoji) == '🎦' and user != bot.user and reaction.message == message

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=None, check=check)

        role = discord.utils.get(ctx.guild.roles, name="Movie Time")

        if role:
            await user.add_roles(role)
        else:
            await ctx.send("The 'Movie Time' role was not found.")

        reaction, user = await bot.wait_for('reaction_remove', timeout=None, check=check)

        if role:
            await user.remove_roles(role)
        else:
            await ctx.send("The 'Movie Time' role was not found.")

    except asyncio.TimeoutError:
        await ctx.send("Movie Night sign-up has ended.")