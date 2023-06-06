from bot import bot


@bot.command()
async def blinded(ctx):
    await ctx.send("```A blinded creature can\'t see and automatically fails any ability check that requires sight. \nAttack rolls against the creature have advantage, and the creature\'s attack rolls have disadvantage.```")

@bot.command()
async def charmed(ctx):
    await ctx.send("```-A charmed creature can\'t attack the charmer or target the charmer with harmful abilities or magical effects. \n-The charmer has advantage on any ability check to interact socially with the creature.```")

@bot.command()
async def deafened(ctx):
    await ctx.send("```-A deafened creature can\'t hear and automatically fails any ability check that requires hearing.```")

@bot.command()
async def frightened(ctx):
    await ctx.send("```-A frightened creature has disadvantage on ability checks and attack rolls while the source of its fear is within line of sight. \n-The creature can\'t willingly move closer to the source of its fear.```")

@bot.command()
async def grappled(ctx):
    await ctx.send("```-A grappled creature\'s speed becomes 0, and it can\'t benefit from any bonus to its speed. \n-The condition ends if the grappler is incapacitated (see the condition).\n The condition also ends if an effect removes the grappled creature from the reach of the grappler or grappling effect, such as when a creature is hurled away by the thunderwave spell.```")

@bot.command()
async def incapacitated(ctx):
    await ctx.send("```-An incapacitated creature can\'t take actions or reactions.```")

@bot.command()
async def invisible(ctx):
    await ctx.send("```-An invisible creature is impossible to see without the aid of magic or a special sense. For the purpose of hiding, the creature is heavily obscured. The creature\'s location can be detected by any noise it makes or any tracks it leaves. \n-Attack rolls against the creature have disadvantage, and the creature\'s attack rolls have advantage.```")

@bot.command()
async def paralyzed(ctx):
    await ctx.send("```-A paralyzed creature is incapacitated (see the condition) and can\'t move or speak.\n-The creature automatically fails Strength and Dexterity saving throws.\n-Attack rolls against the creature have advantage. \n-Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.```")

@bot.command()
async def petrified(ctx):
    await ctx.send("```-A petrified creature is transformed, along with any nonmagical object it is wearing or carrying, into a solid inanimate substance (usually stone). Its weight increases by a factor of ten, and it ceases aging. \n-The creature is incapacitated (see the condition), can\'t move or speak, and is unaware of its surroundings. \n-Attack rolls against the creature have advantage. \n-he creature automatically fails Strength and Dexterity saving throws. \n-The creature has resistance to all damage. \n-The creature is immune to poison and disease, although a poison or disease already in its system is suspended, not neutralized.```")

@bot.command()
async def poisoned(ctx):
    await ctx.send("```-A poisoned creature has disadvantage on attack rolls and ability checks.```")

@bot.command()
async def prone(ctx):
    await ctx.send("```-A prone creature\'s only movement option is to crawl, unless it stands up and thereby ends the condition. \n-The creature has disadvantage on attack rolls. \n-An attack roll against the creature has advantage if the attacker is within 5 feet of the creature. Otherwise, the attack roll has disadvantage.```")

@bot.command()
async def restrained(ctx):
    await ctx.send("```-A restrained creature\'s speed becomes 0, and it can\'t benefit from any bonus to its speed. \n-Attack rolls against the creature have advantage, and the creature\'s attack rolls have disadvantage. \n-The creature has disadvantage on Dexterity saving throws.```")

@bot.command()
async def stunned(ctx):
    await ctx.send("```-A stunned creature is incapacitated (see the condition), can\'t move, and can speak only falteringly. \n-The creature automatically fails Strength and Dexterity saving throws. \n-Attack rolls against the creature have advantage.```")

@bot.command()
async def unconscious(ctx):
    await ctx.send("```-An unconscious creature is incapacitated (see the condition), can\'t move or speak, and is unaware of its surroundings \n-The creature drops whatever it\'s holding and falls prone. \n-The creature automatically fails Strength and Dexterity saving throws. \n-The creature automatically fails Strength and Dexterity saving throws. \n-Attack rolls against the creature have advantage. \n-Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.```")

@bot.command()
async def exhaustion(ctx):
    await ctx.send("```-Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect\'s description. \n \n  Exhaustion Effects: \n 1: Disadvantage on ability checks \n 2: Speed halved \n 3: Disadvantage on attack rolls and saving throws \n 4: Hit point maximum halved \n 5: Speed reduced to 0 \n 6: Death \n \n-If an already exhausted creature suffers another effect that causes exhaustion, its current level of exhaustion increases by the amount specified in the effect\'s description. \n-A creature suffers the effect of its current level of exhaustion as well as all lower levels. For example, a creature suffering level 2 exhaustion has its speed halved and has disadvantage on ability checks. \n-An effect that removes exhaustion reduces its level as specified in the effect\'s description, with all exhaustion effects ending if a creature\'s exhaustion level is reduced below 1. \n-Finishing a long rest reduces a creature\'s exhaustion level by 1, provided that the creature has also ingested some food and drink.```")