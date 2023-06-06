import random
from bot import bot


@bot.command()
async def roll(ctx, dice_expression='1d20'):
    try:
        # Split the dice expression into dice and modifier (if present)
        parts = dice_expression.split('+')
        dice_part = parts[0]
        modifier_part = parts[1] if len(parts) > 1 else '0'

        # Parse the dice expression
        num_dice, num_sides = map(int, dice_part.lower().split('d'))
        modifier = int(modifier_part)

        if num_dice <= 0 or num_sides <= 0:
            raise ValueError

        # Roll the dice
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(rolls) + modifier

        await ctx.send(f'```Rolling {dice_expression}: {", ".join(map(str, rolls))}\nTotal: {total}```')

    except (ValueError, IndexError):
        await ctx.send('Invalid dice expression. Please use the format XdY[+Z], where X is the number of dice, Y is the number of sides, and Z is an optional modifier.')

@bot.command()
async def rolla(ctx, modifier='',):
    try:
        # Roll with advantage (2d20) and calculate the total
        rolls = [random.randint(1, 20) for _ in range(2)]
        total = max(rolls)

        # Apply the modifier if provided
        if modifier:
            total += int(modifier)

        await ctx.send(f'```Rolling with Advantage: {", ".join(map(str, rolls))}\nTotal: {total}```')

    except ValueError:
        await ctx.send('Invalid modifier. Please provide a valid number for the modifier.')

@bot.command()
async def rolld(ctx, modifier=''):
    try:
        # Roll with disadvantage (2d20) and calculate the total
        rolls = [random.randint(1, 20) for _ in range(2)]
        total = min(rolls)

        # Apply the modifier if provided
        if modifier:
            total += int(modifier)

        await ctx.send(f'```Rolling with Disadvantage: {", ".join(map(str, rolls))}\nTotal: {total}```')

    except ValueError:
        await ctx.send('Invalid modifier. Please provide a valid number for the modifier.')


@bot.command()
async def wroll(ctx, dice_expression=''):
    try:
        # Parse the dice expression
        parts = dice_expression.lower().split('+')
        num_dice, num_sides = map(int, parts[0].split('d'))

        # Roll the dice and calculate the total
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(rolls)

        # Apply modifiers if provided
        if len(parts) > 1:
            modifiers = list(map(int, parts[1:]))
            total += sum(modifiers)

        # Send the roll result as a DM to the sender
        dm_channel = await ctx.author.create_dm()
        await dm_channel.send(f'```Rolling {dice_expression}: {", ".join(map(str, rolls))}\nTotal: {total}```')

    except (ValueError, IndexError):
        await ctx.send(
            "Invalid dice expression. Please use the format XdY[+Z], where X is the number of dice, Y is the number of sides, and Z is an optional modifier.")


@bot.command()
async def wrolla(ctx, modifier=''):
    try:
        # Roll with advantage (2d20) and calculate the total
        rolls = [random.randint(1, 20) for _ in range(2)]
        total = max(rolls)

        # Apply the modifier if provided
        if modifier:
            total += int(modifier)

        # Send the roll result as a DM to the sender
        dm_channel = await ctx.author.create_dm()
        await dm_channel.send(f'```Rolling with Advantage: {", ".join(map(str, rolls))}\nTotal: {total}```')

    except ValueError:
        await ctx.send('Invalid modifier. Please provide a valid number for the modifier.')


@bot.command()
async def wrolld(ctx, modifier=''):
    try:
        # Roll with disadvantage (2d20) and calculate the total
        rolls = [random.randint(1, 20) for _ in range(2)]
        total = min(rolls)

        # Apply the modifier if provided
        if modifier:
            total += int(modifier)

        # Send the roll result as a DM to the sender
        dm_channel = await ctx.author.create_dm()
        await dm_channel.send(f'```Rolling with Disadvantage: {", ".join(map(str, rolls))}\nTotal: {total}```')

    except ValueError:
        await ctx.send('Invalid modifier. Please provide a valid number for the modifier.')

