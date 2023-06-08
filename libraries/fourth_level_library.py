fourth_level_spells = {
    'arcane eye': {
        'description': 'Create an invisible, magical eye within range that hovers in the air for the duration.\n\nYou mentally receive visual information from the eye, which has normal vision and darkvision out to 30 feet. The eye can look in every direction.\n\nAs an action, you can move the eye up to 30 feet in any direction. There is no limit to how far away from you the eye can move, but it can\'t enter another plane of existence. A solid barrier blocks the eye\'s movement, but the eye can pass through an opening as small as 1 inch in diameter.',
        'level': '4',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a bit of bat fur)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Divination',
        'concentration': True,

    },
    'aura of life': {
        'description': 'Life-preserving energy radiates from you in an aura with a 30-foot radius. Until the spell ends, the aura moves with you, centered on you. Each nonhostile creature in the aura (including you) has resistance to necrotic damage, and its hit point maximum can\'t be reduced. In addition, a nonhostile, living creature regains 1 hit point when it starts its turn in the aura with 0 hit points.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Abjuration',
        'concentration': True,

    },
    'aura of purity': {
        'description': 'Purifying energy radiates from you in an aura with a 30-foot radius. Until the spell ends, the aura moves with you, centered on you. Each nonhostile creature in the aura (including you) can\'t become diseased, has resistance to poison damage, and has advantage on Saving Throws against effects that cause any of the following conditions: blinded, charmed, deafened, frightened, paralyzed, poisoned, and stunned.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Abjuration',
        'concentration': True,

    },
    'banishment': {
        'description': 'You attempt to send one creature that you can see within range to another plane of existence. The target must succeed on a Charisma Saving Throw or be banished.\n\nIf the target is native to the plane of existence you\'re on, you banish the target to a harmless demiplane. While there, the target is incapacitated. The target remains there until the spell ends, at which point the target reappears in the space it left or in the nearest unoccupied space if that space is occupied.\n\nIf the target is native to a different plane of existence than the one you\'re on, the target is banished with a faint popping noise, returning to its home plane. If the spell ends before 1 minute has passed, the target reappears in the space it left or in the nearest unoccupied space if that space is occupied. Otherwise, the target doesn\'t return.\n\nWhen you cast this spell using a spell slot of 5th level or higher, you can target one additional creature for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (an item distasteful to the target)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Abjuration',
        'concentration': True,

    },
    'blight': {
        'description': 'Necromantic energy washes over a creature of your choice that you can see within range, draining moisture and vitality from it. The target must make a Constitution Saving Throw. The target takes 8d8 necrotic damage on a failed save, or half as much damage on a successful one. This spell has no effect on undead or constructs.\n\nIf you target a plant creature or a magical plant, it makes the Saving Throw with disadvantage, and the spell deals maximum damage to it.\n\nIf you target a nonmagical plant that isn\'t a creature, such as a tree or shrub, it doesn\'t make a Saving Throw, it simply withers and dies.\n\nWhen you cast this spell using a spell slot of 5th level or higher, the damage increases by 1d8 for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Necromancy',


    },
    'charm monster': {
        'description': 'You attempt to charm a creature you can see within range. It must make a Wisdom Saving Throw, and it does so with advantage if you or your companions are fighting it. If it fails the Saving Throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it. The charmed creature is friendly to you. When the spell ends, the creature knows it was charmed by you.\n\nWhen you cast this spell using a spell slot of 5th level or higher, you can target one additional creature for each slot level above 4th. The creatures must be within 30 feet of each other when you target them.',
        'level': '4',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Enchantment',


    },
    'compulsion': {
        'description': 'Creatures of your choice that you can see within range and that can hear you must make a Wisdom Saving Throw. A target automatically succeeds on this Saving Throw if it can\'t be charmed. On a failed save, a target is affected by this spell. Until the spell ends, you can use a bonus action on each of your turns to designate a direction that is horizontal to you. Each affected target must use as much of its movement as possible to move in that direction on its next turn. It can take its action before it moves. After moving in this way, it can make another Wisdom Saving Throw to try to end the effect.\n\nA target isn\'t compelled to move into an obviously deadly hazard, such as a fire or pit, but it will provoke opportunity attacks to move in the designated direction.',
        'level': '4',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V',
        'duration': '1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'confusion': {
        'description': 'This spell assaults and twists creatures\' minds, spawning delusions and provoking uncontrolled action. Each creature in a 10-foot-radius sphere centered on a point you choose within range must succeed on a Wisdom Saving Throw when you cast this spell or be affected by it.\n\nAn affected target can\'t take reactions and must roll a d10 at the start of each of its turns to determine its behavior for that turn.\n╔══════╤═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n║ d10  │ Behavior                                                                                                                                                                                        ║\n╠══════╪═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣\n║ 1    │ The creature uses all its movement to move in a random direction. To determine the direction, roll a d8 and assign a direction to each die face. The creature doesn\'t take an action this turn. ║\n╟──────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╢\n║ 2-6  │ The creature doesn\'t move or take actions this turn.                                                                                                                                            ║\n╟──────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╢\n║ 7-8  │ The creature uses its action to make a Melee Attack against a randomly determined creature within its reach. If there is no creature within its reach, the creature does nothing this turn.     ║\n╟──────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╢\n║ 9-10 │ The creature can act and move normally.                                                                                                                                                         ║\n╚══════╧═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\n\nAt the end of each of its turns, an affected target can make a Wisdom Saving Throw. If it succeeds, this effect ends for that target.\n\nWhen you cast this spell using a spell slot of 5th level or higher, the radius of the sphere increases by 5 feet for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S, M (three nut shells)',
        'duration': '1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'conjure minor elementals': {
        'description': 'You summon elementals that appear in unoccupied spaces that you can see within range. You choose one the following options for what appears:\n\n•One elemental of challenge rating 2 or lower\n•Two elementals of challenge rating 1 or lower\n•Four elementals of challenge rating 1/2 or lower\n•Eight elementals of challenge rating 1/4 or lower.\n\nAn elemental summoned by this spell disappears when it drops to 0 hit points or when the spell ends.\n\nThe summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don\'t issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.\n\nThe DM has the creatures\' statistics.\n\nWhen you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot.',
        'level': '4',
        'casting_time': '1 minute',
        'range': '90 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Conjuration',
        'concentration': True,

    },
    'conjure woodland beings': {
        'description': 'You summon fey creatures that appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:\n\n•One fey creature of challenge rating 2 or lower\n•Two fey creatures of challenge rating 1 or lower\n•Four fey creatures of challenge rating 1/2 or lower\n•Eight fey creatures of challenge rating 1/4 or lower\n\nA summoned creature disappears when it drops to 0 hit points or when the spell ends.\n\nThe summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which have their own turns. They obey any verbal commands that you issue to them (no action required by you). If you don\'t issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.\n\nThe DM has the creatures\' statistics.\n\nWhen you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot.',
        'level': '4',
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (one holly berry per creature summoned)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Conjuration',
        'concentration': True,

    },
    'control water': {
        'description': 'Until the spell ends, you control any freestanding water inside an area you choose that is a cube up to 100 feet on a side. You can choose from any of the following effects when you cast this spell. As an action on your turn, you can repeat the same effect or choose a different one.\n\nFlood\nYou cause the water level of all standing water in the area to rise by as much as 20 feet. If the area includes a shore, the flooding water spills over onto dry land.\n\nIf you choose an area in a large body of water, you instead create a 20-foot tall wave that travels from one side of the area to the other and then crashes down. Any huge or smaller vehicles in the wave\'s path are carried with it to the other side. Any huge or smaller vehicles struck by the wave have a 25 percent chance of capsizing.\n\nThe water level remains elevated until the spell ends or you choose a different effect. If this effect produced a wave, the wave repeats on the start of your next turn while the flood effect lasts.\n\nPart Water\nYou cause water in the area to move apart and create a trench. The trench extends across the spell\'s area, and the separated water forms a wall to either side. The trench remains until the spell ends or you choose a different effect. The water then slowly fills in the trench over the course of the next round until the normal water level is restored.\n\nRedirect Water\nYou cause flowing water in the area to move in a direction you choose, even if the water has to flow over obstacles, up walls, or in other unlikely directions. The water in the area moves as you direct it, but once it moves beyond the spell\'s area, it resumes its flow based on the terrain conditions. The water continues to move in the direction you chose until the spell ends or you choose a different effect.\n\nWhirlpool\nThis effect requires a body of water at least 50 feet square and 25 feet deep. You cause a whirlpool to form in the center of the area. The whirlpool forms a vortex that is 5 feet wide at the base, up to 50 feet wide at the top, and 25 feet tall. Any creature or object in the water and within 25 feet of the vortex is pulled 10 feet toward it. A creature can swim away from the vortex by making a Strength (Athletics) check against your Spell Save DC.\n\nWhen a creature enters the vortex for the first time on a turn or starts its turn there, it must make a Strength Saving Throw. On a failed save, the creature takes 2d8 bludgeoning damage and is caught in the vortex until the spell ends. On a successful save, the creature takes half damage, and isn\'t caught in the vortex. A creature caught in the vortex can use its action to try to swim away from the vortex as described above, but has disadvantage on the Strength (Athletics) check to do so.\n\nThe first time each turn that an object enters the vortex, the object takes 2d8 bludgeoning damage; this damage occurs each round it remains in the vortex.',
        'level': '4',
        'casting_time': '1 action',
        'range': '300 feet',
        'components': 'V, S, M (a drop of water and a pinch of dust)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'death ward': {
        'description': 'You touch a creature and grant it a measure of protection from death.\n\nThe first time the target would drop to 0 hit points as a result of taking damage, the target instead drops to 1 hit point, and the spell ends.\n\nIf the spell is still in effect when the target is subjected to an effect that would kill it instantaneously without dealing damage, that effect is instead negated against the target, and the spell ends.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': '8 hours',
        'school': 'Abjuration',


    },
    'dimension door': {
        'description': 'You teleport yourself from your current location to any other spot within range. You arrive at exactly the spot desired. It can be a place you can see, one you can visualize, or one you can describe by stating distance and direction, such as "200 feet straight downward" or "upward to the northwest at a 45-degree angle, 300 feet."\n\nYou can bring along objects as long as their weight doesn\'t exceed what you can carry. You can also bring one willing creature of your size or smaller who is carrying gear up to its carrying capacity. The creature must be within 5 feet of you when you cast this spell.\n\nIf you would arrive in a place already occupied by an object or a creature, you and any creature traveling with you each take 4d6 force damage, and the spell fails to teleport you.',
        'level': '4',
        'casting_time': '1 action',
        'range': '500 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'divination': {
        'description': 'Your magic and an offering put you in contact with a god or a god\'s servants. You ask a single question concerning a specific goal, event, or activity to occur within 7 days. The DM offers a truthful reply. The reply might be a short phrase, a cryptic rhyme, or an omen.\n\nThe spell doesn\'t take into account any possible circumstances that might change the outcome, such as the casting of additional spells or the loss or gain of a companion.\n\nIf you cast the spell two or more times before finishing your next long rest, there is a cumulative 25 percent chance for each casting after the first that you get a random reading. The DM makes this roll in secret.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (incense and a sacrificial offering appropriate to your religion, together worth at least 25 gp)',
        'duration': 'Instantaneous',
        'school': 'Divination',

        'ritual': True
    },
    'dominate beast': {
        'description': 'You attempt to beguile a beast that you can see within range. It must succeed on a Wisdom Saving Throw or be charmed by you for the duration. If you or creatures that are friendly to you are fighting it, it has advantage on the Saving Throw.\n\nWhile the beast is charmed, you have a telepathic link with it as long as the two of you are on the same plane of existence. You can use this telepathic link to issue commands to the creature while you are conscious (no action required), which it does its best to obey. You can specify a simple and general course of action, such as "Attack that creature," "Run over there," or "Fetch that object." If the creature completes the order and doesn\'t receive further direction from you, it defends and preserves itself to the best of its ability.\n\nYou can use your action to take total and precise control of the target. Until the end of your next turn, the creature takes only the actions you choose, and doesn\'t do anything that you don\'t allow it to do. During this time, you can also cause the creature to use a reaction, but this requires you to use your own reaction as well.\n\nEach time the target takes damage, it makes a new Wisdom Saving Throw against the spell. If the Saving Throw succeeds, the spell ends.\n\nWhen you cast this spell with a 5th-level spell slot, the duration is concentration, up to 10 minutes. When you use a 6th-level spell slot, the duration is concentration, up to 1 hour. When you use a spell slot of 7th level or higher, the duration is concentration, up to 8 hours.',
        'level': '4',
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'ego whip': {
        'description': 'You lash the mind of one creature you can see within range, filling it with despair. The target must succeed on an Intelligence Saving Throw or suffer disadvantage on Attack Rolls, Ability Checks, and Saving Throws, and it can\'t cast spells. At the end of each of its turns, the target can make another Intelligence Saving Throw. On a success, the spell ends on the target.',
        'level': '4',
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S, M (a leech)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'elemental bane': {
        'description': 'Choose one creature you can see within range, and choose one of the following damage types: acid, cold, fire, lightning, or thunder. The target must succeed on a Constitution Saving Throw or be affected by the spell for its duration. The first time each turn the affected target takes damage of the chosen type, the target takes an extra 2d6 damage of that type. Moreover, the target loses any resistance to that damage type until the spell ends.\n\nWhen you cast this spell using a spell slot of 5th level or higher, you can target one additional creature for each slot level above 4th. The creatures must be within 30 feet of each other when you target them.',
        'level': '4',
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'evards black tentacles': {
        'description': 'Squirming, ebony tentacles fill a 20-foot square on ground that you can see within range. For the duration, these tentacles turn the ground in the area into difficult terrain.\n\nWhen a creature enters the affected area for the first time on a turn or starts its turn there, the creature must succeed on a Dexterity Saving Throw or take 3d6 bludgeoning damage and be restrained by the tentacles until the spell ends. A creature that starts its turn in the area and is already restrained by the tentacles takes 3d6 bludgeoning damage.\n\nA creature restrained by the tentacles can use its action to make a Strength or Dexterity Check (its choice) against your Spell Save DC. On a success, it frees itself.',
        'level': '4',
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

    },
    'fabricate': {
        'description': 'You convert raw materials into products of the same material. For example, you can fabricate a wooden bridge from a clump of trees, a rope from a patch of hemp, and clothes from flax or wool.\n\nChoose raw materials that you can see within range. You can fabricate a large or smaller object (contained within a 10-foot cube, or eight connected 5-foot cubes), given a sufficient quantity of raw material. If you are working with metal, stone, or another mineral substance, however, the fabricated object can be no larger than medium (contained within a single 5-foot cube). The quality of objects made by the spell is commensurate with the quality of the raw materials.\n\nCreatures or magic items can\'t be created or transmuted by this spell. You also can\'t use it to create items that ordinarily require a high degree of craftsmanship, such as jewelry, weapons, glass, or armor, unless you have proficiency with the type of artisan\'s tools used to craft such objects.',
        'level': '4',
        'casting_time': '10 minutes',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Transmutation',

    },
    'find greater steed': {
        'description': 'You summon a spirit that assumes the form of a loyal, majestic mount. Appearing in an unoccupied space within range, the spirit takes on a form you choose: a Griffon, a Pegasus, a Peryton, a Dire Wolf, a Rhinoceros, or a Saber-Toothed Tiger. The creature has the statistics provided in the Monster Manual for the chosen form, though it is a celestial, a fey, or a fiend (your choice) instead of its normal creature type. Additionally, if it has an Intelligence Score of 5 or lower, its Intelligence becomes 6, and it gains the ability to understand one language of your choice that you speak.\n\nYou control the mount in combat. While the mount is within 1 mile of you, you can communicate with it telepathically. While mounted on it, you can make any spell you cast that targets only you also target the mount.\n\nThe mount disappears temporarily when it drops to 0 hit points or when you dismiss it as an action. Casting this spell again re-summons the bonded mount, with all its hit points restored and any conditions removed.\n\nYou can\'t have more than one mount bonded by this spell or find steed at the same time. As an action, you can release a mount from its bond, causing it to disappear permanently.\n\nWhenever the mount disappears, it leaves behind any objects it was wearing or carrying.',
        'level': '4',
        'casting_time': '10 minutes',
        'range': '30 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Conjuration',

    },
    'fire shield': {
        'description': 'Thin and wispy flames wreathe your body for the duration, shedding bright light in a 10-foot radius and dim light for an additional 10 feet. You can end the spell early by using an action to dismiss it.\n\nThe flames provide you with a warm shield or a chill shield, as you choose. The warm shield grants you resistance to cold damage, and the chill shield grants you resistance to fire damage.\n\nIn addition, whenever a creature within 5 feet of you hits you with a Melee Attack, the shield erupts with flame. The attacker takes 2d8 fire damage from a warm shield, or 2d8 cold damage from a cold shield.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (a bit of phosphorus or a firefly)',
        'duration': '10 minutes',
        'school': 'Evocation',


    },
    'freedom of movement': {
        'description': 'You touch a willing creature. For the duration, the target\'s movement is unaffected by difficult terrain, and spells and other magical effects can neither reduce the target\'s speed nor cause the target to be paralyzed or restrained.\n\nThe target can also spend 5 feet of movement to automatically escape from nonmagical restraints, such as manacles or a creature that has it grappled. Finally, being underwater imposes no penalties on the target\'s movement or attacks.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a leather strap, bound around the arm or a similar appendage)',
        'duration': '1 hour',
        'school': 'Abjuration',


    },
    'giant insect': {
        'description': 'You transform up to ten centipedes, three spiders, five wasps, or one scorpion within range into giant versions of their natural forms for the duration. A centipede becomes a Giant Centipede, a spider becomes a Giant Spider, a wasp becomes a Giant Wasp, and a scorpion becomes a Giant Scorpion.\n\nEach creature obeys your verbal commands, and in combat, they act on your turn each round. The DM has the statistics for these creatures and resolves their actions and movement.\n\nA creature remains in its giant size for the duration, until it drops to 0 hit points, or until you use an action to dismiss the effect on it.\n\nThe DM might allow you to choose different targets. For example, if you transform a bee, its giant version might have the same statistics as a Giant Wasp.',
        'level': '4',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S',
        'duration': '10 minutes',
        'school': 'Transmutation',


    },
    'grasping vine': {
        'description': 'You conjure a vine that sprouts from the ground in an unoccupied space of your choice that you can see within range. When you cast this spell, you can direct the vine to lash out at a creature within 30 feet of it that you can see. That creature must succeed on a Dexterity Saving Throw or be pulled 20 feet directly toward the vine.\n\nUntil the spell ends, you can direct the vine to lash out at the same creature or another one as a bonus action on each of your turns.',
        'level': '4',
        'casting_time': '1 bonus action',
        'range': '30 feet',
        'components': 'V, S, M (a bit of honeycomb and jade dust worth at least 25 gp, which the spell consumes)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

    },
    'greater invisibility': {
        'description': 'You or a creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target\'s person.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Illusion',
        'concentration': True,

    },
    'guardian of faith': {
        'description': 'A large spectral guardian appears and hovers for the duration in an unoccupied space of your choice that you can see within range. The guardian occupies that space and is indistinct except for a gleaming sword and shield emblazoned with the symbol of your deity.\n\nAny creature hostile to you that moves to a space within 10 feet of the guardian for the first time on a turn must succeed on a Dexterity Saving Throw. The creature takes 20 radiant damage on a failed save, or half as much damage on a successful one. The guardian vanishes when it has dealt a total of 60 damage.',
        'level': '4',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V',
        'duration': '8 hours',
        'school': 'Conjuration',


    },
    'guardian of nature': {
        'description': 'A nature spirit answers your call and transforms you into a powerful guardian. The transformation lasts until the spell ends. You choose one of the following forms to assume: Primal Beast or Great Tree.\n\nPrimal Beast\nBestial fur covers your body, your facial features become feral, and you gain the following benefits:\n\n•Your walking speed increases by 10 feet.\n•You gain darkvision with a range of 120 feet.\n•You make Strength-based Attack Rolls with advantage.\n•Your Melee Weapon Attacks deal an extra 1d6 force damage on a hit.\n\nGreat Tree\nYour skin appears barky, leaves sprout from your hair, and you gain the following benefits:\n\n•You gain 10 temporary hit points.\n•You make Constitution Saving Throws with advantage.\n•You make Dexterity- and Wisdom-based Attack Rolls with advantage.\n•While you are on the ground, the ground within 15 feet of you is difficult terrain for your enemies.',
        'level': '4',
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'hallucinatory terrain': {
        'description': 'You make natural terrain in a 150-foot cube in range look, sound, and smell like some other sort of natural terrain. Thus, open fields or a road can be made to resemble a swamp, hill, crevasse, or some other difficult or impassable terrain. A pond can be made to seem like a grassy meadow, a precipice like a gentle slope, or a rock-strewn gully like a wide and smooth road. Manufactured structures, equipment, and creatures within the area aren\'t changed in appearance.\n\nThe tactile characteristics of the terrain are unchanged, so creatures entering the area are likely to see through the illusion. If the difference isn\'t obvious by touch, a creature carefully examining the illusion can attempt an Intelligence (Investigation) check against your Spell Save DC to disbelieve it. A creature who discerns the illusion for what it is, sees it as a vague image superimposed on the terrain.',
        'level': '4',
        'casting_time': '10 minutes',
        'range': '300 feet',
        'components': 'V, S, M (a stone, a twig, and a bit of green plant)',
        'duration': '24 hours',
        'school': 'Illusion',
    },
    'ice storm': {
        'description': 'A hail of rock-hard ice pounds to the ground in a 20-foot-radius, 40-foot-high cylinder centered on a point within range. Each creature in the cylinder must make a Dexterity Saving Throw. A creature takes 2d8 bludgeoning damage and 4d6 cold damage on a failed save, or half as much damage on a successful one.\n\nHailstones turn the storm\'s area of effect into difficult terrain until the end of your next turn.\n\nWhen you cast this spell using a spell slot of 5th level or higher, the bludgeoning damage increases by 1d8 for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '300 feet',
        'components': 'V, S, M (a pinch of dust and a few drops of water)',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'leomunds secret chest': {
        'description': 'You hide a chest, and all its contents, on the Ethereal Plane. You must touch the chest and the miniature replica that serves as a material component for the spell. The chest can contain up to 12 cubic feet of nonliving material (3 feet by 2 feet by 2 feet).\n\nWhile the chest remains on the Ethereal Plane, you can use an action and touch the replica to recall the chest. It appears in an unoccupied space on the ground within 5 feet of you. You can send the chest back to the Ethereal Plane by using an action and touching both the chest and the replica.\n\nAfter 60 days, there is a cumulative 5 percent chance per day that the spell\'s effect ends. This effect ends if you cast this spell again, if the smaller replica chest is destroyed, or if you choose to end the spell as an action. If the spell ends and the larger chest is on the Ethereal Plane, it is irretrievably lost.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (an exquisite chest, 3 feet by 2 feet by 2 feet, constructed from rare materials worth at least 5,000 gp)',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'locate creature': {
        'description': 'Describe or name a creature that is familiar to you. You sense the direction to the creature\'s location, as long as that creature is within 1,000 feet of you. If the creature is moving, you know the direction of its movement.\n\nThe spell can locate a specific creature known to you, or the nearest creature of a specific kind (such as a Human or a Unicorn), so long as you have seen such a creature up close—within 30 feet—at least once. If the creature you described or named is in a different form, such as being under the effects of a polymorph spell, this spell doesn\'t locate the creature.\n\nThis spell can\'t locate a creature if running water at least 10 feet wide blocks a direct path between you and the creature.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (a bit of fur from a bloodhound)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Divination',
        'concentration': True,

    },
    'mordenkainens faithful hound': {
        'description': 'You conjure a phantom watchdog in an unoccupied space that you can see within range, where it remains for the duration, until you dismiss it as an action, or until you move more than 100 feet away from it.\n\nThe hound is invisible to all creatures except you and can\'t be harmed. When a small or larger creature comes within 30 feet of it without first speaking the password that you specify when you cast this spell, the hound starts barking loudly. The hound sees invisible creatures and can see into the Ethereal Plane. It ignores illusions.\n\nAt the start of each of your turns, the hound attempts to bite one creature within 5 feet of it that is hostile to you. The hound\'s attack bonus is equal to your Spellcasting Ability Modifier + your proficiency bonus. On a hit, it deals 4d8 piercing damage.',
        'level': '4',
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a tiny silver whistle, a piece of bone, and a thread)',
        'duration': '8 hours',
        'school': 'Conjuration',


    },
    'mordenkainens private sanctum': {
        'description': 'You make an area within range magically secure. The area is a cube that can be as small as 5 feet to as large as 100 feet on each side. The spell lasts for the duration or until you use an action to dismiss it.\n\nWhen you cast the spell, you decide what sort of security the spell provides, choosing any or all of the following properties:\n\n•Sound can\'t pass through the barrier at the edge of the warded area.\n•The barrier of the warded area appears dark and foggy, preventing vision (including darkvision) through it.\n•Sensors created by divination spells can\'t appear inside the protected area or pass through the barrier at its perimeter.\n•Creatures in the area can\'t be targeted by divination spells.\n•Nothing can teleport into or out of the warded area.\n•Planar travel is blocked within the warded area.\n\nCasting this spell on the same spot every day for a year makes this effect permanent.\n\nWhen you cast this spell using a spell slot of 5th level or higher, you can increase the size of the cube by 100 feet for each slot level beyond 4th. Thus you could protect a cube that can be up to 200 feet on one side by using a spell slot of 5th level.',
        'level': '4',
        'casting_time': '10 minutes',
        'range': '120 feet',
        'components': 'V, S, M (a thin sheet of lead, a piece of opaque glass, a wad of cotton or cloth, and powdered chrysolite)',
        'duration': '24 hours',
        'school': 'Abjuration',


    },
    'otilukes resilient sphere': {
        'description': 'A sphere of shimmering force encloses a creature or object of large size or smaller within range. An unwilling creature must make a Dexterity Saving Throw. On a failed save, the creature is enclosed for the duration.\n\nNothing—not physical objects, energy, or other spell effects—can pass through the barrier, in or out, though a creature in the sphere can breathe there. The sphere is immune to all damage, and a creature or object inside can\'t be damaged by attacks or effects originating from outside, nor can a creature inside the sphere damage anything outside it.\n\nThe sphere is weightless and just large enough to contain the creature or object inside. An enclosed creature can use its action to push against the sphere\'s walls and thus roll the sphere at up to half the creature\'s speed. Similarly, the globe can be picked up and moved by other creatures.\n\nA disintegrate spell targeting the globe destroys it without harming anything inside it.',
        'level': '4',
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S, M (a hemispherical piece of clear crystal and a matching hemispherical piece of gum arabic)',
        'duration': '1 minute',
        'school': 'Evocation',


    },
    'phantasmal killer': {
        'description': 'You tap into the nightmares of a creature you can see within range and create an illusory manifestation of its deepest fears, visible only to that creature. The target must make a Wisdom Saving Throw. On a failed save, the target becomes frightened for the duration. At the end of each of the target\'s turns before the spell ends, the target must succeed on a Wisdom Saving Throw or take 4d10 psychic damage. On a successful save, the spell ends.\n\nWhen you cast this spell using a spell slot of 5th level or higher, the damage increases by 1d10 for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Illusion',
        'concentration': True,

    },
    'polymorph': {
        'description': 'This spell transforms a creature that you can see within range into a new form. An unwilling creature must make a Wisdom Saving Throw to avoid the effect. The spell has no effect on a shapechanger or a creature with 0 hit points.\n\nThe transformation lasts for the duration, or until the target drops to 0 hit points or dies. The new form can be any beast whose challenge rating is equal to or less than the target\'s (or the target\'s level, if it doesn\'t have a challenge rating). The target\'s game statistics, including Mental Ability Scores, are replaced by the statistics of the chosen beast. It retains its alignment and personality.\n\nThe target assumes the hit points of its new form. When it reverts to its normal form, the creature returns to the number of hit points it had before it transformed. If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form. As long as the excess damage doesn\'t reduce the creature\'s normal form to 0 hit points, it isn\'t knocked unconscious.\n\nThe creature is limited in the actions it can perform by the nature of its new form, and it can\'t speak, cast spells, or take any other action that requires hands or speech.\n\nThe target\'s gear melds into the new form. The creature can\'t activate, use, wield, or otherwise benefit from any of its equipment.',
        'level': '4',
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a caterpillar cocoon)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Transmutation',
        'concentration': True,

    },
    'shadow of moil': {
        'description': 'Flame-like shadows wreathe your body until the spell ends, causing you to become heavily obscured to others. The shadows turn dim light within 10 feet of you into darkness, and bright light in the same area to dim light.\n\nUntil the spell ends, you have resistance to radiant damage. In addition, whenever a creature within 10 feet of you hits you with an attack, the shadows lash out at that creature, dealing it 2d8 necrotic damage.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Necromancy',
        'concentration': True,

    },
    'sickening radiance': {
        'description': 'Dim, greenish light spreads within a 30-foot-radius sphere centered on a point you choose within range. The light spreads around corners, and it lasts until the spell ends.\n\nWhen a creature moves into the spell\'s area for the first time on a turn or starts its turn there, that creature must succeed on a Constitution Saving Throw or take 4d10 radiant damage, and it suffers one level of exhaustion and emits a dim, greenish light in a 5-foot radius. This light makes it impossible for the creature to benefit from being invisible. The light and any levels of exhaustion caused by this spell go away when the spell ends.',
        'level': '4',
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

    },
    'staggering smite': {
        'description': 'The next time you hit a creature with a Melee Weapon Attack during this spell\'s duration, your weapon pierces both body and mind, and the attack deals an extra 4d6 psychic damage to the target. The target must make a Wisdom Saving Throw. On a failed save, it has disadvantage on Attack Rolls and Ability Checks, and can\'t take reactions, until the end of its next turn.',
        'level': '4',
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'stone shape': {
        'description': 'You touch a stone object of medium size or smaller or a section of stone no more than 5 feet in any dimension and form it into any shape that suits your purpose. So, for example, you could shape a large rock into a weapon, idol, or coffer, or make a small passage through a wall, as long as the wall is less than 5 feet thick. You could also shape a stone door or its frame to seal the door shut. The object you create can have up to two hinges and a latch, but finer mechanical detail isn\'t possible.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (soft clay, which must be worked into roughly the desired shape of the stone object)',
        'duration': 'Instantaneous',
        'school': 'Transmutation',


    },
    'stoneskin': {
        'description': 'This spell turns the flesh of a willing creature you touch as hard as stone. Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage.',
        'level': '4',
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (diamond dust worth 100 gp, which the spell consumes)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Abjuration',
        'concentration': True,

    },
    'storm sphere': {
        'description': 'A 20-foot-radius sphere of whirling air springs into existence, centered on a point you choose within range. The sphere remains for the spell\'s duration. Each creature in the sphere when it appears or that ends its turn there must succeed on a Strength Saving Throw or take 2d6 bludgeoning damage. The sphere\'s space is difficult terrain.\n\nUntil the spell ends, you can use a bonus action on each of your turns to cause a bolt of lightning to leap from the center of the sphere toward one creature you choose within 60 feet of the center. Make a Ranged Spell Attack. You have advantage on the Attack Roll if the target is in the sphere. On a hit, the target takes 4d6 lightning damage.\n\nCreatures within 30 feet of the sphere have disadvantage on Wisdom (Perception) checks made to listen.\n\nWhen you cast this spell using a spell slot of 5th level or higher, the damage for each of its effects increases by 1d6 for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S, M (a bit of tinsel, a pinch of powder made by crushing a clear gemstone, and a small, straight piece of iron)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'summon greater demon': {
        'description': 'You utter foul words, summoning one demon from the chaos of the Abyss. You choose the demon\'s type, which must be one of challenge rating 5 or lower, such as a Shadow Demon or a Barlgura. The demon appears in an unoccupied space you can see within range, and the demon disappears when it drops to 0 hit points or when the spell ends.\n\nRoll initiative for the demon, which has its own turns. When you summon it and on each of your turns thereafter, you can issue a verbal command to it (requiring no action on your part), telling it what it must do on its next turn. If you issue no command, it spends its turn attacking any creature within reach that has attacked it.\n\nAt the end of each of the demon\'s turns, it makes a Charisma Saving Throw. The demon has disadvantage on this Saving Throw if you say its true name. On a failed save, the demon continues to obey you. On a successful save, your control of the demon ends for the rest of the duration, and the demon spends its turns pursuing and attacking the nearest non-demons to the best of its ability. If you stop concentrating on the spell before it reaches its full duration, an uncontrolled demon doesn\'t disappear for 1d6 rounds if it still has hit points.\n\nAs part of casting the spell, you can form a circle on the ground with the blood used as a material component. The circle is large enough to encompass your space. While the spell lasts, the summoned demon can\'t cross the circle or harm it, and it can\'t target anyone within it. Using the material component in this manner consumes it when the spell ends.\n\nWhen you cast this spell using a spell slot of 5th level or higher, the challenge rating increases by 1 for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a vial of blood from a humanoid killed within the past 24 hours)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Conjuration',
        'concentration': True,

    },
    'vitriolic sphere': {
        'description': 'You point at a location within range, and a glowing 1-foot-diameter ball of emerald acid streaks there and explodes in a 20-foot-radius sphere. Each creature in that area must make a Dexterity Saving Throw. On a failed save, a creature takes 10d4 acid damage and another 5d4 acid damage at the end of its next turn. On a successful save, a creature takes half the initial damage and no damage at the end of its next turn.\n\nWhen you cast this spell using a spell slot of 5th level or higher, the initial damage increases by 2d4 for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'wall of fire': {
        'description': 'You create a wall of fire on a solid surface within range. You can make the wall up to 60 feet long, 20 feet high, and 1 foot thick, or a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick. The wall is opaque and lasts for the duration.\n\nWhen the wall appears, each creature within its area must make a Dexterity Saving Throw. On a failed save, a creature takes 5d8 fire damage, or half as much damage on a successful save.\n\nOne side of the wall, selected by you when you cast this spell, deals 5d8 fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage.\n\nWhen you cast this spell using a spell slot of 5th level or higher, the damage increases by 1d8 for each slot level above 4th.',
        'level': '4',
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M (a small piece of phosphorus)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'watery sphere': {
        'description': 'You conjure up a sphere of water with a 5-foot radius at a point you can see within range. The sphere can hover but no more than 10 feet off the ground. The sphere remains for the spell\'s duration.\n\nAny creature in the sphere\'s space must make a Strength Saving Throw. On a successful save, a creature is ejected from that space to the nearest unoccupied space of the creature\'s choice outside the sphere. A huge or larger creature succeeds on the Saving Throw automatically, and a large or smaller creature can choose to fail it. On a failed save, a creature is restrained by the sphere and is engulfed by the water. At the end of each of its turns, a restrained target can repeat the Saving Throw, ending the effect on itself on a success.\n\nThe sphere can restrain as many as four medium or smaller creatures or one large creature. If the sphere restrains a creature that causes it to exceed this capacity, a random creature that was already restrained by the sphere falls out of it and lands prone in a space within 5 feet of it.\n\nAs an action, you can move the sphere up to 30 feet in a straight line. If it moves over a pit, a cliff, or other drop-off, it safely descends until it is hovering 10 feet above the ground. Any creature restrained by the sphere moves with it. You can ram the sphere into creatures, forcing them to make the Saving Throw.\n\nWhen the spell ends, the sphere falls to the ground and extinguishes all normal flames within 30 feet of it. Any creature restrained by the sphere is knocked prone in the space where it falls. The water then vanishes.',
        'level': '4',
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S, M (a droplet of water)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

    }
}