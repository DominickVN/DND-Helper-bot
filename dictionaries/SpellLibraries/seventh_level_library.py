seventh_level_spells = {
    'conjure celestial': {
        'description': 'You summon a celestial of challenge rating 4 or lower, which appears in an unoccupied space that you can see within range. The celestial disappears when it drops to 0 hit points or when the spell ends.\n\nThe celestial is friendly to you and your companions for the duration. Roll initiative for the celestial, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you), as long as they don\'t violate its alignment. If you don\'t issue any commands to the celestial, it defends itself from hostile creatures but otherwise takes no actions.\n\nThe DM has The Celestial\'s statistics.\n\nWhen you cast this spell using a 9th-level spell slot, you summon a celestial of challenge rating 5 or lower.',
        'level': 7,
        'casting_time': '1 minute',
        'range': '90 feet',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Conjuration',


    },
    'crown of stars': {
        'description': 'Seven star-like motes of light appear and orbit your head until the spell ends. You can use a bonus action to send one of the motes streaking toward one creature or object within 120 feet of you. When you do so, make a Ranged Spell Attack. On a hit, the target takes 4d12 radiant damage. Whether you hit or miss, the mote is expended. The spell ends early if you expend the last mote.\n\nIf you have four or more motes remaining, they shed bright light in a 30-foot radius and dim light for an additional 30 feet. If you have one to three motes remaining, they shed dim light in a 30-foot radius.\n\nWhen you cast this spell using a spell slot of 8th level or higher, the number of motes created increases by two for each slot level above 7th.',
        'level': 7,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Evocation',


    },
    'delayed blast fireball': {
        'description': 'A beam of yellow light flashes from your pointing finger, then condenses to linger at a chosen point within range as a glowing bead for the duration. When the spell ends, either because your concentration is broken or because you decide to end it, the bead blossoms with a low roar into an explosion of flame that spreads around corners. Each creature in a 20-foot-radius sphere centered on that point must make a Dexterity Saving Throw. A creature takes fire damage equal to the total accumulated damage on a failed save, or half as much damage on a successful one.\n\nThe spell\'s base damage is 12d6. If at the end of your turn the bead has not yet detonated, the damage increases by 1d6.\n\nIf the glowing bead is touched before the interval has expired, the creature touching it must make a Dexterity Saving Throw. On a failed save, the spell ends immediately, causing the bead to erupt in flame. On a successful save, the creature can throw the bead up to 40 feet. When it strikes a creature or a solid object, the spell ends, and the bead explodes.\n\nThe fire damages objects in the area and ignites flammable objects that aren\'t being worn or carried.\n\nWhen you cast this spell using a spell slot of 8th level or higher, the base damage increases by 1d6 for each slot level above 7th.',
        'level': 7,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'divine word': {
        'description': 'You utter a divine word, imbued with the power that shaped the world at the dawn of creation. Choose any number of creatures you can see within range. Each creature that can hear you must make a Charisma Saving Throw. On a failed save, a creature suffers an effect based on its current hit points:\n\n•50 hit points or fewer: deafened for 1 minute\n•40 hit points or fewer: deafened and blinded for 10 minutes\n•30 hit points or fewer: blinded, deafened, and stunned for 1 hour\n•20 hit points or fewer: killed instantly\n\nRegardless of its current hit points, a celestial, an elemental, a fey, or a fiend that fails its save is forced back to its plane of origin (if it isn\'t there already) and can\'t return to your current plane for 24 hours by any means short of a wish spell.',
        'level': 7,
        'casting_time': '1 bonus action',
        'range': '30 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'etherealness': {
        'description': 'You step into the border regions of the Ethereal Plane, in the area where it overlaps with your current plane. You remain in the Border Ethereal for the duration or until you use your action to dismiss the spell. During this time, you can move in any direction. If you move up or down, every foot of movement costs an extra foot. You can see and hear the plane you originated from, but everything there looks gray, and you can\'t see anything more than 60 feet away.\n\nWhile on the Ethereal Plane, you can only affect and be affected by other creatures on that plane. Creatures that aren\'t on the Ethereal Plane can\'t perceive you and can\'t interact with you, unless a special ability or magic has given them the ability to do so.\n\nYou ignore all objects and effects that aren\'t on the Ethereal Plane, allowing you to move through objects you perceive on the plane you originated from.\n\nWhen the spell ends, you immediately return to the plane you originated from in the spot you currently occupy. If you occupy the same spot as a solid object or creature when this happens, you are immediately shunted to the nearest unoccupied space that you can occupy and take force damage equal to twice the number of feet you are moved.\n\nThis spell has no effect if you cast it while you are on the Ethereal Plane or a plane that doesn\'t border it, such as one of the Outer Planes.\n\nWhen you cast this spell using a spell slot of 8th level or higher, you can target up to three willing creatures (including you) for each slot level above 7th. The creatures must be within 10 feet of you when you cast the spell.',
        'level': 7,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '8 hours',
        'school': 'Transmutation',


    },
    'finger of death': {
        'description': 'You send negative energy coursing through a creature that you can see within range, causing it searing pain. The target must make a Constitution Saving Throw. It takes 7d8 + 30 necrotic damage on a failed save, or half as much damage on a successful one.\n\nA humanoid killed by this spell rises at the start of your next turn as a Zombie that is permanently under your command, following your verbal orders to the best of its ability.',
        'level': 7,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Necromancy',


    },
    'fire storm': {
        'description': 'A storm made up of sheets of roaring flame appears in a location you choose within range. The area of the storm consists of up to ten 10-foot cubes, which you can arrange as you wish. Each cube must have at least one face adjacent to the face of another cube. Each creature in the area must make a Dexterity Saving Throw. It takes 7d10 fire damage on a failed save, or half as much damage on a successful one.\n\nThe fire damages objects in the area and ignites flammable objects that aren\'t being worn or carried. If you choose, plant life in the area is unaffected by this spell.',
        'level': 7,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'forcecage': {
        'description': 'An immobile, invisible, cube-shaped prison composed of magical force springs into existence around an area you choose within range. The prison can be a cage or a solid box as you choose.\n\nA prison in the shape of a cage can be up to 20 feet on a side and is made from 1/2-inch diameter bars spaced 1/2 inch apart.\n\nA prison in the shape of a box can be up to 10 feet on a side, creating a solid barrier that prevents any matter from passing through it and blocking any spells cast into or out from the area.\n\nWhen you cast the spell, any creature that is completely inside the cage\'s area is trapped. Creatures only partially within the area, or those too large to fit inside the area, are pushed away from the center of the area until they are completely outside the area.\n\nA creature inside the cage can\'t leave it by nonmagical means. If the creature tries to use teleportation or interplanar travel to leave the cage, it must first make a Charisma Saving Throw. On a success, the creature can use that magic to exit the cage. On a failure, the creature can\'t exit the cage and wastes the use of the spell or effect. The cage also extends into the Ethereal Plane, blocking ethereal travel.\n\nThis spell can\'t be dispelled by dispel magic.',
        'level': 7,
        'casting_time': '1 action',
        'range': '100 feet',
        'components': 'V, S, M',
        'duration': '1 hour',
        'school': 'Evocation',


    },
    'mirage arcane': {
        'description': 'You make terrain in an area up to 1 mile square look, sound, smell, and even feel like some other sort of terrain. The terrain\'s general shape remains the same, however. Open fields or a road could be made to resemble a swamp, hill, crevasse, or some other difficult or impassable terrain. A pond can be made to seem like a grassy meadow, a precipice like a gentle slope, or a rock-strewn gully like a wide and smooth road.\n\nSimilarly, you can alter the appearance of structures, or add them where none are present. The spell doesn\'t disguise, conceal, or add creatures.\n\nThe illusion includes audible, visual, tactile, and olfactory elements, so it can turn clear ground into difficult terrain (or vice versa) or otherwise impede movement through the area. Any piece of the illusory terrain (such as a rock or stick) that is removed from the spell\'s area disappears immediately.\n\nCreatures with truesight can see through the illusion to the terrain\'s true form; however, all other elements of the illusion remain, so while the creature is aware of the illusion\'s presence, the creature can still physically interact with the illusion.',
        'level': 7,
        'casting_time': '10 minutes',
        'range': 'Sight',
        'components': 'V, S',
        'duration': '10 days',
        'school': 'Illusion',


    },
    'mordenkainen\'s magnificent mansion': {
        'description': 'You conjure an extradimensional dwelling in range that lasts for the duration. You choose where its one entrance is located. The entrance shimmers faintly and is 5 feet wide and 10 feet tall. You and any creature you designate when you cast the spell can enter the extradimensional dwelling as long as the portal remains open. You can open or close the portal if you are within 30 feet of it. While closed, the portal is invisible.\n\nBeyond the portal is a magnificent foyer with numerous chambers beyond. The atmosphere is clean, fresh, and warm.\n\nYou can create any floor plan you like, but the space can\'t exceed 50 cubes, each cube being 10 feet on each side. The place is furnished and decorated as you choose. It contains sufficient food to serve a nine course banquet for up to 100 people. A staff of 100 near-transparent servants attends all who enter. You decide the visual appearance of these servants and their attire. They are completely obedient to your orders. Each servant can perform any task a normal Human servant could perform, but they can\'t attack or take any action that would directly harm another creature. Thus the servants can fetch things, clean, mend, fold clothes, light fires, serve food, pour wine, and so on. The servants can go anywhere in the mansion but can\'t leave it. Furnishings and other objects created by this spell dissipate into smoke if removed from the mansion. When the spell ends, any creatures inside the extradimensional space are expelled into the open spaces nearest to the entrance.',
        'level': 7,
        'casting_time': '1 minute',
        'range': '300 feet',
        'components': 'V, S, M',
        'duration': '24 hours',
        'school': 'Conjuration',


    },
    'mordenkainen\'s sword': {
        'description': 'You create a sword-shaped plane of force that hovers within range. It lasts for the duration.\n\nWhen the sword appears, you make a Melee Spell Attack against a target of your choice within 5 feet of the sword. On a hit, the target takes 3d10 force damage. Until the spell ends, you can use a bonus action on each of your turns to move the sword up to 20 feet to a spot you can see and repeat this attack against the same target or a different one.',
        'level': 7,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'plane shift': {
        'description': 'You and up to eight willing creatures who link hands in a circle are transported to a different plane of existence. You can specify a target destination in general terms, such as the City of Brass on the Elemental Plane of Fire or the palace of Dispater on the second level of the Nine Hells, and you appear in or near that destination. If you are trying to reach the City of Brass, for example, you might arrive in its Street of Steel, before its Gate of Ashes, or looking at the city from across the Sea of Fire, at the DM\'s discretion.\n\nAlternatively, if you know the sigil sequence of a teleportation circle on another plane of existence, this spell can take you to that circle. If the teleportation circle is too small to hold all the creatures you transported, they appear in the closest unoccupied spaces next to the circle.\n\nYou can use this spell to banish an unwilling creature to another plane. Choose a creature within your reach and make a Melee Spell Attack against it. On a hit, the creature must make a Charisma Saving Throw. If the creature fails this save, it is transported to a random location on the plane of existence you specify. A creature so transported must find its own way back to your current plane of existence.',
        'level': 7,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'power word pain': {
        'description': 'You speak a word of power that causes waves of intense pain to assail one creature you can see within range. If the target has 100 hit points or fewer, it is subject to crippling pain. Otherwise, the spell has no effect on it. A target is also unaffected if it is immune to being charmed.\n\nWhile the target is affected by crippling pain, any speed it has can be no higher than 10 feet. The target also has disadvantage on Attack Rolls, Ability Checks, and Saving Throws, other than Constitution Saving Throws. Finally, if the target tries to cast a spell, it must first succeed on a Constitution Saving Throw, or the casting fails and the spell is wasted.\n\nA target suffering this pain can make a Constitution Saving Throw at the end of each of its turns. On a successful save, the pain ends.',
        'level': 7,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Enchantment',


    },
    'prismatic spray': {
        'description': 'Eight multicolored rays of light flash from your hand. Each ray is a different color and has a different power and purpose. Each creature in a 60-foot cone must make a Dexterity Saving Throw. For each target, roll a d8 to determine which color ray affects it.\n\n1-Red\nThe target takes 10d6 fire damage on a failed save, or half as much damage on a successful one.\n\n2-Orange\nThe target takes 10d6 acid damage on a failed save, or half as much damage on a successful one.\n\n3-Yellow\nThe target takes 10d6 lightning damage on a failed save, or half as much damage on a successful one.\n\n4-Green\nThe target takes 10d6 poison damage on a failed save, or half as much damage on a successful one.\n\n5-Blue\nThe target takes 10d6 cold damage on a failed save, or half as much damage on a successful one.\n\n6-Indigo\nOn a failed save, the target is restrained. It must then make a Constitution Saving Throw at the end of each of its turns. If it successfully saves three times, the spell ends. If it fails its save three times, it permanently turns to stone and is subjected to the petrified condition. The successes and failures don\'t need to be consecutive, keep track of both until the target collects three of a kind.\n\n7-Violet\nOn a failed save, the target is blinded. It must then make a Wisdom Saving Throw at the start of your next turn. A successful save ends the blindness. If it fails that save, the creature is transported to another plane of existence of the DM\'s choosing and is no longer blinded. (Typically, a creature that is on a plane that isn\'t its home plane is banished home, while other creatures are usually cast into the Astral or Ethereal planes.)\n\n8-Special\nThe target is struck by two rays. Roll twice more, rerolling any 8.',
        'level': 7,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'project image': {
        'description': 'You create an illusory copy of yourself that lasts for the duration. The copy can appear at any location within range that you have seen before, regardless of intervening obstacles. The illusion looks and sounds like you but is intangible. If the illusion takes any damage, it disappears, and the spell ends.\n\nYou can use your action to move this illusion up to twice your speed, and make it gesture, speak, and behave in whatever way you choose. It mimics your mannerisms perfectly.\n\nYou can see through its eyes and hear through its ears as if you were in its space. On your turn as a bonus action, you can switch from using its senses to using your own, or back again. While you are using its senses, you are blinded and deafened in regard to your own surroundings.\n\nPhysical interaction with the image reveals it to be an illusion, because things can pass through it. A creature that uses its action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your Spell Save DC. If a creature discerns the illusion for what it is, the creature can see through the image, and any noise it makes sounds hollow to the creature.',
        'level': 7,
        'casting_time': '1 action',
        'range': '500 miles',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 1 day',
        'school': 'Illusion',
        'concentration': True,

    },
    'regenerate': {
        'description': 'You touch a creature and stimulate its natural healing ability. The target regains 4d8 + 15 hit points. For the duration of the spell, the target regains 1 hit point at the start of each of its turns (10 hit points each minute).\n\nThe target\'s severed body members (fingers, legs, tails, and so on), if any, are restored after 2 minutes. If you have the severed part and hold it to the stump, the spell instantaneously causes the limb to knit to the stump.',
        'level': 7,
        'casting_time': '1 minute',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Transmutation',


    },
    'resurrection': {
        'description': 'You touch a dead creature that has been dead for no more than a century, that didn\'t die of old age, and that isn\'t undead. If its soul is free and willing, the target returns to life with all its hit points.\n\nThis spell neutralizes any poisons and cures normal diseases afflicting the creature when it died. It doesn\'t, however, remove magical diseases, curses, and the like; if such effects aren\'t removed prior to casting the spell, they afflict the target on its return to life.\n\nThis spell closes all mortal wounds and restores any missing body parts.\n\nComing back from the dead is an ordeal. The target takes a -4 penalty to all Attack Rolls, Saving Throws, and Ability Checks. Every time the target finishes a long rest, the penalty is reduced by 1 until it disappears.\n\nCasting this spell to restore life to a creature that has been dead for one year or longer taxes you greatly. Until you finish a long rest, you can\'t cast spells again, and you have disadvantage on all Attack Rolls, Ability Checks, and Saving Throws.',
        'level': 7,
        'casting_time': '1 hour',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Necromancy',


    },
    'reverse gravity': {
        'description': 'This spell reverses gravity in a 50-foot-radius, 100-foot high cylinder centered on a point within range. All creatures and objects that aren\'t somehow anchored to the ground in the area fall upward and reach the top of the area when you cast this spell. A creature can make a Dexterity Saving Throw to grab onto a fixed object it can reach, thus avoiding the fall.\n\nIf some solid object (such as a ceiling) is encountered in this fall, falling objects and creatures strike it just as they would during a normal downward fall. If an object or creature reaches the top of the area without striking anything, it remains there, oscillating slightly, for the duration.\n\nAt the end of the duration, affected objects and creatures fall back down.',
        'level': 7,
        'casting_time': '1 action',
        'range': '100 feet',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'sequester': {
        'description': 'By means of this spell, a willing creature or an object can be hidden away, safe from detection for the duration. When you cast the spell and touch the target, it becomes invisible and can\'t be targeted by divination spells or perceived through scrying sensors created by divination spells.\n\nIf the target is a creature, it falls into a state of suspended animation. Time ceases to flow for it, and it doesn\'t grow older.\n\nYou can set a condition for the spell to end early. The condition can be anything you choose, but it must occur or be visible within 1 mile of the target. Examples include "after 1,000 years" or "when the tarrasque awakens." This spell also ends if the target takes any damage.',
        'level': 7,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Until dispelled',
        'school': 'Transmutation',


    },
    'simulacrum': {
        'description': 'You shape an illusory duplicate of one beast or humanoid that is within range for the entire casting time of the spell. The duplicate is a creature, partially real and formed from ice or snow, and it can take actions and otherwise be affected as a normal creature. It appears to be the same as the original, but it has half the creature\'s hit point maximum and is formed without any equipment. Otherwise, the illusion uses all the statistics of the creature it duplicates, except that it is a construct.\n\nThe simulacrum is friendly to you and creatures you designate. It obeys your spoken commands, moving and acting in accordance with your wishes and acting on your turn in combat. The simulacrum lacks the ability to learn or become more powerful, so it never increases its level or other abilities, nor can it regain expended spell slots.If the simulacrum is damaged, you can repair it in an alchemical laboratory, using rare herbs and minerals worth 100 gp per hit point it regains. The simulacrum lasts until it drops to 0 hit points, at which point it reverts to snow and melts instantly.\n\nIf you cast this spell again, any currently active duplicates you created with this spell are instantly destroyed.',
        'level': 7,
        'casting_time': '12 hours',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Until dispelled',
        'school': 'Illusion',


    },
    'symbol': {
        'description': 'When you cast this spell, you inscribe a harmful glyph either on a surface (such as a section of floor, a wall, or a table) or within an object that can be closed to conceal the glyph (such as a book, a scroll, or a treasure chest). If you choose a surface, the glyph can cover an area of the surface no larger than 10 feet in diameter. If you choose an object, that object must remain in its place; if the object is moved more than 10 feet from where you cast this spell, the glyph is broken, and the spell ends without being triggered.\n\nThe glyph is nearly invisible, requiring an Intelligence (Investigation) check against your Spell Save DC to find it.\n\nYou decide what triggers the glyph when you cast the spell. For glyphs inscribed on a surface, the most typical triggers include touching or stepping on the glyph, removing another object covering it, approaching within a certain distance of it, or manipulating the object that holds it. For glyphs inscribed within an object, the most common triggers are opening the object, approaching within a certain distance of it, or seeing or reading the glyph.\n\nYou can further refine the trigger so the spell is activated only under certain circumstances or according to a creature\'s physical characteristics (such as height or weight), or physical kind (for example, the ward could be set to affect hags or shapechangers). You can also specify creatures that don\'t trigger the glyph, such as those who say a certain password.When you inscribe the glyph, choose one of the options below for its effect. Once triggered, the glyph glows, filling a 60-foot-radius sphere with dim light for 10 minutes, after which time the spell ends. Each creature in the sphere when the glyph activates is targeted by its effect, as is a creature that enters the sphere for the first time on a turn or ends its turn there.\n\nDeath\nEach target must make a Constitution Saving Throw, taking 10d10 necrotic damage on a failed save, or half as much damage on a successful save.\n\nDiscord\nEach target must make a Constitution Saving Throw. On a failed save, a target bickers and argues with other creatures for 1 minute. During this time, it is incapable of meaningful communication and has disadvantage on Attack Rolls and Ability Checks.\n\nFear\nEach target must make a Wisdom Saving Throw and becomes frightened for 1 minute on a failed save. While frightened, the target drops whatever it is holding and must move at least 30 feet away from the glyph on each of its turns, if able.\n\nHopelessness\nEach target must make a Charisma Saving Throw. On a failed save, the target is overwhelmed with despair for 1 minute. During this time, it can\'t attack or target any creature with harmful abilities, spells, or other magical effects.\n\nInsantity\nEach target must make an Intelligence Saving Throw. On a failed save, the target is driven insane for 1 minute. An insane creature can\'t take actions, can\'t understand what other creatures say, can\'t read, and speaks only in gibberish. The DM controls its movement, which is erratic.\n\nPain\nEach target must make a Constitution Saving Throw and becomes incapacitated with excruciating pain for 1 minute on a failed save.\n\nSleep\nEach target must make a Wisdom Saving Throw and falls unconscious for 10 minutes on a failed save. A creature awakens if it takes damage or if someone uses an action to shake or slap it awake.\n\nStunning\nEach target must make a Wisdom Saving Throw and becomes stunned for 1 minute on a failed save.',
        'level': 7,
        'casting_time': '1 minute',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Until dispelled or triggered',
        'school': 'Abjuration',


    },
    'teleport': {
        'description': 'This spell instantly transports you and up to eight willing creatures of your choice that you can see within range, or a single object that you can see within range, to a destination you select. If you target an object, it must be able to fit entirely inside a 10-foot cube, and it can\'t be held or carried by an unwilling creature.\n\nThe destination you choose must be known to you, and it must be on the same plane of existence as you. Your familiarity with the destination determines whether you arrive there successfully. The DM rolls d100 and consults the table.\n\nTeleportation\n\n╔═══════════════════╤════════╤══════════════╤════════════╤═══════════╗\n║ Familiarity       │ Mishap │ Similar Area │ Off Target │ On Target ║\n╠═══════════════════╪════════╪══════════════╪════════════╪═══════════╣\n║ Permanent circle  │ --     │ --           │ --         │ 01-100    ║\n╟───────────────────┼────────┼──────────────┼────────────┼───────────╢\n║ Associated object │ --     │ --           │ --         │ 01-100    ║\n╟───────────────────┼────────┼──────────────┼────────────┼───────────╢\n║ Very familiar     │ 01-05  │ 06-13        │ 14-24      │ 25-100    ║\n╟───────────────────┼────────┼──────────────┼────────────┼───────────╢\n║ Seen casually     │ 01-33  │ 34-43        │ 44-53      │ 54-100    ║\n╟───────────────────┼────────┼──────────────┼────────────┼───────────╢\n║ Viewed once       │ 01-43  │ 44-53        │ 54-73      │ 74-100    ║\n╟───────────────────┼────────┼──────────────┼────────────┼───────────╢\n║ Description       │ 01-43  │ 44-53        │ 54-73      │ 74-100    ║\n╟───────────────────┼────────┼──────────────┼────────────┼───────────╢\n║ False destination │ 01-50  │ 51-100       │ --         │ --        ║\n╚═══════════════════╧════════╧══════════════╧════════════╧═══════════╝\n\nFamiliarity\n"Permanent circle" means a permanent teleportation circle whose sigil sequence you know. "Associated object" means that you possess an object taken from the desired destination within the last six months, such as a book from a wizard\'s library, bed linen from a royal suite, or a chunk of marble from a lich\'s secret tomb.\n\n"Very familiar" is a place you have been very often, a place you have carefully studied, or a place you can see when you cast the spell. "Seen casually" is someplace you have seen more than once but with which you aren\'t very familiar. "Viewed once" is a place you have seen once, possibly using magic. "Description" is a place whose location and appearance you know through someone else\'s description, perhaps from a map.\n\n"False destination" is a place that doesn\'t exist. Perhaps you tried to scry an enemy\'s sanctum but instead viewed an illusion, or you are attempting to teleport to a familiar location that no longer exists.\n\nOn Target\nYou and your group (or the target object) appear where you want to.\n\nOff Target\nYou and your group (or the target object) appear a random distance away from the destination in a random direction. Distance off target is 1d10 x 1d10 percent of the distance that was to be traveled. For example, if you tried to travel 120 miles, landed off target, and rolled a 5 and 3 on the two d10s, then you would be off target by 15%, or 18 miles. The DM determines the direction off target randomly by rolling a d8 and designating 1 as north, 2 as northeast, 3 as east, and so on around the points of the compass. If you were teleporting to a coastal city and wound up 18 miles out at sea, you could be in trouble.\n\nSimilar Area\nYou and your group (or the target object) wind up in a different area that\'s visually or thematically similar to the target area. If you are heading for your home laboratory, for example, you might wind up in another wizard\'s laboratory or in an alchemical supply shop that has many of the same tools and implements as your laboratory. Generally, you appear in the closest similar place, but since the spell has no range limit, you could conceivably wind up anywhere on the plane.\n\nMishap\nThe spell\'s unpredictable magic results in a difficult journey. Each teleporting creature (or the target object) takes 3d10 force damage, and the DM rerolls on the table to see where you wind up (multiple mishaps can occur, dealing damage each time).',
        'level': 7,
        'casting_time': '1 action',
        'range': '10 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'temple of the gods': {
        'description': 'You cause a temple to shimmer into existence on ground you can see within range. The temple must fit within an unoccupied cube of space, up to 120 feet on each side. The temple remains until the spell ends. It is dedicated to whatever god, pantheon, or philosophy is represented by the holy symbol used in the casting.\n\nYou make all decisions about the temple\'s appearance. The interior is enclosed by a floor, walls, and a roof, with one door granting access to the interior and as many windows as you wish. Only you and any creatures you designate when you cast the spell can open or close the door.\n\nThe temple\'s interior is an open space with an idol or altar at one end. You decide whether the temple is illuminated and whether that illumination is bright light or dim light. The smell of burning incense fills the air within, and the temperature is mild.\n\nThe temple opposes types of creatures you choose when you cast this spell. Choose one or more of the following: celestials, elementals, fey, fiends, or undead. If a creature of the chosen type attempts to enter the temple, that creature must make a Charisma Saving Throw. On a failed save, it can\'t enter the temple for 24 hours. Even if the creature can enter the temple, the magic there hinders it; whenever it makes an Attack Roll, an Ability Check, or a Saving Throw inside the temple, it must roll a d4 and subtract the number rolled from the d20 roll.\n\nIn addition, the sensors created by divination spells can\'t appear inside the temple, and creatures within can\'t be targeted by divination spells.\n\nFinally, whenever any creature in the temple regains hit points from a spell of 1st level or higher, the creature regains additional hit points equal to your Wisdom Modifier (minimum 1 hit point).\n\nThe temple is made from opaque magical force that extends into the Ethereal Plane, thus blocking ethereal travel into the temple\'s interior. Nothing can physically pass through the temple\'s exterior. It can\'t be dispelled by dispel magic, and antimagic field has no effect on it. A disintegrate spell destroys the temple instantly.\n\nCasting this spell on the same spot every day for a year makes this effect permanent.',
        'level': 7,
        'casting_time': '1 hour',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'whirlwind': {
        'description': 'A whirlwind howls down to a point that you can see on the ground within range. The whirlwind is a 10-foot-radius, 30-foot-high cylinder centered on that point. Until the spell ends, you can use your action to move the whirlwind up to 30 feet in any direction along the ground. The whirlwind sucks up any medium or smaller objects that aren\'t secured to anything and that aren\'t worn or carried by anyone.\n\nA whirlwind howls down to a point that you can see on the ground within range. The whirlwind is a 10-foot-radius, 30-foot-high cylinder centered on that point. Until the spell ends, you can use your action to move the whirlwind up to 30 feet in any direction along the ground. The whirlwind sucks up any medium or smaller objects that aren\'t secured to anything and that aren\'t worn or carried by anyone.A restrained creature can use an action to make a Strength or Dexterity Check against your Spell Save DC. If successful, the creature is no longer restrained by the whirlwind and is hurled 3d6 × 10 feet away from it in a random direction.',
        'level': 7,
        'casting_time': '1 action',
        'range': '300 feet',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    }
}
