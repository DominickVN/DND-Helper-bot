import discord
from bot import bot
from cantrips_library import cantrips
from first_level_library import first_level_spells
from second_level_library import second_level_spells
from third_level_library import third_level_spells
from fourth_level_library import fourth_level_spells
from fifth_level_library import fifth_level_spells
from sixth_level_library import sixth_level_spells
from seventh_level_library import seventh_level_spells
from eighth_level_library import eighth_level_spells
from ninth_level_library import ninth_level_spells



@bot.command(aliases=['s'])
async def spell(ctx, *, spell_name):
    spell_name = spell_name.lower()  # Convert the spell name to lowercase for case-insensitive matching
    spell_info = None
    libraries = [cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells,fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells]
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

    response = f"# {spell_name}\n\n" \
               f"```Level: {spell_info['level']}\n```" \
               f"```* Casting Time: {spell_info['casting_time']}\n```" \
               f"```* Range: {spell_info['range']}\n```" \
               f"```* Components: {spell_info['components']}\n```" \
               f"```* Duration: {spell_info['duration']}\n```" \
               f"```* Ritual: {spell_info.get('ritual', False)}\n```" \
               f"```* School: {spell_info['school']}\n```" \
               f"```\n{spell_info['description']}```"

    # Split the response if it exceeds the Discord API character limit
    if len(response) > 2000:
        response_parts = [response[i:i + 2000] for i in range(0, len(response), 2000)]
        for i, part in enumerate(response_parts):
            part = f"{part} (Part {i+1}/{len(response_parts)})"
            await ctx.send(part)
    else:
        await ctx.send(response)




@bot.command()
async def search_spell_by_title(ctx, title):
    spell = None
    for library in [cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells, fifth_level_spells, sixth_level_spells, seventh_level_spells]:
        if title.lower() in library:
            spell = library[title.lower()]
            break

    if spell:
        embed = discord.Embed(title=title.capitalize(), description=spell['description'], color=0x00ff00)
        embed.add_field(name="Level", value=str(spell['level']), inline=True)
        embed.add_field(name="Casting Time", value=spell['casting_time'], inline=True)
        embed.add_field(name="Range", value=spell['range'], inline=True)
        embed.add_field(name="Components", value=spell['components'], inline=True)
        embed.add_field(name="Duration", value=spell['duration'], inline=True)
        embed.add_field(name="School", value=spell['school'], inline=True)
        embed.add_field(name="Concentration", value=str(spell['concentration']), inline=True)
        embed.add_field(name="Ritual", value=str(spell['ritual']), inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Spell not found.")
