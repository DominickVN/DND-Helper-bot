import random
import discord
from bot import bot


@bot.command(aliases=['r'])
async def roll(ctx, dice_expression='1d20', modifier=''):
    try:
        parts = dice_expression.split('+')
        dice_part = parts[0]
        modifier_part = parts[1] if len(parts) > 1 else '0'

        num_dice, num_sides = map(int, dice_part.lower().split('d'))
        modifier = int(modifier_part) if modifier_part else 0

        if num_dice <= 0 or num_sides <= 0:
            raise ValueError

        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(rolls) + modifier
        result_str = ', '.join(str(roll) if roll != 20 else f'**{roll}**' for roll in rolls)

        embed = discord.Embed(title='Roll', color=discord.Color.green())
        embed.add_field(name='', value=dice_expression, inline=False)
        embed.add_field(name='Results', value=result_str, inline=False)
        if modifier != 0:
            embed.add_field(name='Modifier', value=str(modifier), inline=False)
        embed.add_field(name='Total', value=str(total), inline=False)

        await ctx.send(embed=embed)

    except (ValueError, IndexError):
        await ctx.send('Invalid dice expression. Please use the format XdY[+Z], where X is the number of dice, Y is the number of sides, and Z is an optional modifier.')



@bot.command(aliases=['ra'])
async def rolla(ctx, modifier=''):
    try:
        rolls = [random.randint(1, 20) for _ in range(2)]
        modifier = int(modifier) if modifier else 0
        total = max(rolls) + modifier

        embed = discord.Embed(title='Roll with Advantage', color=discord.Color.green())
        embed.add_field(name='Results', value=', '.join(map(str, rolls)), inline=False)
        if modifier != 0:
            embed.add_field(name='Modifier', value=str(modifier), inline=False)
        embed.add_field(name='Total', value=str(total), inline=False)

        await ctx.send(embed=embed)

    except ValueError:
        await ctx.send('Invalid modifier. Please provide a valid number for the modifier.')


@bot.command(aliases=['rd'])
async def rolld(ctx, modifier=''):
    try:
        rolls = [random.randint(1, 20) for _ in range(2)]
        modifier = int(modifier) if modifier else 0
        total = min(rolls) + modifier

        embed = discord.Embed(title='Roll with Disadvantage', color=discord.Color.green())
        embed.add_field(name='Results', value=', '.join(map(str, rolls)), inline=False)
        if modifier != 0:
            embed.add_field(name='Modifier', value=str(modifier), inline=False)
        embed.add_field(name='Total', value=str(total), inline=False)

        await ctx.send(embed=embed)

    except ValueError:
        await ctx.send('Invalid modifier. Please provide a valid number for the modifier.')


@bot.command(aliases=['wr'])
async def wroll(ctx, dice_expression='', modifier=''):
    try:
        parts = dice_expression.lower().split('+')
        num_dice, num_sides = map(int, parts[0].split('d'))
        modifier = int(modifier) if modifier else 0

        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(rolls) + modifier

        embed = discord.Embed(title='Whisper Roll', color=discord.Color.green())
        embed.add_field(name='Expression', value=dice_expression, inline=False)
        embed.add_field(name='Results', value=', '.join(map(str, rolls)), inline=False)
        if modifier != 0:
            embed.add_field(name='Modifier', value=str(modifier), inline=False)
        embed.add_field(name='Total', value=str(total), inline=False)

        dm_channel = await ctx.author.create_dm()
        await dm_channel.send(embed=embed)

    except (ValueError, IndexError):
        await ctx.send(
            "Invalid dice expression. Please use the format XdY[+Z], where X is the number of dice, Y is the number of sides, and Z is an optional modifier.")


@bot.command(aliases=['wra'])
async def wrolla(ctx, modifier=''):
    try:
        rolls = [random.randint(1, 20) for _ in range(2)]
        modifier = int(modifier) if modifier else 0
        total = max(rolls) + modifier

        embed = discord.Embed(title='Whisper Roll with Advantage', color=discord.Color.green())
        embed.add_field(name='Results', value=', '.join(map(str, rolls)), inline=False)
        if modifier != 0:
            embed.add_field(name='Modifier', value=str(modifier), inline=False)
        embed.add_field(name='Total', value=str(total), inline=False)

        dm_channel = await ctx.author.create_dm()
        await dm_channel.send(embed=embed)

    except ValueError:
        await ctx.send('Invalid modifier. Please provide a valid number for the modifier.')

@bot.command(aliases=['wrd'])
async def wrolld(ctx, modifier=''):
    try:
        rolls = [random.randint(1, 20) for _ in range(2)]
        modifier = int(modifier) if modifier else 0
        total = min(rolls) + modifier

        embed = discord.Embed(title='Whisper Roll with Disadvantage', color=discord.Color.green())
        embed.add_field(name='Results', value=', '.join(map(str, rolls)), inline=False)
        if modifier != 0:
            embed.add_field(name='Modifier', value=str(modifier), inline=False)
        embed.add_field(name='Total', value=str(total), inline=False)

        dm_channel = await ctx.author.create_dm()
        await dm_channel.send(embed=embed)

    except ValueError:
        await ctx.send('Invalid modifier. Please provide a valid number for the modifier.')


@bot.command(aliases=['fac'])
async def flipacoin(ctx):
    result = random.choice(["Heads", "Tails"])

    embed = discord.Embed(title='Flip a Coin', color=discord.Color.green())
    embed.add_field(name='', value=result, inline=False)

    await ctx.send(embed=embed)