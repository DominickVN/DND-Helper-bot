import discord
from discord.ext import commands
from bot import bot
from libraries.actions_library import actions

@bot.command(aliases=['act'])
async def action(ctx, action_name):
    action_name = action_name.capitalize()
    if action_name in actions:
        action_info = actions[action_name]
        description = action_info["Description"]
        usage = action_info["Usage"]

        embed = discord.Embed(title=f"{action_name} Action", color=discord.Color.yellow())
        embed.add_field(name="Description", value=description, inline=False)
        embed.add_field(name="Usage", value=usage, inline=False)

        await ctx.send(embed=embed)
    else:
        await ctx.send("That action is not found in the library.")