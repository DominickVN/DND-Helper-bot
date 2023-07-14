import discord
from discord import app_commands
import creds

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=362747783679180801)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=362747783679180801), name = 'tester', description='testing') #guild specific slash command
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"I am working! I was made with Discord.py!", ephemeral = True) 

@tree.command(guild = discord.Object(id=362747783679180801), name = 'initiative', description='Start tracking initiative!') #guild specific slash command
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Start Rolling!") 


client.run(creds.TOKEN)

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

# class aclient(discord.Client):
#     def __init__(self):
#         super().__init__(intents = discord.Intents.default())
#         self.synced = False #we use this so the bot doesn't sync commands more than once

#     async def on_ready(self):
#         await self.wait_until_ready()
#         if not self.synced: #check if slash commands have been synced 
#             await tree.sync(guild = discord.Object(id=362747783679180801)) #guild specific: leave blank if global (global registration can take 1-24 hours)
#             self.synced = True
#         print(f"We have logged in as {self.user}.")

# client = aclient()
# tree = app_commands.CommandTree(client)

# @tree.command(guild = discord.Object(id=362747783679180801), name = 'initiative', description='Start tracking initiative!') #guild specific slash command
# async def slash2(interaction: discord.Interaction):
#     await interaction.response.send_message(f"Start Rolling!") 

# client.run(creds.TOKEN)