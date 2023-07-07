import discord
from discord.ext import commands
import sqlite3
from bot import bot

# Connect to the SQLite database
conn = sqlite3.connect("character_sheets.db")
c = conn.cursor()

# Create the characters table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS characters
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id TEXT,
              name TEXT,
              class TEXT,
              race TEXT,
              strength INTEGER,
              dexterity INTEGER,
              constitution INTEGER,
              intelligence INTEGER,
              wisdom INTEGER,
              charisma INTEGER)''')
conn.commit()

@bot.command(aliases=['cc'])
async def create_character(ctx):
    questions = [
        "What is your character's name?",
        "What is your character's class?",
        "What is your character's race?",
        "What is your character's Strength score?",
        "What is your character's Dexterity score?",
        "What is your character's Constitution score?",
        "What is your character's Intelligence score?",
        "What is your character's Wisdom score?",
        "What is your character's Charisma score?"
    ]
    answers = []

    def check_author(message):
        return message.author == ctx.author and message.channel == ctx.channel

    def get_next_question():
        if len(answers) >= len(questions):
            return None
        else:
            return questions[len(answers)]

    def insert_character_into_db():
        sql = '''INSERT INTO characters (user_id, name, class, race, strength, dexterity, constitution, intelligence, wisdom, charisma)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        user_id = str(ctx.author.id)
        c.execute(sql, (user_id,) + tuple(answers))
        conn.commit()

    def create_embed(question):
        current_question = len(answers) + 1
        total_questions = len(questions)
        embed = discord.Embed(title=f"Question {current_question}/{total_questions}", description=question)
        return embed

    def parse_score(score):
        try:
            score = int(score)
            if score < 1 or score > 20:
                return None
            else:
                return score
        except ValueError:
            return None

    async def ask_question(question):
        embed = create_embed(question)
        dm_channel = await ctx.author.create_dm()
        await dm_channel.send(embed=embed)
        response = await bot.wait_for('message', check=check_author)
        return response.content

    for question in questions:
        answer = await ask_question(question)
        answers.append(answer)

        if len(answers) == 9:
            # Convert score inputs to integers
            for i in range(3, 9):
                score = parse_score(answers[i])
                if score is None:
                    await ctx.send("Invalid score input. Scores must be integers between 1 and 20.")
                    return
                answers[i] = score

            # Insert character into the database
            insert_character_into_db()

            await ctx.send("Character creation complete! Character information has been stored in the database.")
            return

    conn.close()



@bot.command(aliases=['cs'])
async def character_sheet(ctx):
    user_id = str(ctx.author.id)

    # Connect to the SQLite database
    conn = sqlite3.connect("character_sheets.db")
    c = conn.cursor()

    # Retrieve the character from the database based on the user_id
    c.execute("SELECT * FROM characters WHERE user_id=?", (user_id,))
    character = c.fetchone()

    if not character:
        await ctx.send("No character found. use `&create_character` to make one!")
        conn.close()
        return

    # Extract the character information from the database
    _, _, name, char_class, race, strength, dexterity, constitution, intelligence, wisdom, charisma = character

    # Create the character sheet embed
    embed = discord.Embed(title=name)
    embed.add_field(name="Race", value=race, inline=False)
    embed.add_field(name="Class", value=char_class, inline=False)
    embed.add_field(name="Ability Scores", value=f"Strength: {strength}\nDexterity: {dexterity}\nConstitution: {constitution}\nIntelligence: {intelligence}\nWisdom: {wisdom}\nCharisma: {charisma}", inline=False)

    await ctx.send(embed=embed)

    conn.close()