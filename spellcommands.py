import discord
from bot import bot

from libraries.cantrips_library import cantrips
from libraries.first_level_library import first_level_spells
from libraries.second_level_library import second_level_spells
from libraries.third_level_library import third_level_spells
from libraries.fourth_level_library import fourth_level_spells
from libraries.fifth_level_library import fifth_level_spells
from libraries.sixth_level_library import sixth_level_spells
from libraries.seventh_level_library import seventh_level_spells
from libraries.eighth_level_library import eighth_level_spells
from libraries.ninth_level_library import ninth_level_spells




@bot.command(aliases=['s'])
async def spell(ctx, *, spell_name):
    spell_name = spell_name.lower()  # Convert the spell name to lowercase for case-insensitive matching
    spell_info = None
    libraries = [cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells,
                fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells]
    for library in libraries:
        if spell_name in library:
            spell_info = library[spell_name]
            break

    if not spell_info:
        response = "Spell not found."
        await ctx.send(response)
        return

    # Capitalize the spell name
    spell_name = spell_name.title()

    # Create an embed
    embed = discord.Embed(title=spell_name, color=discord.Color.blue())
    embed.add_field(name="Level", value=f"{spell_info['level']}", inline=False)
    embed.add_field(name="Casting Time", value=f"{spell_info['casting_time']}", inline=False)
    embed.add_field(name="Range", value=f"{spell_info['range']}", inline=False)
    embed.add_field(name="Components", value=f"{spell_info['components']}", inline=False)
    embed.add_field(name="Duration", value=f"{spell_info['duration']}", inline=False)
    embed.add_field(name="Ritual", value=f"{spell_info.get('ritual', False)}", inline=False)
    embed.add_field(name="School", value=f"{spell_info['school']}", inline=False)
    
    # Split the description into new fields whenever there is a \n or \n\n
    description = spell_info['description']
    description_parts = description.split("\n\n")
    for i, part in enumerate(description_parts):
        embed.add_field(name=f"Description (Part {i+1})", value=f"```\n{part}```", inline=False)

    await ctx.send(embed=embed)

#most spells still work, a small few aren't perfectly formatted yet