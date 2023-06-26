from bot import bot
from libraries.classes_library import class_rules
import discord

@bot.command(aliases=['class','cl'])
async def clas(ctx, class_name=None):
    if class_name is None:
        await ctx.send("Please provide a class name. Usage: `!class (class_name)`")
        return

    # Check if the class name is valid
    if class_name.lower() not in class_library:
        await ctx.send(f"Invalid class name. Available classes: {', '.join(class_library.keys())}")
        return

    class_info = class_library[class_name.lower()]

    # Generate the class rules string
    rules_str = ""
    for level, rules in class_info.features.items():
        rules_str += f"Level {level}:\n"
        for rule in rules:
            rules_str += f"- {rule}\n"
        rules_str += "\n"

    await ctx.send(f"Class: {class_name.capitalize()}\n```{rules_str}```")
