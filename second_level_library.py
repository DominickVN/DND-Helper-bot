second_level_spells = {
    'aganazzar\'s scorcher': {
        'description': 'A line of roaring flame 30 feet long and 5 feet wide emanates from you in a direction you choose. Each creature in the line must make a Dexterity Saving Throw. A creature takes 3d8 fire damage on a failed save, or half as much damage on a successful one. \n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.',
        'level': '2nd level',
        'casting_time': '1 action',
        'range': 'Self (15-foot cone)',
        'components': 'V, S, M (a red dragon\'s scale)',
        'duration': 'Instantaneous',
        'school': 'Evocation',

    },
    'aid': {
        'description': 'Your spell bolsters your allies with toughness and resolve. Choose up to three creatures within range. Each target\'s hit point maximum and current hit points increase by 5 for the duration.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, a target\'s hit points increase by an additional 5 for each slot level above 2nd.',
        'level': '2nd level',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a tiny strip of white cloth)',
        'duration': '8 hours',
        'school': 'Abjuration',

    },
    'alter self': {
        'description': 'You assume a different form. When you cast the spell, choose one of the following options, the effects of which last for the duration of the spell. While the spell lasts, you can end one option as an action to gain the benefits of a different one.\n\nAquatic Adaptation\n\nYou adapt your body to an aquatic environment, sprouting gills and growing webbing between your fingers. You can breathe underwater and gain a swimming speed equal to your walking speed.\n\nChange Appearance\n\nYou transform your appearance. You decide what you look like, including your height, weight, facial features, sound of your voice, hair length, coloration, and distinguishing characteristics, if any. You can make yourself appear as a member of another race, though none of your statistics change. You also can\'t appear as a creature of a different size than you, and your basic shape stays the same; if you\'re bipedal, you can\'t use this spell to become quadrupedal, for instance. At any time for the duration of the spell, you can use your action to change your appearance in this way again.\n\nNatural Weapons\n\nYou grow claws, fangs, spines, horns, or a different natural weapon of your choice. Your unarmed strikes deal 1d6 bludgeoning, piercing, or slashing damage, as appropriate to the natural weapon you chose, and you are proficient with your unarmed strikes. Finally, the natural weapon is magic and you have a +1 bonus to the Attack & Damage Rolls you make using it.',
        'level': '2nd level',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Transmutation',

    },
    'animal messenger': {
        'description': 'By means of this spell, you use an animal to deliver a message. Choose a tiny beast you can see within range, such as a squirrel, a blue jay, or a bat. You specify a location, which you must have visited, and a recipient who matches a general description, such as "a man or woman dressed in the uniform of the town guard" or "a red-haired dwarf wearing a pointed hat." You also speak a message of up to twenty-five words. The target beast travels for the duration of the spell toward the specified location, covering about 50 miles per 24 hours for a flying messenger, or 25 miles for other animals.\n\nWhen the messenger arrives, it delivers your message to the creature that you described, replicating the sound of your voice. The messenger speaks only to a creature matching the description you gave. If the messenger doesn\'t reach its destination before the spell ends, the message is lost, and the beast makes its way back to where you cast this spell.\n\nIf you cast this spell using a spell slot of 3rd level or higher, the duration of the spell increases by 48 hours for each slot level above 2nd.',
        'level': '2nd level',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a morsel of food)',
        'duration': '24 hours',
        'school': 'Enchantment',
        'ritual': True

    },
    'arcane lock': {
        'description': 'You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration. You and the creatures you designate when you cast this spell can open the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this spell for 1 minute. Otherwise, it is impassable until it is broken or the spell is dispelled or suppressed. Casting knock on the object suppresses arcane lock for 10 minutes.\n\nWhile affected by this spell, the object is more difficult to break or force open; the DC to break it or pick any locks on it increases by 10.',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (gold dust worth at least 25 gp, which the spell consumes)',
        'duration': 'Until dispelled',
        'school': 'Abjuration',

    },
    'augury': {
        'description': 'By casting gem-inlaid sticks, rolling dragon bones, laying out ornate cards, or employing some other divining tool, you receive an omen from an otherworldly entity about the results of a specific course of action that you plan to take within the next 30 minutes. The DM chooses from the following possible omens:\n\n•Weal, for good results\n•Woe, for bad results\n•Weal and woe, for both good and bad results\n•Nothing, for results that aren\'t especially good or bad\n\nThe spell doesn\'t take into account any possible circumstances that might change the outcome, such as the casting of additional spells or the loss or gain of a companion.\n\nIf you cast the spell two or more times before completing your next long rest, there is a cumulative 25% chance for each casting after the first that you get a random reading. The DM makes this roll in secret.',
        'level': '2nd level',
        'casting_time': '1 minute',
        'range': 'Self',
        'components': 'V, S, M (specially marked sticks, bones, or similar tokens worth at least 25 gp)',
        'duration': 'Instantaneous',
        'school': 'Divination',
        'ritual': True

    },
    'barkskin': {
        'description': 'You touch a willing creature. Until the spell ends, the target\'s skin has a rough, bark-like appearance, and the target\'s AC can\'t be less than 16, regardless of what kind of armor it is wearing.',
        'level': '2nd level',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a handful of oak bark)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Transmutation',
        'concentration': True,

    },
    'beast sense': {
        'description': 'You touch a willing beast. For the duration of the spell, you can use your action to see through the beast\'s eyes and hear what it hears, and continue to do so until you use your action to return to your normal senses. While perceiving through the beast\'s senses, you gain the benefits of any special senses possessed by that creature, though you are blinded and deafened to your own surroundings.',
        'level': '2nd level',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'S',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Divination',
        'concentration': True,
        'ritual': True
    },
    'blindness/deafness': {
        'description': 'You can blind or deafen a foe. Choose one creature that you can see within range to make a Constitution Saving Throw. If it fails, the target is either blinded or deafened (your choice) for the duration. At the end of each of its turns, the target can make a Constitution Saving Throw. On a success, the spell ends.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.',
        'level': '2nd level',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V',
        'duration': '1 minute',
        'school': 'Necromancy',

    },
    'blur': {
        'description': 'Your body becomes blurred, shifting and wavering to all who can see you. For the duration, any creature has disadvantage on Attack Rolls against you. An attacker is immune to this effect if it doesn\'t rely on sight, as with blindsight, or can see through illusions, as with truesight.',
        'level': '2nd level',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Illusion',
        'concentration': True,

    },
    'branding smite': {
        'description': 'The next time you hit a creature with a Weapon Attack before this spell ends, the weapon gleams with astral radiance as you strike. The attack deals an extra 2d6 radiant damage to the target, which becomes visible if it\'s invisible, and the target sheds dim light in a 5-foot radius and can\'t become invisible until the spell ends.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the extra damage increases by 1d6 for each slot level above 2nd.',
        'level': '2nd level',
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'calm emotions': {
        'description': 'You attempt to suppress strong emotions in a group of people. Each humanoid in a 20-foot-radius sphere centered on a point you choose within range must make a Charisma Saving Throw; a creature can choose to fail this Saving Throw if it wishes. If a creature fails its Saving Throw, choose one of the following two effects.\n\nYou can suppress any effect causing a target to be charmed or frightened. When this spell ends, any suppressed effect resumes, provided that its duration has not expired in the meantime.\n\nAlternatively, you can make a target indifferent about creatures of your choice that it is hostile toward. This indifference ends if the target is attacked or harmed by a spell or if it witnesses any of its friends being harmed. When the spell ends, the creature becomes hostile again, unless the DM rules otherwise.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'cloud of daggers': {
        'description': 'You fill the air with spinning daggers in a cube 5 feet on each side, centered on a point you choose within range. A creature takes 4d4 slashing damage when it enters the spell\'s area for the first time on a turn or starts its turn there.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 2d4 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a sliver of glass)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

    },
    'continual flame': {
        'description': 'A flame, equivalent in brightness to a torch, springs forth from an object that you touch. The effect looks like a regular flame, but it creates no heat and doesn\'t use oxygen. A continual flame can be covered or hidden but not smothered or quenched.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (ruby dust worth 50 gp, which the spell consumes)',
        'duration': 'Until dispelled',
        'school': 'Evocation',


    },
    'cordon of arrows': {
        'description': 'You plant four pieces of nonmagical ammunition—arrows or crossbow bolts—in the ground within range and lay magic upon them to protect an area. Until the spell ends, whenever a creature other than you comes within 30 feet of the ammunition for the first time on a turn or ends its turn there, one piece of ammunition flies up to strike it. The creature must succeed on a Dexterity Saving Throw or take 1d6 piercing damage. The piece of ammunition is then destroyed. The spell ends when no ammunition remains.\n\nWhen you cast this spell, you can designate any creatures you choose, and the spell ignores them.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the amount of ammunition that can be affected increases by two for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 minute',
        'range': '5 feet',
        'components': 'V, S, M (four or more arrows or bolts)',
        'duration': '8 hours',
        'school': 'Abjuration',


    },
    'crown of madness': {
        'description': 'One humanoid of your choice that you can see within range must succeed on a Wisdom Saving Throw or become charmed by you for the duration. While the target is charmed in this way, a twisted crown of jagged iron appears on its head, and a madness glows in its eyes.\n\nThe charmed target must use its action before moving on each of its turns to make a Melee Attack against a creature other than itself that you mentally choose. The target can act normally on its turn if you choose no creature or if none are within its reach.\n\nOn your subsequent turns, you must use your action to maintain control over the target, or the spell ends. Also, the target can make a Wisdom Saving Throw at the end of each of its turns. On a success, the spell ends.',
        'level': 2,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'darkness': {
        'description': 'Magical darkness spreads from a point you choose within range to fill a 15-foot-radius sphere for the duration. The darkness spreads around corners. A creature with darkvision can\'t see through this darkness, and nonmagical light can\'t illuminate it.\n\nIf the point you choose is on an object you are holding or one that isn\'t being worn or carried, the darkness emanates from the object and moves with it. Completely covering the source of the darkness with an opaque object, such as a bowl or a helm, blocks the darkness.\n\nIf any of this spell\'s area overlaps with an area of light created by a spell of 2nd level or lower, the spell that created the light is dispelled.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, M (bat fur and a drop of pitch or piece of coal)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

    },
    'darkvision': {
        'description': 'If any of this spell\'s area overlaps with an area of light created by a spell of 2nd level or lower, the spell that created the light is dispelled.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (either a pinch of dried carrot or an agate)',
        'duration': '8 hours',
        'school': 'Transmutation',


    },
    'detect thoughts': {
        'description': 'For the duration, you can read the thoughts of certain creatures. When you cast the spell and as your action on each turn until the spell ends, you can focus your mind on any one creature that you can see within 30 feet of you. If the creature you choose has an Intelligence of 3 or lower or doesn\'t speak any language, the creature is unaffected.\n\nYou initially learn the surface thoughts of the creature—what is most on its mind in that moment. As an action, you can either shift your attention to another creature\'s thoughts or attempt to probe deeper into the same creature\'s mind. If you probe deeper, the target must make a Wisdom Saving Throw. If it fails, you gain insight into its reasoning (if any), its emotional state, and something that looms large in its mind (such as something it worries over, loves, or hates). If it succeeds, the spell ends. Either way, the target knows that you are probing into its mind, and unless you shift your attention to another creature\'s thoughts, the creature can use its action on its turn to make an Intelligence Check contested by your Intelligence Check; if it succeeds, the spell ends.\n\nQuestions verbally directed at the target creature naturally shape the course of its thoughts, so this spell is particularly effective as part of an interrogation.\n\nYou can also use this spell to detect the presence of thinking creatures you can\'t see. When you cast the spell or as your action during the duration, you can search for thoughts within 30 feet of you. The spell can penetrate barriers, but 2 feet of rock, 2 inches of any metal other than lead, or a thin sheet of lead blocks you. You can\'t detect a creature with an Intelligence of 3 or lower or one that doesn\'t speak any language.\n\nOnce you detect the presence of a creature in this way, you can read its thoughts for the rest of the duration as described above, even if you can\'t see it, but it must still be within range.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (a copper piece)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Divination',
        'concentration': True,

    },
    'dragon\'s breath': {
        'description': 'You touch one willing creature and imbue it with the power to spew magical energy from its mouth, provided it has one. Choose acid, cold, fire, lightning, or poison. Until the spell ends, the creature can use an action to exhale energy of the chosen type in a 15-foot cone. Each creature in that area must make a Dexterity Saving Throw, taking 3d6 damage of the chosen type on a failed save, or half as much damage on a successful one.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d6 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 bonus action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'dust devil': {
        'description': 'Choose an unoccupied 5-foot cube of air that you can see within range. An elemental force that resembles a dust devil appears in the cube and lasts for the spell\'s duration.\n\nAny creature that ends its turn within 5 feet of the dust devil must make a Strength Saving Throw. On a failed save, the creature takes 1d8 bludgeoning damage and is pushed 10 feet away from the dust devil. On a successful save, the creature takes half as much damage and isn\'t pushed.\n\nAs a bonus action, you can move the dust devil up to 30 feet in any direction. If the dust devil moves over sand, dust, loose dirt, or light gravel, it sucks up the material and forms a 10-foot-radius cloud of debris around itself that lasts until the start of your next turn. The cloud heavily obscures its area.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a pinch of dust)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

    },
    'earth bind': {
        'description': 'Choose one creature you can see within range. Yellow strips of magical energy loop around the creature. The target must succeed on a Strength Saving Throw, or its flying speed (if any) is reduced to 0 feet for the spell\'s duration. An airborne creature affected by this spell safely descends at 60 feet per round until it reaches the ground or the spell ends.',
        'level': 2,
        'casting_time': '1 action',
        'range': '300 feet',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'enhance ability': {
        'description': 'You touch a creature and bestow upon it a magical enhancement. Choose one of the following effects; the target gains that effect until the spell ends.\n\nBear\'s Endurance\n•The target has advantage on Constitution Checks. It also gains 2d6 temporary hit points, which are lost when the spell ends.\n\nBull\'s Strength\n•The target has advantage on Strength Checks, and his or her carrying capacity doubles.\n\nCat\'s Grace\n•The target has advantage on Dexterity Checks. It also doesn\'t take damage from falling 20 feet or less if it isn\'t incapacitated.\n\nEagle\'s Splendor\n•The target has advantage on Charisma Checks.\n\nFox\'s Cunning\n•The target has advantage on Intelligence Checks.\n\nOwl\'s Wisdom\n•The target has advantage on Wisdom Checks.\n\n\nWhen you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (fur or a feather from a beast)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Transmutation',
        'concentration': True,

    },
    'enlarge/reduce': {
        'description': 'You cause a creature or an object you can see within range to grow larger or smaller for the duration. Choose either a creature or an object that is neither worn nor carried. If the target is unwilling, it can make a Constitution Saving Throw. On a success, the spell has no effect.\n\nIf the target is a creature, everything it is wearing and carrying changes size with it. Any item dropped by an affected creature returns to normal size at once.\n\n\nEnlarge\n\nThe target\'s size doubles in all dimensions, and its weight is multiplied by eight. This growth increases its size by one category—from medium to large, for example. If there isn\'t enough room for the target to double its size, the creature or object attains the maximum possible size in the space available. Until the spell ends, the target also has advantage on Strength Checks and Strength Saving Throws. The target\'s weapons also grow to match its new size. While these weapons are enlarged, the target\'s attacks with them deal 1d4 extra damage.\n\n\nReduce\n\nThe target\'s size is halved in all dimensions, and its weight is reduced to one-eighth of normal. This reduction decreases its size by one category—from medium to small, for example. Until the spell ends, the target also has disadvantage on Strength Checks and Strength Saving Throws. The target\'s weapons also shrink to match its new size. While these weapons are reduced, the target\'s attacks with them deal 1d4 less damage (this can\'t reduce the damage below 1).',
        'level': 2,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a pinch of powdered iron)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'enthrall': {
        'description': 'You weave a distracting string of words, causing creatures of your choice that you can see within range and that can hear you to make a Wisdom Saving Throw. Any creature that can\'t be charmed succeeds on this Saving Throw automatically, and if you or your companions are fighting a creature, it has advantage on the save. On a failed save, the target has disadvantage on Wisdom (Perception) checks made to perceive any creature other than you until the spell ends or until the target can no longer hear you. The spell ends if you are incapacitated or can no longer speak.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': '1 minute',
        'school': 'Enchantment',


    },
    'find steed': {
        'description': 'You summon a spirit that assumes the form of an unusually intelligent, strong, and loyal steed, creating a long-lasting bond with it. Appearing in an unoccupied space within range, the steed takes on a form that you choose: a Warhorse, a Pony, a Camel, an Elk, or a Mastiff. (Your DM might allow other animals to be summoned as steeds.) The steed has the statistics of the chosen form, though it is a celestial, fey, or fiend (your choice) instead of its normal type. Additionally, if your steed has an Intelligence of 5 or less, its Intelligence becomes 6, and it gains the ability to understand one language of your choice that you speak.\n\nYour steed serves you as a mount, both in combat and out, and you have an instinctive bond with it that allows you to fight as a seamless unit. While mounted on your steed, you can make any spell you cast that targets only you also target your steed.\n\nWhen the steed drops to 0 hit points, it disappears, leaving behind no physical form. You can also dismiss your steed at any time as an action, causing it to disappear. In either case, casting this spell again summons the same steed, restored to its hit point maximum.\n\nWhile your steed is within 1 mile of you, you can communicate with each other telepathically.\n\nYou can\'t have more than one steed bonded by this spell at a time. As an action, you can release the steed from its bond at any time, causing it to disappear.',
        'level': 2,
        'casting_time': '10 minutes',
        'range': '30 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Conjuration',

        'ritual': True
    },
    'find traps': {
        'description': 'You sense the presence of any trap within range that is within line of sight. A trap, for the purpose of this spell, includes anything that would inflict a sudden or unexpected effect you consider harmful or undesirable, which was specifically intended as such by its creator. Thus, the spell would sense an area affected by the alarm spell, a glyph of warding, or a mechanical pit trap, but it would not reveal a natural weakness in the floor, an unstable ceiling, or a hidden sinkhole.\n\nThis spell merely reveals that a trap is present. You don\'t learn the location of each trap, but you do learn the general nature of the danger posed by a trap you sense.',
        'level': 2,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Divination',


    },
    'flame blade': {
        'description': 'You evoke a fiery blade in your free hand. The blade is similar in size and shape to a scimitar, and it lasts for the duration. If you let go of the blade, it disappears, but you can evoke the blade again as a bonus action.\n\nYou can use your action to make a Melee Spell Attack with the fiery blade. On a hit, the target takes 3d6 fire damage.\n\nThe flaming blade sheds bright light in a 10-foot radius and dim light for an additional 10 feet.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for every two slot levels above 2nd.',
        'level': 2,
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V, S, M (leaf of sumac)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

    },
    'flaming sphere': {
        'description': 'A 5-foot-diameter sphere of fire appears in an unoccupied space of your choice within range and lasts for the duration. Any creature that ends its turn within 5 feet of the sphere must make a Dexterity Saving Throw. The creature takes 2d6 fire damage on a failed save, or half as much damage on a successful one.\n\nAs a bonus action, you can move the sphere up to 30 feet. If you ram the sphere into a creature, that creature must make the Saving Throw against the sphere\'s damage, and the sphere stops moving this turn.\n\nWhen you move the sphere, you can direct it over barriers up to 5 feet tall and jump it across pits up to 10 feet wide. The sphere ignites flammable objects not being worn or carried, and it sheds bright light in a 20-foot radius and dim light for an additional 20 feet.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d6 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a bit of tallow, a pinch of brimstone, and a dusting of powdered iron)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

    },
    'flock of familiars': {
        'description': 'You temporarily summon three familiars—spirits that take animal forms of your choice. Each familiar uses the same rules and options for a familiar conjured by the find familiar spell. All the familiars conjured by this spell must be the same type of creature (celestials, fey, or fiends; your choice). If you already have a familiar conjured by the find familiar spell or similar means, then one fewer familiars are conjured by this spell.\n\nFamiliars summoned by this spell can telepathically communicate with you and share their visual or auditory senses while they are within 1 mile of you.\n\nWhen you cast a spell with a range of touch, one of the familiars conjured by this spell can deliver the spell, as normal. However, you can cast a touch spell through only one familiar per turn.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, you conjure an additional familiar for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Conjuration',


    },
    'gentle repose': {
        'description': 'You touch a corpse or other remains. For the duration, the target is protected from decay and can\'t become undead.\n\nThe spell also effectively extends the time limit on raising the target from the dead, since days spent under the influence of this spell don\'t count against the time limit of spells such as raise dead.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a pinch of salt and one copper piece placed on each of the corpse\'s eyes, which must remain there for the duration)',
        'duration': '10 days',
        'school': 'Necromancy',


    },
    'gust of wind': {
        'description': 'A line of strong wind 60 feet long and 10 feet wide blasts from you in a direction you choose for the spell\'s duration. Each creature that starts its turn in the line must succeed on a Strength Saving Throw or be pushed 15 feet away from you in a direction following the line.\n\nAny creature in the line must spend 2 feet of movement for every 1 foot it moves when moving closer to you.\n\nThe gust disperses gas or vapor, and it extinguishes candles, torches, and similar unprotected flames in the area. It causes protected flames, such as those of lanterns, to dance wildly and has a 50 perent chance to extinguish them.\n\nAs a bonus action on each of your turns before the spell ends, you can change the direction in which the line blasts from you.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Self (60-foot line)',
        'components': 'V, S, M (a legume seed)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'healing spirit': {
        'description': 'YYou call forth a nature spirit to soothe the wounded. The intangible spirit appears in a space that is a 5-foot cube you can see within range. The spirit looks like a transparent beast or fey (your choice).\n\nUntil the spell ends, whenever you or a creature you can see moves into the spirit\'s space for the first time on a turn or starts its turn there, you can cause the spirit to restore 1d6 hit points to that creature (no action required). The spirit can\'t heal constructs or undead.\n\nAs a bonus action on your turn, you can move the spirit up to 30 feet to a space you can see.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the healing increases by 1d6 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 bonus action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

    },
    'heat metal': {
        'description': 'Choose a manufactured metal object, such as a metal weapon or a suit of heavy or medium metal armor, that you can see within range. You cause the object to glow red-hot. Any creature in physical contact with the object takes 2d8 fire damage when you cast the spell. Until the spell ends, you can use a bonus action on each of your subsequent turns to cause this damage again.\n\nIf a creature is holding or wearing the object and takes the damage from it, the creature must succeed on a Constitution Saving Throw or drop the object if it can. If it doesn\'t drop the object, it has disadvantage on Attack Rolls and Ability Checks until the start of your next turn.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'hold person': {
        'description': 'Choose a humanoid that you can see within range. The target must succeed on a Wisdom Saving Throw or be paralyzed for the duration. At the end of each of its turns, the target can make another Wisdom Saving Throw. On a success, the spell ends on the target.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, you can target one additional humanoid for each slot level above 2nd. The humanoids must be within 30 feet of each other when you target them.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'invisibility': {
        'description': 'A creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target\'s person. The spell ends for a target that attacks or casts a spell.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (an eyelash encased in gum arabic)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Illusion',
        'concentration': True,

    },
    'knock': {
        'description': 'Choose an object that you can see within range. The object can be a door, a box, a chest, a set of manacles, a padlock, or another object that contains a mundane or magical means that prevents access.\n\nA target that is held shut by a mundane lock or that is stuck or barred becomes unlocked, unstuck, or unbarred. If the object has multiple locks, only one of them is unlocked.\n\nIf you choose a target that is held shut with arcane lock, that spell is suppressed for 10 minutes, during which time the target can be opened and shut normally.\n\nWhen you cast the spell, a loud knock, audible from as far away as 300 feet, emanates from the target object.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Transmutation',


    },
    'lesser restoration': {
        'description': 'You touch a creature and can end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Abjuration',


    },
    'levitate': {
        'description': 'One creature or loose object of your choice that you can see within range rises vertically, up to 20 feet, and remains suspended there for the duration. The spell can levitate a target that weighs up to 500 pounds. An unwilling creature that succeeds on a Constitution Saving Throw is unaffected.\n\nThe target can move only by pushing or pulling against a fixed object or surface within reach (such as a wall or a ceiling), which allows it to move as if it were climbing. You can change the target\'s altitude by up to 20 feet in either direction on your turn. If you are the target, you can move up or down as part of your move. Otherwise, you can use your action to move the target, which must remain within the spell\'s range.\n\nWhen the spell ends, the target floats gently to the ground if it is still aloft.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (either a small leather loop or a piece of golden wire bent into a cup shape with a long shank on one end)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'locate animals or plants': {
        'description': 'Describe or name a specific kind of beast or plant. Concentrating on the voice of nature in your surroundings, you learn the direction and distance to the closest creature or plant of that kind within 5 miles, if any are present.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (a bit of fur from a bloodhound)',
        'duration': 'Instantaneous',
        'school': 'Divination',

        'ritual': True
    },
    'locate object': {
        'description': 'Describe or name an object that is familiar to you. You sense the direction to the object\'s location, as long as that object is within 1,000 feet of you. If the object is in motion, you know the direction of its movement.\n\nThe spell can locate a specific object known to you, as long as you have seen it up close—within 30 feet—at least once. Alternatively, the spell can locate the nearest object of a particular kind, such as a certain kind of apparel, jewelry, furniture, tool, or weapon.\n\nThis spell can\'t locate an object if any thickness of lead, even a thin sheet, blocks a direct path between you and the object.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (a forked twig)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Divination',
        'concentration': True,

    },
    'magic mouth': {
        'description': 'You implant a message within an object in range, a message that is uttered when a trigger condition is met. Choose an object that you can see and that isn\'t being worn or carried by another creature. Then speak the message, which must be 25 words or less, though it can be delivered over as long as 10 minutes. Finally, determine the circumstance that will trigger the spell to deliver your message.\n\nWhen that circumstance occurs, a magical mouth appears on the object and recites the message in your voice and at the same volume you spoke. If the object you chose has a mouth or something that looks like a mouth (for example, the mouth of a statue), the magical mouth appears there so that the words appear to come from the object\'s mouth. When you cast this spell, you can have the spell end after it delivers its message, or it can remain and repeat its message whenever the trigger occurs.\n\nThe triggering circumstance can be as general or as detailed as you like, though it must be based on visual or audible conditions that occur within 30 feet of the object. For example, you could instruct the mouth to speak when any creature moves within 30 feet of the object or when a silver bell rings within 30 feet of it.',
        'level': 2,
        'casting_time': '1 minute',
        'range': '30 feet',
        'components': 'V, S, M (a honeycomb and jade dust worth at least 10 gp, which the spell consumes)',
        'duration': 'Until dispelled',
        'school': 'Illusion',


    },
    'magic weapon': {
        'description': 'You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic weapon with a +1 bonus to Attack Rolls and Damage Rolls.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the bonus increases to +2. When you use a spell slot of 6th level or higher, the bonus increases to +3.',
        'level': 2,
        'casting_time': '1 bonus action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Transmutation',
        'concentration': True,

    },
    'maximilian\'s earthen grasp': {
        'description': 'You choose a 5-foot-square unoccupied space on the ground that you can see within range. A medium hand made from compacted soil rises there and reaches for one creature you can see within 5 feet of it. The target must make a Strength Saving Throw. On a failed save, the target takes 2d6 bludgeoning damage and is restrained for the spell\'s duration.\n\nAs an action, you can cause the hand to crush the restrained target, which must make a Strength Saving Throw. The target takes 2d6 bludgeoning damage on a failed save, or half as much damage on a successful one.\n\nTo break out, the restrained target can use its action to make a Strength Check against your Spell Save DC. On a success, the target escapes and is no longer restrained by the hand.\n\nAs an action, you can cause the hand to reach for a different creature or to move to a different unoccupied space within range. The hand releases a restrained target if you do either.',
        'level': 2,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a miniature hand sculpted from clay)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'melf\'s acid arrow': {
        'description': 'A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a Ranged Spell Attack against the target. On a hit, the target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage and no damage at the end of its next turn.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage (both initial and later) increases by 1d4 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S, M (powdered rhubarb leaf and an adder\'s stomach)',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'mental barrier': {
        'description': 'You protect your mind with a wall of looping, repetitive thought. Until the start of your next turn, you have advantage on Intelligence, Wisdom, and Charisma Saving Throws, and you have resistance to psychic damage.',
        'level': 2,
        'casting_time': 'Reaction',
        'range': '60 feet',
        'components': 'V, S, M (a small silver mirror)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Abjuration',
        'concentration': True,

    },
    'mind spike': {
        'description': 'You reach into the mind of one creature you can see within range. The target must make a Wisdom Saving Throw, taking 3d8 psychic damage on a failed save, or half as much damage on a successful one. On a failed save, you also always know the target\'s location until the spell ends, but only while the two of you are on the same plane of existence. While you have this knowledge, the target can\'t become hidden from you, and if it\'s invisible, it gains no benefit from that condition against you.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'S',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Divination',
        'concentration': True,

    },
    'mirror image': {
        'description': 'Three illusory duplicates of yourself appear in your space. Until the spell ends, the duplicates move with you and mimic your actions, shifting position so it\'s impossible to track which image is real. You can use your action to dismiss the illusory duplicates.\n\nEach time a creature targets you with an attack during the spell\'s duration, roll a d20 to determine whether the attack instead targets one of your duplicates.\n\nIf you have three duplicates, you must roll a 6 or higher to change the attack\'s target to a duplicate. With two duplicates, you must roll an 8 or higher. With one duplicate, you must roll an 11 or higher.\n\nA duplicate\'s AC equals 10 + your Dexterity Modifier. If an attack hits a duplicate, the duplicate is destroyed. A duplicate can be destroyed only by an attack that hits it. It ignores all other damage and effects. The spell ends when all three duplicates are destroyed.\n\nA creature is unaffected by this spell if it can\'t see, if it relies on senses other than sight, such as blindsight, or if it can perceive illusions as false, as with truesight.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '1 minute',
        'school': 'Illusion',


    },
    'misty step': {
        'description': 'Briefly surrounded by silvery mist, you teleport up to 30 feet to an unoccupied space that you can see.',
        'level': 2,
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'moonbeam': {
        'description': 'A silvery beam of pale light shines down in a 5-foot-radius, 40-foot-high cylinder centered on a point within range. Until the spell ends, dim light fills the cylinder.\n\nWhen a creature enters the spell\'s area for the first time on a turn or starts its turn there, it is engulfed in ghostly flames that cause searing pain, and it must make a Constitution Saving Throw. It takes 2d10 radiant damage on a failed save, or half as much damage on a successful one.\n\nA shapechanger makes its Saving Throw with disadvantage. If it fails, it also instantly reverts to its original form and can\'t assume a different form until it leaves the spell\'s light.\n\nOn each of your turns after you cast this spell, you can use an action to move the beam up to 60 feet in any direction.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d10 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M (several seeds of any moonseed plant and a piece of opalescent feldspar)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'nystul\'s magic aura': {
        'description': 'You place an illusion on a creature or an object you touch so that divination spells reveal false information about it. The target can be a willing creature or an object that isn\'t being carried or worn by another creature.\n\nWhen you cast the spell, choose one or both of the following effects. The effect lasts for the duration. If you cast this spell on the same creature or object every day for 30 days, placing the same effect on it each time, the illusion lasts until it is dispelled.\n\nFalse Aura\n•You change the way the target appears to spells and magical effects, such as detect magic, that detect magical auras. You can make a nonmagical object appear magical, a magical object appear nonmagical, or change the object\'s magical aura so that it appears to belong to a specific school of magic that you choose. When you use this effect on an object, you can make the false magic apparent to any creature that handles the item.\n\nMask\n•You change the way the target appears to spells and magical effects that detect creature types, such as a paladin\'s Divine Sense or the trigger of a symbol spell. You choose a creature type and other spells and magical effects treat the target as if it were a creature of that type or of that alignment.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a small square of silk)',
        'duration': '24 hours',
        'school': 'Illusion',


    },
    'pass without trace': {
        'description': 'A veil of shadows and silence radiates from you, masking you and your companions from detection. For the duration, each creature you choose within 30 feet of you (including you) has a +10 bonus to Dexterity (Stealth) Checks and can\'t be tracked except by magical means. A creature that receives this bonus leaves behind no tracks or other traces of its passage.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (ashes from a burned leaf of mistletoe and a sprig of spruce)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Abjuration',
        'concentration': True,

    },
    'phantasmal force': {
        'description': 'You craft an illusion that takes root in the mind of a creature that you can see within range. The target must make an Intelligence Saving Throw. On a failed save, you create a phantasmal object, creature, or other visible phenomenon of your choice that is no larger than a 10-foot cube and that is perceivable only to the target for the duration. This spell has no effect on undead or constructs.\n\nThe phantasm includes sound, temperature, and other stimuli, also evident only to the creature.\n\nThe target can use its action to examine the phantasm with an Intelligence (Investigation) check against your Spell Save DC. If the check succeeds, the target realizes that the phantasm is an illusion, and the spell ends.\n\nWhile a target is affected by the spell, the target treats the phantasm as if it were real. The target rationalizes any illogical outcomes from interacting with the phantasm. For example, a target attempting to walk across a phantasmal bridge that spans a chasm falls once it steps onto the bridge. If the target survives the fall, it still believes that the bridge exists and comes up with some other explanation for its fall—it was pushed, it slipped, or a strong wind might have knocked it off.\n\nAn affected target is so convinced of the phantasm\'s reality that it can even take damage from the illusion. A phantasm created to appear as a creature can attack the target. Similarly, a phantasm created to appear as fire, a pool of acid, or lava can burn the target. Each round on your turn, the phantasm can deal 1d6 psychic damage to the target if it is in the phantasm\'s area or within 5 feet of the phantasm, provided that the illusion is of a creature or hazard that could logically deal damage, such as by attacking. The target perceives the damage as a type appropriate to the illusion.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a bit of fleece)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Illusion',
        'concentration': True,

    },
    'prayer of healing': {
        'description': 'Up to six creatures of your choice that you can see within range each regain hit points equal to 2d8 + your Spellcasting Ability Modifier. This spell has no effect on undead or constructs.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the healing increases by 1d8 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '10 minutes',
        'range': '30 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'protection from poison': {
        'description': 'You touch a creature. If it is poisoned, you neutralize the poison. If more than one poison afflicts the target, you neutralize one poison that you know is present, or you neutralize one at random.\n\nFor the duration, the target has advantage on Saving Throws against being poisoned, and it has resistance to poison damage.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Abjuration',


    },
    'pyrotechnics': {
        'description': 'Choose an area of nonmagical flame that you can see and that fits within a 5-foot cube within range. You can extinguish the fire in that area, and you create either fireworks or smoke when you do so.\n\nFireworks\n•The target explodes with a dazzling display of colors. Each creature within 10 feet of the target must succeed on a Constitution Saving Throw or become blinded until the end of your next turn.\n\nSmoke\n•Thick black smoke spreads out from the target in a 20-foot radius, moving around corners. The area of the smoke is heavily obscured. The smoke persists for 1 minute or until a strong wind disperses it.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a bit of phosphorus or a firefly)',
        'duration': 'Instantaneous',
        'school': 'Transmutation',


    },
    'ray of enfeeblement': {
        'description': 'A black beam of enervating energy springs from your finger toward a creature within range. Make a Ranged Spell Attack against the target. On a hit, the target deals only half damage with Weapon Attacks that use Strength until the spell ends.\n\nAt the end of each of the target\'s turns, it can make a Constitution Saving Throw against the spell. On a success, the spell ends.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Necromancy',
        'concentration': True,

    },
    'rope trick': {
        'description': 'You touch a length of rope that is up to 60 feet long. One end of the rope then rises into the air until the whole rope hangs perpendicular to the ground. At the upper end of the rope, an invisible entrance opens to an extradimensional space that lasts until the spell ends.\n\nThe extradimensional space can be reached by climbing to the top of the rope. The space can hold as many as eight medium or smaller creatures. The rope can be pulled into the space, making the rope disappear from view outside the space.\n\nAttacks and spells can\'t cross through the entrance into or out of the extradimensional space, but those inside can see out of it as if through a 3-foot-by-5-foot window centered on the rope.\n\nAnything inside the extradimensional space drops out when the spell ends.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (powdered corn extract and a twisted loop of parchment)',
        'duration': '1 hour',
        'school': 'Transmutation',


    },
    'scorching ray': {
        'description': 'You create three rays of fire and hurl them at targets within range. You can hurl them at one target or several.\n\nMake a Ranged Spell Attack for each ray. On a hit, the target takes 2d6 fire damage.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, you create one additional ray for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'see invisibility': {
        'description': 'For the duration, you see invisible creatures and objects as if they were visible, and you can see into the Ethereal Plane. Ethereal creatures and objects appear ghostly and translucent.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (a dash of talc and a small amount of silver powder)',
        'duration': '1 hour',
        'school': 'Divination',


    },
    'shadow blade': {
        'description': 'You weave together threads of shadow to create a sword of solidified gloom in your hand. This magic sword lasts until the spell ends. It counts as a simple melee weapon with which you are proficient. It deals 2d8 psychic damage on a hit and has the finesse, light, and thrown properties (range 20/60). In addition, when you use the sword to attack a target that is in dim light or darkness, you make the Attack Roll with advantage.\n\nIf you drop the weapon or throw it, it dissipates at the end of the turn. Thereafter, while the spell persists, you can use a bonus action to cause the sword to reappear in your hand.\n\nWhen you cast this spell using a 3rd- or 4th-level spell slot, the damage increases to 3d8. When you cast it using a 5th- or 6th-level spell slot, the damage increases to 4d8. When you cast it using a spell slot of 7th level or higher, the damage increases to 5d8.',
        'level': 2,
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Illusion',
        'concentration': True,

    },
    'shatter': {
        'description': 'A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range. Each creature in a 10-foot-radius sphere centered on that point must make a Constitution Saving Throw. A creature takes 3d8 thunder damage on a failed save, or half as much damage on a successful one. A creature made of inorganic material such as stone, crystal, or metal has disadvantage on this Saving Throw.\n\nA nonmagical object that isn\'t being worn or carried also takes the damage if it\'s in the spell\'s area.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a chip of mica)',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'silence': {
        'description': 'For the duration, no sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose within range. Any creature or object entirely inside the sphere is immune to thunder damage, and creatures are deafened while entirely inside it. Casting a spell that includes a verbal component is impossible there.',
        'level': 2,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Illusion',
        'concentration': True,

    },
    'skywrite': {
        'description': 'You cause up to ten words to form in a part of the sky you can see. The words appear to be made of cloud and remain in place for the spell\'s duration. The words dissipate when the spell ends. A strong wind can disperse the clouds and end the spell early.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Sight',
        'components': 'V, S, M (powdered cloud and a bit of red clay)',
        'duration': '1 hour',
        'school': 'Transmutation',


    },
    'snilloc\'s snowball swarm': {
        'description': 'A flurry of magic snowballs erupts from a point you choose within range. Each creature in a 5-foot-radius sphere centered on that point must make a Dexterity Saving Throw. A creature takes 3d6 cold damage on a failed save, or half as much damage on a successful one.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d6 for each slot level above 2nd.',
        'level': 2,
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S, M (a small piece of white leather wrapped in a loop)',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'spider climb': {
        'description': 'Until the spell ends, one willing creature you touch gains the ability to move up, down, and across vertical surfaces and upside down along ceilings, while leaving its hands free. The target also gains a climbing speed equal to its walking speed.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a drop of bitumen and a spider)',
        'duration': '1 hour',
        'school': 'Transmutation',


    },
    'spike growth': {
        'description': 'The ground in a 20-foot radius centered on a point within range twists and sprouts hard spikes and thorns. The area becomes difficult terrain for the duration. When a creature moves into or within the area, it takes 2d4 piercing damage for every 5 feet it travels.\n\nThe transformation of the ground is camouflaged to look natural. Any creature that can\'t see the area at the time the spell is cast must make a Wisdom (Perception) check against your Spell Save DC to recognize the terrain as hazardous before entering it.',
        'level': 2,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S, M (seven sharp thorns or seven small twigs)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'spiritual weapon': {
        'description': 'You create a floating, spectral weapon within range that lasts for the duration or until you cast this spell again. When you cast the spell, you can make a Melee Spell Attack against a creature within 5 feet of the weapon. On a hit, the target takes force damage equal to 1d8 + your Spellcasting Ability Modifier.\n\nAs a bonus action on your turn, you can move the weapon up to 20 feet and repeat the attack against a creature within 5 feet of it.\n\nThe weapon can take whatever form you choose. Clerics of deities who are associated with a particular weapon (as St. Cuthbert is known for his mace and Thor for his hammer) make this spell\'s effect resemble that weapon.\n\nWhen you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for every two slot levels above 2nd.',
        'level': 2,
        'casting_time': '1 bonus action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': '1 minute',
        'school': 'Evocation',


    },
    'suggestion': {
        'description': 'You suggest a course of activity (limited to a sentence or two) and magically influence a creature you can see within range that can hear and understand you. Creatures that can\'t be charmed are immune to this effect. The suggestion must be worded in such a manner as to make the course of action sound reasonable. Asking the creature to stab itself, throw itself onto a spear, immolate itself, or do some other obviously harmful act ends the spell.\n\nThe target must make a Wisdom Saving Throw. On a failed save, it pursues the course of action you described to the best of its ability. The suggested course of action can continue for the entire duration. If the suggested activity can be completed in a shorter time, the spell ends when the subject finishes what it was asked to do.\n\nYou can also specify conditions that will trigger a special activity during the duration. For example, you might suggest that a knight give her warhorse to the first beggar she meets. If the condition isn\'t met before the spell expires, the activity isn\'t performed.\n\nIf you or any of your companions damage the target, the spell ends.',
        'level': 2,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, M (a snake\'s tongue and either a bit of honeycomb or a drop of sweet oil)',
        'duration': 'Concentration, up to 8 hours',
        'school': 'Enchantment',
        'concentration': True,

    },
    'thought shield': {
        'description': 'You weave a clouding veil over the mind of one creature you touch. For the duration, the target\'s mind can\'t be read or detected, creatures can\'t telepathically communicate with the target unless the target allows it, and the target has advantage on Saving Throws against any effect that would determine whether it is telling the truth.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Abjuration',


    },
    'warding bond': {
        'description': 'This spell wards a willing creature you touch and creates a mystic connection between you and the target until the spell ends. While the target is within 60 feet of you, it gains a +1 bonus to AC and Saving Throws, and it has resistance to all damage. Also, each time it takes damage, you take the same amount of damage.\n\nThe spell ends if you drop to 0 hit points or if you and the target become separated by more than 60 feet. It also ends if the spell is cast again on either of the connected creatures. You can also dismiss the spell as an action.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a pair of platinum rings worth at least 50 gp each, which you and the target must wear for the duration)',
        'duration': '1 hour',
        'school': 'Abjuration',


    },
    'warding wind': {
        'description': 'A strong wind (20 miles per hour) blows around you in a 10-foot radius and moves with you, remaining centered on you. The wind lasts for the spell\'s duration.\n\nThe wind has the following effects:\n\n•It deafens you and other creatures in its area.\n•It extinguishes unprotected flames in its area that are torch-sized or smaller.\n•It hedges out vapor, gas, and fog that can be dispersed by strong wind.\n•The area is difficult terrain for creatures other than you.\n•The Attack Rolls of Ranged Weapon Attacks have disadvantage if the attacks pass in or out of the wind.',
        'level': 2,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

    },
    'web': {
        'description': 'You conjure a mass of thick, sticky webbing at a point of your choice within range. The webs fill a 20-foot cube from that point for the duration. The webs are difficult terrain and lightly obscure their area.\n\nIf the webs aren\'t anchored between two solid masses (such as walls or trees) or layered across a floor, wall, or ceiling, the conjured web collapses on itself, and the spell ends at the start of your next turn. Webs layered over a flat surface have a depth of 5 feet.\n\nEach creature that starts its turn in the webs or that enters them during its turn must make a Dexterity Saving Throw. On a failed save, the creature is restrained as long as it remains in the webs or until it breaks free.\n\nA creature restrained by the webs can use its action to make a Strength Check against your Spell Save DC. If it succeeds, it is no longer restrained.\n\nThe webs are flammable. Any 5-foot cube of webs exposed to fire burns away in 1 round, dealing 2d4 fire damage to any creature that starts its turn in the fire.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a bit of spiderweb)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Conjuration',
        'concentration': True,

    },
    'zone of truth': {
        'description': 'You create a magical zone that guards against deception in a 15-foot-radius sphere centered on a point of your choice within range. Until the spell ends, a creature that enters the spell\'s area for the first time on a turn or starts its turn there must make a Charisma Saving Throw. On a failed save, a creature can\'t speak a deliberate lie while in the radius. You know whether each creature succeeds or fails on its Saving Throw.\n\nAn affected creature is aware of the spell and can thus avoid answering questions to which it would normally respond with a lie. Such creatures can be evasive in its answers as long as it remains within the boundaries of the truth.',
        'level': 2,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a small silver or copper coin)',
        'duration': '10 minutes',
        'school': 'Enchantment',
        
    },
}
