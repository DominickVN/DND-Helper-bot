from bot import bot
import math

@bot.command()
async def calculate(ctx, *, expression):
    try:
        result = evaluate_expression(expression)
        await ctx.send(f'```{expression} = {result}```')
    except Exception as e:
        await ctx.send(f'Error: {str(e)}')

def evaluate_expression(expression):
    # Remove any whitespace from the expression
    expression = expression.replace(' ', '')

    # Replace 'sqrt' with 'math.sqrt'
    expression = expression.replace('sqrt', 'math.sqrt')

    # Evaluate the expression using eval() function
    result = eval(expression)

    return result


#I did not write this, ChatGPT did