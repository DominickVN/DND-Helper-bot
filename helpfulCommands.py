from bot import bot

@bot.command()
async def actions(ctx):
    await ctx.send("```At the beginning of your turn you get all of your available actions back. These include: \n\n• Action \n\n• Bonus Action \n\n• Reaction \n\nThese actions can be spent like currency; You can use each of them once per turn, and you do not need to use all of them.```")