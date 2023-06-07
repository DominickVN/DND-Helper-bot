from bot import bot
from cantrips_library import cantrips
from first_level_library import first_level_spells
from second_level_library import second_level_spells
from third_level_library import third_level_spells
from fourth_level_library import fourth_level_spells



@bot.command(aliases=['s'])
async def spell(ctx, *, spell_name):
    spell_name = spell_name.lower()  # Convert the spell name to lowercase for case-insensitive matching
    if spell_name in cantrips:
        spell_info = cantrips[spell_name]
    elif spell_name in first_level_spells:
        spell_info = first_level_spells[spell_name]
    elif spell_name in second_level_spells:
        spell_info = second_level_spells[spell_name]
    elif spell_name in third_level_spells:
        spell_info = third_level_spells[spell_name]
    elif spell_name in fourth_level_spells:
        spell_info = fourth_level_spells[spell_name]
    elif spell_name in fifth_level_spells:
        spell_info = fifth_level_spells[spell_name]
    else:
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

    await ctx.send(response)