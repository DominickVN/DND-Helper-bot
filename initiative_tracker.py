from discord import Member
from bot import bot
import discord

initiative_trackers = {}

@bot.command(aliases=['i'])
async def initiative(ctx, action=None, *, args=None):
    server_id = ctx.guild.id

    # Checks if the server has an active initiative tracker, so initiatives aren't shared between servers
    if server_id not in initiative_trackers:
        initiative_trackers[server_id] = {
            'main_initiative': {},
            'secret_initiative': {},
        }

    main_initiative_tracker = initiative_trackers[server_id]['main_initiative']
    secret_initiative_tracker = initiative_trackers[server_id]['secret_initiative']

    if action == 'start':
        main_initiative_tracker.clear()
        secret_initiative_tracker.clear()
        embed = discord.Embed(title="Initiative Tracking Started", description="Players can now roll initiative using `!initiative rolled (roll)`.", color=discord.Color.purple())
        await ctx.send(embed=embed)

    elif action == 'rolled':
        if args is None:
            await ctx.send("Invalid Usage. Please provide your initiative roll. Usage: `!initiative rolled (roll)`.")
            return
        member = ctx.author
        main_initiative_tracker[member] = int(args)

        embed = discord.Embed(title="Initiative Rolled", description=f"{member.display_name} rolled initiative: {args}", color=discord.Color.purple())
        await ctx.send(embed=embed)

    elif action == 'add':
        if args is None:
            await ctx.send("Invalid Usage. Please provide the name and rolled initiative. Usage: `!initiative add (name) (rolled)`.")
            return
        # Splits the args into name and rolled initiative
        name, rolled = args.split(maxsplit=1)
        main_initiative_tracker[name] = int(rolled)

        embed = discord.Embed(title="Creature Added", description=f"Added name: {name} with rolled initiative: {rolled}", color=discord.Color.purple())
        await ctx.send(embed=embed)

    elif action == 'secretadd':
        if args is None:
            await ctx.send("Invalid Usage. Please provide the name and rolled initiative. Usage: `!initiative secretAdd (name) (rolled)`.")
            return
        name, rolled = args.split(maxsplit=1)
        # Adds the secret names and rolled initiative to the secret initiative tracker
        secret_initiative_tracker[name] = int(rolled)
        # Creates a direct message channel with the sender
        dm_channel = await ctx.author.create_dm()

        embed = discord.Embed(title="Secret Name Added", description=f"Added secret name: {name} with rolled initiative: {rolled}", color=discord.Color.purple())
        await dm_channel.send(embed=embed)

    elif action == 'edit':
        if main_initiative_tracker:
            embed = discord.Embed(title="Initiative Tracking in Progress", description="Initiative tracking is now in progress. Use `!initiative add (name) (rolled)` to add more names to the tracker.", color=discord.Color.purple())
        else:
            embed = discord.Embed(title="Initiative Tracking Not Started", description="Initiative tracking has not been started. Use `!initiative start` to start the tracking.", color=discord.Color.red())
        await ctx.send(embed=embed)

    elif action == 'end':
        if not main_initiative_tracker:
            await ctx.send("Invalid Action. Initiative tracking is not started or no rolls have been made yet.")
            return
        sorted_main_initiative = sorted(main_initiative_tracker.items(), key=lambda x: x[1], reverse=True)
        main_initiative_order = '\n'.join(f'{i+1}. {name} - {initiative}' for i, (name, initiative) in enumerate(sorted_main_initiative) if name not in secret_initiative_tracker)
        embed = discord.Embed(title="Initiative Order", description=main_initiative_order, color=discord.Color.purple())
        await ctx.send(embed=embed)

        # Checks if any secret names were added
        if secret_initiative_tracker:
            # Combines main initiative tracker and secret initiative tracker
            combined_initiative_tracker = {**main_initiative_tracker, **secret_initiative_tracker}
            sorted_combined_initiative = sorted(combined_initiative_tracker.items(), key=lambda x: x[1], reverse=True)
            secret_initiative_order = '\n'.join(f'{i+1}. {name} - {initiative}' for i, (name, initiative) in enumerate(sorted_combined_initiative))

            # Sends the secret initiative order as a direct message to the person who added the secret names
            dm_channel = await ctx.author.create_dm()
            embed = discord.Embed(title="Secret Initiative Order", description=secret_initiative_order, color=discord.Color.purple())
            await dm_channel.send(embed=embed)

    elif action == 'remove':
        if args is None:
            await ctx.send("Invalid Usage. Please provide the name or number of the creature to remove. Usage: `!initiative remove (name/number)`.")
            return

        names_or_numbers = [item.strip() for item in args.split(',')]
        # Removes creatures from the main initiative tracker
        for name_or_number in names_or_numbers:
            if name_or_number.isdigit():
                index = int(name_or_number) - 1
                if 0 <= index < len(main_initiative_tracker):
                    removed_name = list(main_initiative_tracker.keys())[index]
                    del main_initiative_tracker[removed_name]
            else:
                removed_name = name_or_number
                if removed_name in main_initiative_tracker:
                    del main_initiative_tracker[removed_name]

        await ctx.send("Initiative tracker updated. Removed the specified creatures.")
        # Print the new initiative order without the removed names
        sorted_main_initiative = sorted(main_initiative_tracker.items(), key=lambda x: x[1], reverse=True)
        new_initiative_order = '\n'.join(f'{i+1}. {name} - {initiative}' for i, (name, initiative) in enumerate(sorted_main_initiative) if name not in secret_initiative_tracker)
        embed = discord.Embed(title="New Initiative Order", description=new_initiative_order, color=discord.Color.purple())
        await ctx.send(embed=embed)

    elif action == 'rename':
        if args is None:
            await ctx.send("Invalid Usage. Please provide the number of the creature to rename and the new name. Usage: `!initiative rename (number) (new_name)`.")
            return

        number, new_name = args.split(maxsplit=1)

        if not number.isdigit():
            await ctx.send("Invalid number. Please provide a valid number corresponding to a creature in the initiative order.")
            return

        index = int(number) - 1
        if index < 0 or index >= len(main_initiative_tracker):
            await ctx.send("Invalid number. Please provide a valid number corresponding to a creature in the initiative order.")
            return

        old_name = list(main_initiative_tracker.keys())[index]
        main_initiative_tracker[new_name] = main_initiative_tracker.pop(old_name)

        await ctx.send(f'Renamed creature at position {number} to "{new_name}". Initiative order updated.')
        # Prints the updated initiative order
        sorted_main_initiative = sorted(main_initiative_tracker.items(), key=lambda x: x[1], reverse=True)
        updated_initiative_order = '\n'.join(f'{i+1}. {name} - {initiative}' for i, (name, initiative) in enumerate(sorted_main_initiative) if name not in secret_initiative_tracker)
        embed = discord.Embed(title="Updated Initiative Order", description=updated_initiative_order, color=discord.Color.purple())
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Invalid Action", description="Invalid action. Usage:", color=discord.Color.red())
        embed.add_field(name="Start Tracking", value="!initiative start", inline=False)
        embed.add_field(name="Roll Initiative", value="!initiative rolled (roll)", inline=False)
        embed.add_field(name="Add Creature", value="!initiative add (name) (rolled)", inline=False)
        embed.add_field(name="Add Secret Creature", value="!initiative secretadd (name) (rolled)", inline=False)
        embed.add_field(name="Edit Initiative", value="!initiative edit", inline=False)
        embed.add_field(name="End Tracking", value="!initiative end", inline=False)
        embed.add_field(name="Remove Creature", value="!initiative remove (name/number)", inline=False)
        embed.add_field(name="Rename Creature", value="!initiative rename (number) (new_name)", inline=False)
        await ctx.send(embed=embed)

#known issues:
#'remove' sometimes removes the wrong name when using the number instead of the name. No idea why