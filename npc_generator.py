import random
from bot import bot

npc_races = {
    'human': {
        'names': ['John', 'Mary', 'Robert', 'Emma', 'William', 'Olivia']
    },
    'elf': {
        'names': ['Lithian', 'Elysia', 'Thranduil', 'Elara', 'Galadriel', 'Aranion']
    },
    'dwarf': {
        'names': ['Thorin', 'Gimli', 'Faldor', 'Hilda', 'Durgan', 'Balin']
    },
    'halfling': {
        'names': ['Pippin', 'Merry', 'Samwise', 'Rosie', 'Frodo', 'Lily']
    },
    'orc': {
        'names': ['Grommash', 'Durotan', 'Gul\'dan', 'Garrosh', 'Zugzug', 'Thrall']
    }
}

@bot.command()
async def npc(ctx, action=None, race=None, gender=None):
    if action == 'generate':
        if race and race.lower() in npc_races:
            race = race.lower()
        else:
            race = 'human'

        if gender:
            gender = gender.lower()
            if gender not in ['male', 'female']:
                await ctx.send('Invalid gender. Please specify "male" or "female" or leave it blank for a random gender.')
                return

        name = generate_name(race, gender)
        age = random.randint(18, 60)
        ability_scores = generate_ability_scores()

        npc_info = f"Name: {name}\nAge: {age}\nRace: {race.title()}"
        if gender:
            npc_info += f"\nGender: {gender.capitalize()}"
        npc_info += f"\nAbility Scores: {ability_scores}"

        await ctx.send(f"Generated NPC:\n```{npc_info}```")

def generate_name(race, gender):
    if race in npc_races:
        if gender == 'male':
            names = npc_races[race]['names'][:3]
        elif gender == 'female':
            names = npc_races[race]['names'][3:]
        else:
            names = npc_races[race]['names']
    else:
        names = npc_races['human']['names']

    return random.choice(names)

def generate_ability_scores():
    scores = [random.randint(8, 12) for _ in range(6)]
    return ', '.join(map(str, scores))
