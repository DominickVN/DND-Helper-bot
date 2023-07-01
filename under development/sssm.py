#server-specific state management

# from bot import bot

# class ServerState:
#     def __init__(self):
#         self.initiative_tracker = {}  # Example: Initiative tracker for combat
#         self.npc_data = {}  # Example: Data for NPCs specific to the server

#     def clear_state(self):
#         self.initiative_tracker.clear()
#         self.npc_data.clear()
#         # Add other state attributes as needed
#     def add_dice_roll(self, dice_expression, rolls, total):
#         self.dice_history.append((dice_expression, rolls, total))

# server_states = {}

# @bot.event
# async def on_guild_join(guild):
#     server_states[guild.id] = ServerState()

# @bot.event
# async def on_guild_remove(guild):
#     server_states.pop(guild.id, None)
