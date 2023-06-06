import random
from bot import bot



#d20
@bot.command()
async def roll(ctx):
    number = random.randint(1,20)
    await ctx.send(f"`You rolled a {number}!`")

#d6
@bot.command()
async def rd6(ctx):
    number = random.randint(1,6)
    await ctx.send(f"`You rolled a {number}!`")

#d8
@bot.command()
async def rd8(ctx):
    number = random.randint(1,8)
    await ctx.send(f"`You rolled a {number}!`")

#d10
@bot.command()
async def rd10(ctx):
    number = random.randint(1,10)
    await ctx.send(f"`You rolled a {number}!`")

#d12
@bot.command()
async def rd12(ctx):
    number = random.randint(1,12)
    await ctx.send(f"`You rolled a {number}!`")

#d100
@bot.command()
async def rd100(ctx):
    number = random.randint(1,100)
    await ctx.send(f"`You rolled a {number}!`")