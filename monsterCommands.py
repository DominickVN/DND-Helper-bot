import discord
from bot import bot
from dictionaries.MonsterLibraries.CR0_monsters_library import cr_0_monsters
from dictionaries.MonsterLibraries.CRp125_monsters_library import cr_p125_monsters
from dictionaries.MonsterLibraries.CRp25_monsters_library import cr_p25_monsters
from dictionaries.MonsterLibraries.CRp5_monsters_library import cr_p5_monsters
from dictionaries.MonsterLibraries.CR1_monsters_library import cr_1_monsters
from dictionaries.MonsterLibraries.CR2_monsters_library import cr_2_monsters
from dictionaries.MonsterLibraries.CR3_monsters_library import cr_3_monsters
from dictionaries.MonsterLibraries.CR4_monsters_library import cr_4_monsters
from dictionaries.MonsterLibraries.CR5_monsters_library import cr_5_monsters
from dictionaries.MonsterLibraries.CR6_monsters_library import cr_6_monsters
from dictionaries.MonsterLibraries.CR7_monsters_library import cr_7_monsters
from dictionaries.MonsterLibraries.CR8_monsters_library import cr_8_monsters
from dictionaries.MonsterLibraries.CR9_monsters_library import cr_9_monsters
from dictionaries.MonsterLibraries.CR10_monsters_library import cr_10_monsters
from dictionaries.MonsterLibraries.CR11_monsters_library import cr_11_monsters
from dictionaries.MonsterLibraries.CR12_monsters_library import cr_12_monsters
from dictionaries.MonsterLibraries.CR13_monsters_library import cr_13_monsters
from dictionaries.MonsterLibraries.CR14_monsters_library import cr_14_monsters
from dictionaries.MonsterLibraries.CR15_monsters_library import cr_15_monsters
from dictionaries.MonsterLibraries.CR16_monsters_library import cr_16_monsters
from dictionaries.MonsterLibraries.CR17_monsters_library import cr_17_monsters
from dictionaries.MonsterLibraries.CR19_monsters_library import cr_19_monsters
from dictionaries.MonsterLibraries.CR20_monsters_library import cr_20_monsters
from dictionaries.MonsterLibraries.CR21_monsters_library import cr_21_monsters
from dictionaries.MonsterLibraries.CR22_monsters_library import cr_22_monsters
from dictionaries.MonsterLibraries.CR23_monsters_library import cr_23_monsters
from dictionaries.MonsterLibraries.CR24_monsters_library import cr_24_monsters
from dictionaries.MonsterLibraries.CR30_monsters_library import cr_30_monsters



@bot.command(aliases=("m", "mon"))
async def monster(ctx, *, query):
    if is_dungeon_master(ctx.author):
        libraries = [cr_0_monsters, cr_p125_monsters, cr_p25_monsters, cr_p5_monsters, cr_1_monsters, cr_2_monsters, cr_3_monsters, cr_4_monsters, cr_5_monsters, cr_6_monsters, cr_7_monsters, cr_8_monsters, cr_9_monsters, cr_10_monsters, cr_11_monsters, cr_12_monsters, cr_13_monsters, cr_14_monsters, cr_15_monsters, cr_16_monsters, cr_17_monsters, cr_19_monsters, cr_20_monsters, cr_21_monsters, cr_22_monsters, cr_23_monsters, cr_24_monsters, cr_30_monsters]
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
    embed = discord.Embed(title=name, color=discord.Color.teal())
    embed.add_field(name="Hit Points", value=monster["hit_points"], inline=True)
    embed.add_field(name="Armor Class", value=monster["armor_class"], inline=True)
    embed.add_field(name="Speed", value=monster["speed"], inline=True)
    embed.add_field(name="Size", value=monster["size"], inline=True)
    embed.add_field(name="Type", value=monster["type"], inline=True)
    embed.add_field(name="Challenge", value=monster["challenge"], inline=True)

    abilities = monster.get("abilities")
    if abilities:
        ability_list = list(abilities.items())
        half_length = (len(ability_list) + 1) // 2
        for i, (ability, value) in enumerate(ability_list):
            if i < half_length:
                column_name = "Abilities"
            else:
                column_name = "Abilities (Column 2)"
            modifier = (value - 10) // 2  # Calculate ability score modifier
            modifier_str = f"+{modifier}" if modifier > 0 else str(modifier)
            embed.add_field(name=column_name if i == 0 else "\u200B", value=f"{ability}: {value} ({modifier_str})", inline=True)

    saving_throws = monster.get("saving_throws")
    if saving_throws:
        saving_throws_string = "\n".join(f"{save}: {value}" for save, value in saving_throws.items())
        embed.add_field(name="Saving Throws", value=saving_throws_string[:1024], inline=False)

    damage_immunities = monster.get("damage_immunities")
    if damage_immunities:
        embed.add_field(name="Damage Immunities", value=damage_immunities[:1024], inline=False)

    condition_immunities = monster.get("condition_immunities")
    if condition_immunities:
        embed.add_field(name="Condition Immunities", value=condition_immunities[:1024], inline=False)

    senses = monster.get("senses")
    if senses:
        embed.add_field(name="Senses", value=senses[:1024], inline=False)

    languages = monster.get("languages")
    if languages:
        embed.add_field(name="Languages", value=languages[:1024], inline=False)

    special_traits = monster.get("special_traits")
    if special_traits:
        traits_string = ""
        for trait, description in special_traits.items():
            if isinstance(description, dict):
                action_string = ""
                for key, value in description.items():
                    action_string += f"**{key}**: {value}\n"
                traits_string += f"**{trait}**\n{action_string}\n"
            else:
                traits_string += f"**{trait}**: {description}\n"
            traits_string += "\n"
        traits_chunks = split_string_into_chunks(traits_string, 1024)
        for i, chunk in enumerate(traits_chunks):
            embed.add_field(name=" " if i > 0 else "Special Traits", value=chunk, inline=False)

    actions = monster.get("actions")
    if actions:
        actions_string = ""
        for action, description in actions.items():
            if isinstance(description, dict):
                action_string = ""
                for key, value in description.items():
                    action_string += f"**{key}**: {value}\n"
                actions_string += f"**{action}**\n{action_string}\n"
            else:
                actions_string += f"**{action}**: {description}\n"
            actions_string += "\n"
        actions_chunks = split_string_into_chunks(actions_string, 1024)
        for i, chunk in enumerate(actions_chunks):
            embed.add_field(name=" " if i > 0 else "Actions", value=chunk, inline=False)

    return embed



def split_string_into_chunks(text, chunk_size):
    chunks = []
    current_chunk = ""
    lines = text.split("\n")
    for line in lines:
        if len(current_chunk) + len(line) < chunk_size:
            current_chunk += f"{line}\n"
        else:
            chunks.append(current_chunk)
            current_chunk = f"{line}\n"
    if current_chunk:
        chunks.append(current_chunk)
    return chunks


#chatGPT generated the dictionaries, so a lot of them don't work perfectly yet. WIP