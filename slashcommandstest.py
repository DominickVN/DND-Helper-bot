import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name='hi')
async def hi(interaction):
    await interaction.response.send_message('Hello!')
    try:        
        await tree.sync(guild=discord.Object(id=362747783679180801))

        print(f'Synced')
    except Exception as e:
        print(e)