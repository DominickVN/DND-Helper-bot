from bot import bot
from libraries.conditions_library import conditions
import discord

@bot.command(aliases=['con'])
async def condition(ctx, *, condition_name):
    condition_name = condition_name.lower()
    condition_info = conditions.get(condition_name)

    if not condition_info:
        response = "Condition not found."
        await ctx.send(response)
        return
    
    condition_name = condition_name.title()

    embed = discord.Embed(title=condition_name, description=condition_info['description'], color=discord.Color.blue())
    await ctx.send(embed=embed)