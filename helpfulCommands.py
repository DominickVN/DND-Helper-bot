from bot import bot
import discord

@bot.command()
async def action_econ(ctx):
    embed = discord.Embed(title="Actions", color=discord.Color.yellow())
    embed.add_field(name="Description", value="At the beginning of your turn you get all of your available actions back. These include:", inline=False)
    embed.add_field(name="• Action", value="Perform an action. This can be Attack, Cast a Spell, Help, or anything else in the actions list.", inline=False)
    embed.add_field(name="• Bonus Action", value="Perform a bonus action. Bonus actions are shorter than Actions, and aren't used as often.", inline=False)
    embed.add_field(name="• Reaction", value="Take a reaction. Reactions are the least used action, as they can only be used on turns OTHER than your own.", inline=False)
    embed.add_field(name="Note", value="These actions can be spent like currency; you can use each of them once per turn, and you do not need to use all of them.", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands", color=discord.Color.yellow())
    embed.add_field(name="Description", value="Here are some useful commands:", inline=False)
    embed.add_field(name="• &roll", value="Allows you to roll dice! It can roll any number of dice with any number of sides, and add modifiers! Try `&roll 2d6+3`", inline=False)
    embed.add_field(name="• &spell", value="Allows you to look up the spell info for any spell. Try `&spell Fire Bolt`", inline=False)
    embed.add_field(name="• &initiative", value="Starts an initiative tracker that lets a DM keep track of turn order! Do `&initiativeinfo` for a runthrough of how to use the tracker.", inline=False)
    embed.add_field(name="• &condition", value="Look up any condition with this command. Try `&condition blinded`!", inline=False)
    embed.add_field(name="• &NPC", value="Generate an NPC statblock quickly! Try `&NPC generate`", inline=False)
    embed.add_field(name="• &monster", value="Search for a Monster's statblock using this command! Try `&monster (monster)` to search for a specific name, or try `&monster (type)` and `&monster (challenge rating #)` to get a list of monsters that fit into that category!", inline=False)
    await ctx.send(embed=embed)


@bot.command(aliases=['dc'])
async def diceinfo(ctx):
    embed = discord.Embed(title="Dice Commands", color=discord.Color.yellow())
    embed.add_field(name="Description", value="Here are all of the dice commands:", inline=False)
    embed.add_field(name="• &roll", value="Allows you to roll dice! It can roll any number of dice with any number of sides, and add modifiers! Try `&roll 2d6+3`", inline=False)
    embed.add_field(name="• &rolla", value="Rolls 1d20 with Advantage! You can add modifiers if necessary; `&rolla +5`", inline=False)
    embed.add_field(name="• &rolld", value="Rolls 1d20 with Disadvantage! You can add modifiers if necessary; `&rolld -5`", inline=False)
    embed.add_field(name="• &wroll", value="Functions the same as &roll, but it will send the result to your DMs, perfect for dice rolling privacy.", inline=False)
    embed.add_field(name="• &wrolla", value="Rolls 1d20 with Advantage, straight to your DMs!", inline=False)
    embed.add_field(name="• &wrolld", value="Rolls 1d20 with Disadvantage, straight to your DMs!", inline=False)
    embed.set_footer(text="Aliases: &r, &ra, &rd, &wr, &wra, &wrd")
    await ctx.send(embed=embed)


@bot.command(aliases=['ii'])
async def initiativeinfo(ctx):
    embed = discord.Embed(title="Initiative Tracker", color=discord.Color.yellow())
    embed.add_field(name="Description", value="Here is how to use the Initiative Tracker:", inline=False)
    embed.add_field(name="• &initiative start", value="Starts the Initiative Tracker.", inline=False)
    embed.add_field(name="• &initiative rolled (roll)", value="Takes your initiative in place of (roll) and adds your name to the initiative order.", inline=False)
    embed.add_field(name="• &initiative add (name) (roll)", value="Used to add NPCs and enemies to the turn order.", inline=False)
    embed.add_field(name="• &initiative secretAdd (name) (roll)", value="Creates a second initiative order, 'secret initiative'. Best used in a DM with the bot. When initiative tracking is over, the 'secret initiative order' will be sent to the person who used secretAdd, and only that order will have the secret names.", inline=False)
    embed.add_field(name="• &initiative end", value="Ends the initiative tracking and prints the turn order in the channel that end was called.", inline=False)
    embed.add_field(name="• &initiative edit", value="Reopens the initiative order so new names can be added.", inline=False)
    embed.add_field(name="• &initiative remove (name or #)", value="Removes a name from the initiative order.", inline=False)
    embed.set_footer(text="Alias: &i")
    await ctx.send(embed=embed)
