import random
from bot import bot



@bot.command()
async def roll(ctx, dice_expression):
    try:
        parts = dice_expression.lower().split('+')  # Split the expression by '+'
        num_dice, num_sides = map(int, parts[0].split('d'))
        if num_dice <= 0 or num_sides <= 0:
            raise ValueError
        
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(rolls)

        if len(parts) > 1:
            modifiers = list(map(int, parts[1:]))  # Extract the modifiers as a list of integers
            total += sum(modifiers)  # Add the modifiers to the total

        await ctx.send(f'```Rolling {dice_expression}: {", ".join(map(str, rolls))}\nTotal: {total}```')
    except ValueError:
        await ctx.send("Invalid dice expression. Please use the format XdY[+Z], where X is the number of dice, Y is the number of sides, and Z is an optional modifier.")
