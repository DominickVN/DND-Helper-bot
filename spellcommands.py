from bot import bot
from cantrips_library import cantrips



@bot.command()
async def spell(ctx, *, spell_name):
    spell_name = spell_name.lower()  # Convert the spell name to lowercase for case-insensitive matching
    if spell_name in cantrips:
        spell_info = cantrips[spell_name]
        response = f"# {spell_name.capitalize()}\n\n" \
                f"```Level: {spell_info['level']}\n```" \
                f"```* Casting Time: {spell_info['casting_time']}\n```" \
                f"```* Range: {spell_info['range']}\n```" \
                f"```* Components: {spell_info['components']}\n```" \
                f"```* Material Components: {spell_info.get['material_components']}\n```" \
                f"```* Duration: {spell_info['duration']}\n```" \
                f"```* Concentration: {spell_info.get['concentration']}\n```" \
                f"```* Ritual: {spell_info.get['ritual']}\n```" \
                f"```* School: {spell_info['school']}\n```" \
                f"```\n{spell_info['description']}```"
    else:
        response = "Spell not found."

    await ctx.send(response)