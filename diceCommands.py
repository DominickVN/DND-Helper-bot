import random
from bot import bot


@bot.command()
async def roll(ctx, roll_type='', dice_expression='1d20'):
    try:
        is_advantage = False
        is_disadvantage = False

        # Check if Advantage or Disadvantage is specified
        if roll_type.lower() == 'a':
            is_advantage = True
        elif roll_type.lower() == 'd':
            is_disadvantage = True

        # Parse the dice expression
        parts = dice_expression.lower().split('+')
        num_dice, num_sides = map(int, parts[0].split('d'))
        if num_dice <= 0 or num_sides <= 0:
            raise ValueError

        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]

        # Apply Advantage or Disadvantage
        if is_advantage:
            rolls = rolls + [random.randint(1, num_sides) for _ in range(num_dice)]
            total = max(rolls)
            roll_msg = f'Rolling {dice_expression} with Advantage:'
        elif is_disadvantage:
            rolls = rolls + [random.randint(1, num_sides) for _ in range(num_dice)]
            total = min(rolls)
            roll_msg = f'Rolling {dice_expression} with Disadvantage:'
        else:
            total = sum(rolls)
            roll_msg = f'Rolling {dice_expression}:'

        if len(parts) > 1:
            modifiers = list(map(int, parts[1:]))
            total += sum(modifiers)

        await ctx.send(f'```{roll_msg} {", ".join(map(str, rolls))}\nTotal: {total}```')
    except ValueError:
        await ctx.send(
            "Invalid dice expression. Please use the format XdY[+Z], where X is the number of dice, Y is the number of sides, and Z is an optional modifier. "
            "You can specify 'a' for Advantage or 'd' for Disadvantage after the command.")


@bot.command()
async def whisperRoll(ctx, roll_type='', dice_expression='1d20'):
    try:
        is_advantage = False
        is_disadvantage = False

        # Check if Advantage or Disadvantage is specified
        if roll_type.lower() == 'a':
            is_advantage = True
        elif roll_type.lower() == 'd':
            is_disadvantage = True

        # Parse the dice expression
        parts = dice_expression.lower().split('+')
        num_dice, num_sides = map(int, parts[0].split('d'))
        if num_dice <= 0 or num_sides <= 0:
            raise ValueError

        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]

        # Apply Advantage or Disadvantage
        if is_advantage:
            rolls = rolls + [random.randint(1, num_sides) for _ in range(num_dice)]
            total = max(rolls)
            roll_msg = f'Rolling {dice_expression} with Advantage:'
        elif is_disadvantage:
            rolls = rolls + [random.randint(1, num_sides) for _ in range(num_dice)]
            total = min(rolls)
            roll_msg = f'Rolling {dice_expression} with Disadvantage:'
        else:
            total = sum(rolls)
            roll_msg = f'Rolling {dice_expression}:'

        if len(parts) > 1:
            modifiers = list(map(int, parts[1:]))
            total += sum(modifiers)

        # Create a direct message channel with the sender
        dm_channel = await ctx.author.create_dm()

        # Send the roll result to the sender's DMs
        await dm_channel.send(f'```{roll_msg} {", ".join(map(str, rolls))}\nTotal: {total}```')
    except ValueError:
        await ctx.send(
            "Invalid dice expression. Please use the format XdY[+Z], where X is the number of dice, Y is the number of sides, and Z is an optional modifier. "
            "You can specify 'a' for Advantage or 'd' for Disadvantage after the command.")
