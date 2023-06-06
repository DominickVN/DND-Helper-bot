import random
from bot import bot



@bot.command()
async def roll(ctx, dice_expression):
    try:
        num_dice, num_sides = map(int, dice_expression.lower().split('d'))
        if num_dice <= 0 or num_sides <= 0:
            raise ValueError
        
        rolls = [random.randint(1,num_sides) for _ in range(num_dice)]
        total = sum(rolls)

        await ctx.send(f'`Rolling {dice_expression}: {", ".join(map(str, rolls))}\nTotal: {total}`')
    except ValueError:
        await ctx.send("Invalid dice expression. Please use the format XdY, where X is the number of dice and Y is the number of sides.")