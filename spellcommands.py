import discord
from bot import bot

from dictionaries.SpellLibraries.cantrips_library import cantrips
from dictionaries.SpellLibraries.first_level_library import first_level_spells
from dictionaries.SpellLibraries.second_level_library import second_level_spells
from dictionaries.SpellLibraries.third_level_library import third_level_spells
from dictionaries.SpellLibraries.fourth_level_library import fourth_level_spells
from dictionaries.SpellLibraries.fifth_level_library import fifth_level_spells
from dictionaries.SpellLibraries.sixth_level_library import sixth_level_spells
from dictionaries.SpellLibraries.seventh_level_library import seventh_level_spells
from dictionaries.SpellLibraries.eighth_level_library import eighth_level_spells
from dictionaries.SpellLibraries.ninth_level_library import ninth_level_spells




@bot.command(aliases=['s'])
async def spell(ctx, *, spell_name):
    spell_name = spell_name.lower()
    spell_info = None
    dictionaries = [cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells,
                fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells]
    for dictionary in dictionaries:
        if spell_name in dictionary:
            spell_info = dictionary[spell_name]
            break
    if not spell_info:
        response = "Spell not found."
        await ctx.send(response)
        return
    
    spell_name = spell_name.title()
    embed = discord.Embed(color=discord.Color.blue())
    embed.title = spell_name
    embed.add_field(name="Level", value=f"{spell_info['level']}", inline=True)
    embed.add_field(name="Casting Time", value=f"{spell_info['casting_time']}", inline=True)
    embed.add_field(name="Range", value=f"{spell_info['range']}", inline=True)
    embed.add_field(name="Components", value=f"{spell_info['components']}", inline=False)
    embed.add_field(name="Duration", value=f"{spell_info['duration']}", inline=True)
    embed.add_field(name="Ritual", value=f"{spell_info.get('ritual', False)}", inline=True)
    embed.add_field(name="School", value=f"{spell_info['school']}", inline=True)
    
    # Splits the description into new fields whenever there is a \n or \n\n, this is to get around character limits
    description = spell_info['description']
    description_parts = description.split("\n\n")
    for i, part in enumerate(description_parts):
        if len(part) > 1024:
            response = "The description for this spell is too long to display in a single message. Currently working on a way around this."
            await ctx.send(response)
            return
        embed.add_field(name=f" ", value=f"```\n{part}```", inline=False)

    await ctx.send(f"# {spell_name}")
    await ctx.send(embed=embed)

#most spells still work, a small few aren't perfectly formatted yet
#Discord Messages and Embeds have a character limit, and some spells have way too many characters