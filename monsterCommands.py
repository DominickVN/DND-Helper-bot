import discord
from discord.ext import commands
from bot import bot
from libraries.MonsterLibraries.CR0_monsters_library import cr_0_monsters
from libraries.MonsterLibraries.CRp125_monsters_library import cr_p125_monsters


@bot.command(aliases=("m", "mon"))
async def monster(ctx, *, query):
    if is_dungeon_master(ctx.author):
        libraries = [cr_0_monsters, cr_p125_monsters]
        matching_monsters = []
        for library in libraries:
            for name, monster in library.items():
                if query.lower() == name.lower():
                    await ctx.send(embed=create_monster_embed(name, monster))
                    return
                elif query.lower().startswith("cr ") and query[3:].lower() == monster["challenge"].lower():
                    matching_monsters.append(name)

        if matching_monsters:
            monsters_list = "\n- ".join(matching_monsters)
            await ctx.send(f"Found the following monsters matching your query:\n- {monsters_list}")
        else:
            await ctx.send("No monsters found matching your query.")
    else:
        await ctx.send("You're trying to metagame! Only Dungeon Masters can access the monster details.")

def is_dungeon_master(author):
    role_names = [role.name for role in author.roles]
    return "Dungeon Master" in role_names

def create_monster_embed(name, monster):
    embed = discord.Embed(title=name)
    embed.add_field(name="Hit Points", value=monster["hit_points"], inline=True)
    embed.add_field(name="Armor Class", value=monster["armor_class"], inline=True)
    embed.add_field(name="Speed", value=monster["speed"], inline=True)
    embed.add_field(name="Size", value=monster["size"], inline=True)
    embed.add_field(name="Type", value=monster["type"], inline=True)
    embed.add_field(name="Challenge", value=monster["challenge"], inline=True)

    abilities = monster.get("abilities")
    if abilities:
        embed.add_field(name="Abilities", value=abilities, inline=False)

    actions = monster.get("actions")
    if actions:
        for action, description in actions.items():
            embed.add_field(name=action, value=description, inline=False)

    return embed

