from discord import Member
from bot import bot


main_initiative_tracker = {}  # Dictionary to store main initiative rolls
secret_initiative_tracker = {}  # Dictionary to store secret initiative rolls

@bot.command()
async def initiative(ctx, action=None, *, args=None):
    if action == 'start':
        main_initiative_tracker.clear()
        secret_initiative_tracker.clear()
        await ctx.send('```Initiative tracking started. Players can now roll initiative using `!initiative rolled (roll)`.```')

    elif action == 'rolled':
        if args is None:
            await ctx.send('```Please provide your initiative roll. Usage: !initiative rolled (roll)```')
            return

        # Get the member who rolled initiative
        member = ctx.author

        # Add the initiative roll to the main initiative tracker
        main_initiative_tracker[member] = int(args)

        await ctx.send(f'```{member.display_name} rolled initiative: {args}```')

    elif action == 'add':
        if args is None:
            await ctx.send('```Please provide the name and rolled initiative. Usage: !initiative add (name) (rolled)```')
            return

        # Split the args into name and rolled initiative
        name, rolled = args.split(maxsplit=1)

        # Add the name and rolled initiative to the main initiative tracker
        main_initiative_tracker[name] = int(rolled)

        await ctx.send(f'```Added name: {name} with rolled initiative: {rolled}```')

    elif action == 'secretAdd':
        if args is None:
            await ctx.send('```Please provide the name and rolled initiative. Usage: !initiative secretAdd (name) (rolled)```')
            return

        # Split the args into name and rolled initiative
        name, rolled = args.split(maxsplit=1)

        # Add the secret name and rolled initiative to the secret initiative tracker
        secret_initiative_tracker[name] = int(rolled)

        # Create a direct message channel with the sender
        dm_channel = await ctx.author.create_dm()

        await dm_channel.send(f'```Added secret name: {name} with rolled initiative: {rolled}```')

    elif action == 'end':
        if not main_initiative_tracker:
            await ctx.send('```Initiative tracking is not started or no rolls have been made yet.```')
            return

        # Sort the main initiative tracker by initiative rolls in descending order
        sorted_main_initiative = sorted(main_initiative_tracker.items(), key=lambda x: x[1], reverse=True)

        # Generate the main initiative order string
        main_initiative_order = '\n'.join(f'{i+1}. {name} - {initiative}' for i, (name, initiative) in enumerate(sorted_main_initiative) if name not in secret_initiative_tracker)

        # Send the main initiative order to where the command was called
        await ctx.send(f'```Main Initiative Order:\n{main_initiative_order}```')

        # Check if any secret names were added
        if secret_initiative_tracker:
            # Combine main initiative tracker and secret initiative tracker
            combined_initiative_tracker = {**main_initiative_tracker, **secret_initiative_tracker}

            # Sort the combined initiative tracker by initiative rolls in descending order
            sorted_combined_initiative = sorted(combined_initiative_tracker.items(), key=lambda x: x[1], reverse=True)

            # Generate the secret initiative order string
            secret_initiative_order = '\n'.join(f'{i+1}. {name} - {initiative}' for i, (name, initiative) in enumerate(sorted_combined_initiative))

            # Send the secret initiative order as a direct message to the person who added the secret names
            dm_channel = await ctx.author.create_dm()
            await dm_channel.send(f'```Secret Initiative Order:\n{secret_initiative_order}```')

    else:
        await ctx.send('```Invalid action. Usage: `!initiative start`, `!initiative rolled (roll)`, `!initiative add (name) (rolled)`, `!initiative secretAdd (name) (rolled)`, `!initiative end`.```')