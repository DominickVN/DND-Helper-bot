from bot import bot
import math
import discord

@bot.command(aliases = ["calc"])
async def calculate(ctx, *, expression):
    try:
        result = evaluate_expression(expression)
        embed = discord.Embed(title=f"Calculation Result", description=f"```{expression} = {result}```", color=discord.Color.dark_gray())
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(title="Error", description=f"Error occurred: {str(e)}", color=discord.Color.dark_gray())
        await ctx.send(embed=embed)

def evaluate_expression(expression):
    # Remove any whitespace from the expression
    expression = expression.replace(' ', '')

    # Replace 'sqrt' with 'math.sqrt'
    expression = expression.replace('sqrt', 'math.sqrt')

    # Evaluate the expression using eval() function
    result = eval(expression)

    return result


#I did not write this, ChatGPT did