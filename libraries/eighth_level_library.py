eighth_level_spells = {
    "abi-dalzim's horrid wilting": {
        "description": "You draw the moisture from every creature in a 30-foot cube centered on a point you choose within range. Each creature in that area must make a Constitution Saving Throw. Constructs and undead aren't affected, and plants and water elementals make this Saving Throw with disadvantage. A creature takes 12d8 necrotic damage on a failed save, or half as much damage on a successful one.\n\nNonmagical plants in the area that aren't creatures, such as trees and shrubs, wither and die instantly.",
        "level": 8,
        "casting_time": "1 action",
        "range": "150 feet",
        "components": "V, S",
        "duration": "Instantaneous",
        "school": "Necromancy",


    },
    "animal shapes": {
        "description": "Your magic turns others into beasts. Choose any number of willing creatures that you can see within range. You transform each target into the form of a large or smaller beast with a challenge rating of 4 or lower. On subsequent turns, you can use your action to transform affected creatures into new forms.\n\nThe transformation lasts for the duration for each target, or until the target drops to 0 hit points or dies. You can choose a different form for each target. A target's game statistics are replaced by the statistics of the chosen beast, though the target retains its alignment and Intelligence, Wisdom, and Charisma Scores. The target assumes the hit points of its new form, and when it reverts to its normal form, it returns to the number of hit points it had before it transformed. If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form. As long as the excess damage doesn't reduce the creature's normal form to 0 hit points, it isn't knocked unconscious. The creature is limited in the actions it can perform by the nature of its new form, and it can't speak or cast spells.\n\nThe target's gear melds into the new form. The target can't activate, wield, or otherwise benefit from any of its equipment.",
        "level": 8,
        "casting_time": "1 action",
        "range": "30 feet",
        "components": "V, S, M",
        "duration": "Concentration, up to 24 hours",
        "school": "Transmutation",
        "concentration": True,

    },
    "antimagic field": {
        "description": "A 10-foot-radius invisible sphere of antimagic surrounds you. This area is divorced from the magical energy that suffuses the multiverse. Within the sphere, spells can't be cast, summoned creatures disappear, and even magic items become mundane. Until the spell ends, the sphere moves with you, centered on you.\n\nSpells and other magical effects, except those created by an artifact or a deity, are suppressed in the sphere and can't protrude into it. A slot expended to cast a suppressed spell is consumed. While an effect is suppressed, it doesn't function, but the time it spends suppressed counts against its duration.\n\nTargeted Effects\nSpells and other magical effects, such as magic missile and charm person, that target a creature or an object in the sphere have no effect on that target.\n\nAreas of Magic\nThe area of another spell or magical effect, such as [fireball][link], can't extend into the sphere. If the sphere overlaps an area of magic, the part of the area that is covered by the sphere is suppressed. For example, the flames created by a wall of fire are suppressed within the sphere, creating a gap in the wall if the overlap is large enough.\n\nSpells\nAny active spell or other magical effect on a creature or an object in the sphere is suppressed while the creature or object is in it.\n\nMagic Items\nThe properties and powers of magic items are suppressed in the sphere. For example, a +1 longsword in the sphere functions as a nonmagical longsword.\n\nA magic weapon's properties and powers are suppressed if it is used against a target in the sphere or wielded by an attacker in the sphere. If a magic weapon or a piece of magic ammunition fully leaves the sphere (for example, if you fire a magic arrow or throw a magic spear at a target outside the sphere), the magic of the item ceases to be suppressed as soon as it exits.\n\nMagical Travel\nTeleportation and planar travel fail to work in the sphere, whether the sphere is the destination or the departure point for such magical travel. A portal to another location, world, or plane of existence, as well as an opening to an extradimensional space such as that created by the rope trick spell, temporarily closes while in the sphere.\n\nCreatures and Objects\nA creature or object summoned or created by magic temporarily winks out of existence in the sphere. Such a creature instantly reappears once the space the creature occupied is no longer within the sphere.\n\nDispel Magic\nSpells and magical effects such as [dispel magic][link] have no effect on the sphere. Likewise, the spheres created by different [antimagic field][link] spells don't nullify each other.",
        "level": 8,
        "casting_time": "1 action",
        "range": "Self (10-foot radius)",
        "components": "V, S, M",
        "duration": "Concentration, up to 1 hour",
        "school": "Abjuration",
        "concentration": True,

    },
    "antipathy sympathy": {
        "description": "This spell attracts or repels creatures of your choice. You target something within range, either a huge or smaller object or creature or an area that is no larger than a 200-foot cube. Then specify a kind of intelligent creature, such as red dragons, goblins, or vampires. You invest the target with an aura that either attracts or repels the specified creatures for the duration. Choose antipathy or sympathy as the aura's effect.\n\nAntipathy\nThe enchantment causes creatures of the kind you designated to feel an intense urge to leave the area and avoid the target. When such a creature can see the target or comes within 60 feet of it, the creature must succeed on a Wisdom Saving Throw or become frightened. The creature remains frightened while it can see the target or is within 60 feet of it. While frightened by the target, the creature must use its movement to move to the nearest safe spot from which it can't see the target. If the creature moves more than 60 feet from the target and can't see it, the creature is no longer frightened, but the creature becomes frightened again if it regains sight of the target or moves within 60 feet of it.\n\nSympathy\nThe enchantment causes the specified creatures to feel an intense urge to approach the target while within 60 feet of it or able to see it. When such a creature can see the target or comes within 60 feet of it, the creature must succeed on a Wisdom Saving Throw or use its movement on each of its turns to enter the area or move within reach of the target. When the creature has done so, it can't willingly move away from the target.\n\nIf the target damages or otherwise harms an affected creature, the affected creature can make a Wisdom Saving Throw to end the effect, as described below.\n\nEnding the Effect\nIf an affected creature ends its turn while not within 60 feet of the target or able to see it, the creature makes a Wisdom Saving Throw. On a successful save, the creature is no longer affected by the target and recognizes the feeling of repugnance or attraction as magical. In addition, a creature affected by the spell is allowed another Wisdom Saving Throw every 24 hours while the spell persists.\n\nA creature that successfully saves against this effect is immune to it for 1 minute, after which time it can be affected again.",
        "level": 8,
        "casting_time": "1 hour",
        "range": "60 feet",
        "components": "V, S, M",
        "duration": "10 days",
        "school": "Enchantment",


    },
    "clone": {
        "description": "This spell grows an inert duplicate of a living, medium creature as a safeguard against death. This clone forms inside a sealed vessel and grows to full size and maturity after 120 days; you can also choose to have the clone be a younger version of the same creature. It remains inert and endures indefinitely, as long as its vessel remains undisturbed.\n\nAt any time after the clone matures, if the original creature dies, its soul transfers to the clone, provided that the soul is free and willing to return. The clone is physically identical to the original and has the same personality, memories, and abilities, but none of the original's equipment. The original creature's physical remains, if they still exist, become inert and can't thereafter be restored to life, since the creature's soul is elsewhere.",
        "level": 8,
        "casting_time": "1 hour",
        "range": "Touch",
        "components": "V, S, M - a diamond worth at least 1,000 gp and at least 1 cubic inch of flesh of the creature that is to be cloned, which the spell consumes, and a vessel worth at least 2,000 gp that has a sealable lid and is large enough to hold a medium creature, such as a huge urn, coffin, mud-filled cyst in the ground, or crystal container filled with salt water",
        "duration": "Instantaneous",
        "school": "Necromancy",


    },
    "control weather": {
        "description": "You take control of the weather within 5 miles of you for the duration. You must be outdoors to cast this spell. Moving to a place where you don't have a clear path to the sky ends the spell early.\n\nWhen you cast the spell, you change the current weather conditions, which are determined by the DM based on the climate and season. You can change precipitation, temperature, and wind. It takes 1d4 x 10 minutes for the new conditions to take effect. Once they do so, you can change the conditions again. When the spell ends, the weather gradually returns to normal.\n\nWhen you change the weather conditions, find a current condition on the following tables and change its stage by one, up or down. When changing the wind, you can change its direction. [The tables added too many characters and didn't work so I will add them later]",
        "level": 8,
        "casting_time": "10 minutes",
        "range": "Self (5-mile radius)",
        "components": "V, S, M",
        "duration": "Concentration, up to 8 hours",
        "school": "Transmutation",
        "concentration": True,

    },
    "demiplane": {
        "description": "You create a shadowy door on a flat solid surface that you can see within range. The door is large enough to allow medium creatures to pass through unhindered. When opened, the door leads to a demiplane that appears to be an empty room 30 feet in each dimension, made of wood or stone. When the spell ends, the door disappears, and any creatures or objects inside the demiplane remain trapped there, as the door also disappears from the other side.\n\nEach time you cast this spell, you can create a new demiplane, or have the shadowy door connect to a demiplane you created with a previous casting of this spell. Additionally, if you know the nature and contents of a demiplane created by a casting of this spell by another creature, you can have the shadowy door connect to its demiplane instead.",
        "level": 8,
        "casting_time": "1 action",
        "range": "60 feet",
        "components": "S",
        "duration": "1 hour",
        "school": "Conjuration",


    },
    "dominate monster": {
        "description": "You attempt to beguile a creature that you can see within range. It must succeed on a Wisdom Saving Throw or be charmed by you for the duration. If you or creatures that are friendly to you are fighting it, it has advantage on the Saving Throw.\n\nWhile the creature is charmed, you have a telepathic link with it as long as the two of you are on the same plane of existence. You can use this telepathic link to issue commands to the creature while you are conscious (no action required), which it does its best to obey. You can specify a simple and general course of action, such as 'Attack that creature,' 'Run over there,' or 'Fetch that object.' If the creature completes the order and doesn't receive further direction from you, it defends and preserves itself to the best of its ability.\n\nYou can use your action to take total and precise control of the target. Until the end of your next turn, the creature takes only the actions you choose, and doesn't do anything that you don't allow it to do. During this time, you can also cause the creature to use a reaction, but this requires you to use your own reaction as well.\n\nEach time the target takes damage, it makes a new Wisdom Saving Throw against the spell. If the Saving Throw succeeds, the spell ends.\n\nWhen you cast this spell with a 9th-level spell slot, the duration is concentration, up to 8 hours.",
        "level": 8,
        "casting_time": "1 action",
        "range": "60 feet",
        "components": "V, S",
        "duration": "Concentration, up to 1 hour",
        "school": "Enchantment",
        "concentration": True,

    },
    "earthquake": {
        "description": "You create a seismic disturbance at a point on the ground that you can see within range. For the duration, an intense tremor rips through the ground in a 100-foot-radius circle centered on that point and shakes creatures and structures in contact with the ground in that area.\n\nThe ground in the area becomes difficult terrain. Each creature on the ground that is concentrating must make a Constitution Saving Throw. On a failed save, the creature's concentration is broken.\n\nWhen you cast this spell and at the end of each turn you spend concentrating on it, each creature on the ground in the area must make a Dexterity Saving Throw. On a failed save, the creature is knocked prone.\n\nThis spell can have additional effects depending on the terrain in the area, as determined by the DM.\n\nFissures\nFissures open throughout the spell's area at the start of your next turn after you cast the spell. A total of 1d6 such fissures open in locations chosen by the DM. Each is 1d10 x 10 feet deep, 10 feet wide, and extends from one edge of the spell's area to the opposite side. A creature standing on a spot where a fissure opens must succeed on a Dexterity Saving Throw or fall in. A creature that successfully saves moves with the fissure's edge as it opens.\n\nA fissure that opens beneath a structure causes it to automatically collapse (see below).\n\nStructures\nThe tremor deals 50 bludgeoning damage to any structure in contact with the ground in the area when you cast the spell and at the start of each of your turns until the spell ends. If a structure drops to 0 hit points, it collapses and potentially damages nearby creatures. A creature within half the distance of a structure's height must make a Dexterity Saving Throw. On a failed save, the creature takes 5d6 bludgeoning damage, is knocked prone, and is buried in the rubble, requiring a DC 20 Strength (Athletics) check as an action to escape. The DM can adjust the DC higher or lower, depending on the nature of the rubble. On a successful save, the creature takes half as much damage and doesn't fall prone or become buried.",
        "level": 8,
        "casting_time": "1 action",
        "range": "500 feet",
        "components": "V, S, M",
        "duration": "Concentration, up to 1 minute",
        "school": "Evocation",
        "concentration": True,

    },
    "feeblemind": {
        "description": "You blast the mind of a creature that you can see within range, attempting to shatter its intellect and personality. The target takes 4d6 psychic damage and must make an Intelligence Saving Throw.\n\nOn a failed save, the creature's Intelligence and Charisma Scores become 1. The creature can't cast spells, activate magic items, understand language, or communicate in any intelligible way. The creature can, however, identify its friends, follow them, and even protect them.\n\nAt the end of every 30 days, the creature can repeat its Saving Throw against this spell. If it succeeds on its Saving Throw, the spell ends.\n\nThe spell can also be ended by greater restoration, heal, or wish.",
        "level": 8,
        "casting_time": "1 action",
        "range": "150 feet",
        "components": "V, S, M",
        "duration": "Instantaneous",
        "school": "Enchantment",


    },
    "glibness": {
        "description": "Until the spell ends, when you make a Charisma Check, you can replace the number you roll with a 15. Additionally, no matter what you say, magic that would determine if you are telling the truth indicates that you are being truthful.",
        "level": 8,
        "casting_time": "1 action",
        "range": "Self",
        "components": "V",
        "duration": "1 hour",
        "school": "Transmutation",


    },
    "holy aura": {
        "description": "Divine light washes out from you and coalesces in a soft radiance in a 30-foot radius around you. Creatures of your choice in that radius when you cast this spell shed dim light in a 5-foot radius and have advantage on all Saving Throws, and other creatures have disadvantage on Attack Rolls against them until the spell ends. In addition, when a fiend or an undead hits an affected creature with a Melee Attack, the aura flashes with brilliant light. The attacker must succeed on a Constitution Saving Throw or be blinded until the spell ends.",
        "level": 8,
        "casting_time": "1 action",
        "range": "Self (30-foot radius)",
        "components": "V, S, M",
        "duration": "Concentration, up to 1 minute",
        "school": "Abjuration",
        "concentration": True,

    },
    "illusory dragon": {
        "description": "By gathering threads of shadow material from the Shadowfell, you create a huge shadowy dragon in an unoccupied space that you can see within range. The illusion lasts for the spell's duration and occupies its space, as if it were a creature.\n\nWhen the illusion appears, any of your enemies that can see it must succeed on a Wisdom Saving Throw or become frightened of it for 1 minute. If a frightened creature ends its turn in a location where it doesn't have line of sight to the illusion, it can repeat the Saving Throw, ending the effect on itself on a success.\n\nAs a bonus action on your turn, you can move the illusion up to 60 feet. At any point during its movement, you can cause it to exhale a blast of energy in a 60-foot cone originating from its space. When you create the dragon, choose a damage type: acid, cold, fire, lightning, necrotic, or poison. Each creature in the cone must make an Intelligence Saving Throw, taking 7d6 damage of the chosen damage type on a failed save, or half as much damage on a successful one.\n\nThe illusion is tangible because of the shadow stuff used to create it, but attacks miss it automatically, it succeeds on all Saving Throws, and it is immune to all damage and conditions. A creature that uses an action to examine the dragon can determine that it is an illusion by succeeding on an Intelligence (Investigation) check against your Spell Save DC. If a creature discerns the illusion for what it is, the creature can see through it and has advantage on Saving Throws against its breath.",
        "level": 8,
        "casting_time": "1 action",
        "range": "120 feet",
        "components": "V, S, M",
        "duration": "Concentration, up to 1 minute",
        "school": "Illusion",
        "concentration": True,

    },
    "incendiary cloud": {
        "description": "A swirling cloud of smoke shot through with white-hot embers appears in a 20-foot-radius sphere centered on a point within range. The cloud spreads around corners and is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it.\n\nWhen the cloud appears, each creature in it must make a Dexterity Saving Throw. A creature takes 10d8 fire damage on a failed save, or half as much damage on a successful one. A creature must also make this Saving Throw when it enters the spell's area for the first time on a turn or ends its turn there.\n\nThe cloud moves 10 feet directly away from you in a direction that you choose at the start of each of your turns.",
        "level": 8,
        "casting_time": "1 action",
        "range": "150 feet",
        "components": "V, S",
        "duration": "Concentration, up to 1 minute",
        "school": "Conjuration",
        "concentration": True,

    },
    "maddening darkness": {
        "description": "Magical darkness spreads from a point you choose within range to fill a 60-foot-radius sphere until the spell ends. The darkness spreads around corners. A creature with darkvision can't see through this darkness. Non-magical light, as well as light created by spells of 8th level or lower, can't illuminate the area.\n\nShrieks, gibbering, and mad laughter can be heard within the sphere. Whenever a creature starts its turn in the sphere, it must make a Wisdom Saving Throw, taking 8d8 psychic damage on a failed save, or half as much damage on a successful one.",
        "level": 8,
        "casting_time": "1 action",
        "range": "150 feet",
        "components": "V, M",
        "duration": "Concentration, up to 10 minutes",
        "school": "Evocation",
        "concentration": True,

    },
    "maze": {
        "description": "You banish a creature that you can see within range into a labyrinthine demiplane. The target remains there for the duration or until it escapes the maze.\n\nThe target can use its action to attempt to escape. When it does so, it makes a DC 20 Intelligence Check. If it succeeds, it escapes, and the spell ends (a minotaur or goristro demon automatically succeeds).\n\nWhen the spell ends, the target reappears in the space it left or, if that space is occupied, in the nearest unoccupied space.",
        "level": 8,
        "casting_time": "1 action",
        "range": "60 feet",
        "components": "V, S",
        "duration": "Concentration, up to 10 minutes",
        "school": "Conjuration",
        "concentration": True,

    },
    "mighty fortress": {
        "description": "A fortress of stone erupts from a square area of ground of your choice that you can see within range. The area is 120 feet on each side, and it must not have any buildings or other structures on it. Any creatures in the area are harmlessly lifted up as the fortress rises.\n\nThe fortress has four turrets with square bases, each one 20 feet on a side and 30 feet tall, with one turret on each corner. The turrets are connected to each other by stone walls that are each 80 feet long, creating an enclosed area. Each wall is 1 foot thick and is composed of panels that are 10 feet wide and 20 feet tall. Each panel is contiguous with two other panels or one other panel and a turret. You can place up to four stone doors in the fortress's outer wall.\n\nA small keep stands inside the enclosed area. The keep has a square base that is 50 feet on each side, and it has three floors with 10-foot-high ceilings. Each of the floors can be divided into as many rooms as you like, provided each room is at least 5 feet on each side. The floors of the keep are connected by stone staircases, its walls are 6 inches thick, and interior rooms can have stone doors or open archways as you choose. The keep is furnished and decorated however you like, and it contains sufficient food to serve a nine-course banquet for up to 100 people each day. Furnishings, food, and other objects created by this spell crumble to dust if removed from the fortress.\n\nA staff of one hundred invisible servants obeys any command given to them by creatures you designate when you cast the spell. Each servant functions as if created by the unseen servant spell.\n\nThe walls, turrets, and keep are all made of stone that can be damaged. Each 10-foot-by-10-foot section of stone has AC 15 and 30 hit points per inch of thickness. It is immune to poison and psychic damage. Reducing a section of stone to 0 hit points destroys it and might cause connected sections to buckle and collapse at the DM's discretion.\n\nAfter 7 days or when you cast this spell somewhere else, the fortress harmlessly crumbles and sinks back into the ground, leaving any creatures that were inside it safely on the ground.\n\nCasting this spell on the same spot once every 7 days for a year makes the fortress permanent.",
        "level": 8,
        "casting_time": "1 minute",
        "range": "Touch",
        "components": "V, S, M",
        "duration": "Instantaneous",
        "school": "Conjuration",


    },
    "mind blank": {
        "description": "Until the spell ends, one willing creature you touch is immune to psychic damage, any effect that would sense its emotions or read its thoughts, divination spells, and the charmed condition. The spell even foils [wish][link] spells and spells or effects of similar power used to affect the target's mind or to gain information about the target.",
        "level": 8,
        "casting_time": "1 action",
        "range": "Touch",
        "components": "V, S",
        "duration": "24 hours",
        "school": "Abjuration",


    },
    "power word stun": {
        "description": "You speak a word of power that can overwhelm the mind of one creature you can see within range, leaving it dumbfounded. If the target has 150 hit points or fewer, it is stunned. Otherwise, the spell has no effect.\n\nThe stunned target must make a Constitution Saving Throw at the end of each of its turns. On a successful save, this stunning effect ends.",
        "level": 8,
        "casting_time": "1 action",
        "range": "60 feet",
        "components": "V",
        "duration": "Instantaneous",
        "school": "Enchantment",


    },
    "sunburst": {
        "description": "Brilliant sunlight flashes in a 60-foot radius centered on a point you choose within range. Each creature in that light must make a Constitution Saving Throw. On a failed save, a creature takes 12d6 radiant damage and is blinded for 1 minute. On a successful save, it takes half as much damage and isn't blinded by this spell. Undead and oozes have disadvantage on this Saving Throw.\n\nA creature blinded by this spell makes another Constitution Saving Throw at the end of each of its turns. On a successful save, it is no longer blinded.\n\nThis spell dispels any darkness in its area that was created by a spell.",
        "level": 8,
        "casting_time": "1 action",
        "range": "150 feet",
        "components": "V, S, M",
        "duration": "Instantaneous",
        "school": "Evocation",


    },
    "telepathy": {
        "description": "You create a telepathic link between yourself and a willing creature with which you are familiar. The creature can be anywhere on the same plane of existence as you. The spell ends if you or the target are no longer on the same plane.\n\nUntil the spell ends, you and the target can instantaneously share words, images, sounds, and other sensory messages with one another through the link, and the target recognizes you as the creature it is communicating with. The spell enables a creature with an Intelligence Score of at least 1 to understand the meaning of your words and take in the scope of any sensory messages you send to it.",
        "level": 8,
        "casting_time": "1 action",
        "range": "Unlimited",
        "components": "V, S, M",
        "duration": "24 hours",
        "school": "Divination",


    },
    "tsunami": {
        "description": "A wall of water springs into existence at a point you choose within range. You can make the wall up to 300 feet long, 300 feet high, and 50 feet thick. The wall lasts for the duration.\n\nWhen the wall appears, each creature within its area must make a Strength Saving Throw. On a failed save, a creature takes 6d10 bludgeoning damage, or half as much damage on a successful save.\n\nAt the start of each of your turns after the wall appears, the wall, along with any creatures in it, moves 50 feet away from you. Any huge or smaller creature inside the wall or whose space the wall enters when it moves must succeed on a Strength Saving Throw or take 5d10 bludgeoning damage. A creature can take this damage only once per round. At the end of the turn, the wall's height is reduced by 50 feet, and the damage creatures take from the spell on subsequent rounds is reduced by 1d10. When the wall reaches 0 feet in height, the spell ends.\n\nA creature caught in the wall can move by swimming. Because of the force of the wave, though, the creature must make a successful Strength (Athletics) check against your Spell Save DC in order to move at all. If it fails the check, it can't move. A creature that moves out of the area falls to the ground.",
        "level": 8,
        "casting_time": "1 minute",
        "range": "300 feet",
        "components": "V, S",
        "duration": "Instantaneous",
        "school": "Conjuration",
    }
}
