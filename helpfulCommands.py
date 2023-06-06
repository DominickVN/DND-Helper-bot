from bot import bot

@bot.command()
async def actions(ctx):
    await ctx.send("```At the beginning of your turn you get all of your available actions back. These include: \n\n• Action \n\n• Bonus Action \n\n• Reaction \n\nThese actions can be spent like currency; You can use each of them once per turn, and you do not need to use all of them.```")

@bot.command(aliases=['c'])
async def commands(ctx):
    await ctx.send("```Here are some useful commands:\n\n•!roll: Allows you to roll dice! It can roll any number of dice with any number of sides, and add modifiers! Try !roll 2d6+3 \n     •For more dice commands, do !diceinfo\n\n•!spell: Allows you to look up the spell info for any spell. Try !spell Fire Bolt \n\n•!initiative: Starts an initative tracker that lets a DM keep track of turn order! \n     •Do !initiativeinfo for a runthrough of how to use the tracker.\n\n•Look up conditions quickly! Do !blinded for blinded, !charmed for charmed, etc.```")

@bot.command(aliases=['dc'])
async def diceinfo(ctx):
    await ctx.send("```Here are all of the dice commands:\n\n•!roll: Allows you to roll dice! It can roll any number of dice with any number of sides, and add modifiers! Try !roll 2d6+3\n\n•!rolla: Rolls 1d20 with Advantage! You can add modifiers if necessary; !rolla +5\n\n•!rolld: Rolls 1d20 with Disadvantage! You can add modifiers if necessary; !rolld -5\n\n\n•!wroll: Functions the same as !roll, but it will send the result to your DMs, perfect for dice rolling privacy.\n\n•!wrolla: Rolls 1d20 with Advantage, straight to your DMs! \n\n•!wrolld: Rolls 1d20 with Disadvantage, straight to your DMs!\n\n\n Aliases: !r, !ra, !rd, !wr, !wra, !wrd```")

@bot.command(aliases=['ii'])
async def initiativeinfo(ctx):
    await ctx.send("```Here is how to use the Initiative Tracker:\n\n•!initiative start: Starts the Initiative Tracker.\n\n•!initiative rolled (roll): Takes your initiative in place of (roll) and adds your name to the initiative order.\n\n•!initiative add (name) (roll): Used to add NPC's and Enemies to the turn order.\n\n•!initiative secretAdd (name) (roll): Creates a second initiative order, 'secret initiative'. Best used in a DM with the bot. When initiative tracking is over the 'secret initiative order' will be sent to the person who used secretAdd, and only that order will have the secret names.\n\n•!initiative end: Ends the initiative tracking and prints the turn order in the channel that end was called.\n\nAlias: !i```")
