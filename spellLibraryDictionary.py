#Template for spell dictionary
# spell = {
    # 'name': {
    #     'description':'',
    #     'level':'',
    #     'casting_time':'',
    #     'range':'',
    #     'components':'',
    #     'duration':'',
    #     'school':'',
    #     '':'',
    #     'Ritual':'', #True or False

    # },
# }


spells = {
    'acid_splash': {
        'description':'-You hurl a bubble of acid. Choose one creature you can see within range, or choose two creatures you can see within range that are within 5 feet of each other. A target must succeed on a Dexterity Saving Throw or take 1d6 acid damage. \n\n-This spell\'s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'60ft',
        'components':'Verbal, Somatic',
        'duration':'Instantaneous',
        'school':'Conjuration',

    },

        'blade_ward': {
        'description':'-You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by Weapon Attacks.',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'Self',
        'components':'Verbal, Somatic',
        'duration':'1 Round',
        'school':'Abjuration',

    },
        'booming_blade': {
        'description':'-As part of the action used to cast this spell, you must make a Melee Attack with a weapon against one creature within the spell\'s range, otherwise the spell fails. On a hit, the target suffers the attack\'s normal effects, and it becomes sheathed in booming energy until the start of your next turn. If the target willingly moves before then, it immediately takes 1d8 thunder damage, and the spell ends. \n-This spell\'s damage increases when you reach higher levels. At 5th level, the Melee Attack deals an extra 1d8 thunder damage to the target, and the damage the target takes for moving increases to 2d8. Both Damage Rolls increase by 1d8 at 11th level and 17th level.',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'5ft',
        'components':'Verbal, Material',
        'duration':'1 Round',
        'school':'Evocation',

    },
        'chill_touch': {
        'description':'-You create a ghostly, skeletal hand in the space of a creature within range. Make a Ranged Spell Attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can\'t regain hit points until the start of your next turn. Until then, the hand clings to the target. \n-If you hit an undead target, it also has disadvantage on Attack Rolls against you until the end of your next turn. \n-This spell\'s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'120ft',
        'components':'Verbal, Somatic',
        'duration':'1 Round',
        'school':'Necromancy',

    },

        'control_flames': {
        'description':'-You choose nonmagical flame that you can see within range and that fits within a 5-foot cube. You affect it in one of the following ways: \n     ⚫ You instantaneously expand the flame 5 feet in one direction, provided that wood or other fuel is present in the new location. \n     ⚫ You instantaneously extinguish the flames within the cube. \n      ⚫ You double or halve the area of bright light and dim light cast by the flame, change its color, or both. The change lasts for 1 hour. \n     ⚫ You cause simple shapes—such as the vague form of a creature, an inanimate object, or a location—to appear within the flames and animate as you like. The shapes last for 1 hour. \n-If you cast this spell multiple times, you can have up to three non-instantaneous effects created by it active at a time, and you can dismiss such an effect as an action.',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'60 ft',
        'components':'Somatic',
        'duration':'Special',
        'school':'transmutation',

    },

        'create_bonfire': {
        'description':'-You create a bonfire on ground that you can see within range. Until the spell ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire\'s space when you cast the spell must succeed on a Dexterity Saving Throw or take 1d8 fire damage. A creature must also make the Saving Throw when it moves into the bonfire\'s space for the first time on a turn or ends its turn there. \n\n-The bonfire ignites flammable objects in its area that aren\'t being worn or carried. \n\n-The spell\'s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8). ',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'60ft',
        'components':'Verbal, Somatic',
        'duration':'1 Minute',
        'school':'Conjuration',
        'concentration':'True',

    },

        'dancing_lights': {
        'description':'-You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius. \n-As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell\'s range.',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'120 ft',
        'components':'Verbal, Somatic, Material',
        'material_components':'a bit of phosphorus or wychwood, or a glowworm',
        'duration':'1 Minute',
        'school':'Evocation',
        'concentration':'True',

    },

        'druidcraft': {
        'description':'-Whispering to the spirits of nature, you create one of the following effects within range: \n     ⚫ You create a tiny, harmless sensory effect that predicts what the weather will be at your location for the next 24 hours. The effect might manifest as a golden orb for clear skies, a cloud for rain, falling snowflakes for snow, and so on. This effect persists for 1 round. \n     ⚫ You instantly make a flower blossom, a seed pod open, or a leaf bud bloom. \n     ⚫ You create an instantaneous, harmless sensory effect, such as falling leaves, a puff of wind, the sound of a small animal, or the faint odor of skunk. The effect must fit in a 5-foot cube. \n     ⚫ You instantly light or snuff out a candle, a torch, or a small campfire.',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'30ft',
        'components':'Verbal, Somatic',
        'duration':'Instantaneous',
        'school':'Transmutation',

    },

        'eldritch_blast': {
        'description':'-A beam of crackling energy streaks toward a creature within range. Make a Ranged Spell Attack against the target. On a hit, the target takes 1d10 force damage.\n\n-The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level. You can direct the beams at the same target or at different ones. Make a separate Attack Roll for each beam.',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'120 ft',
        'components':'Verbal, Somatic',
        'duration':'Instantaneous',
        'school':'Evocation',

    },

        'encode_thoughts': {
        'description':'-Putting a finger to your head, you pull a memory, an idea, or a message from your mind and transform it into a tangible string of glowing energy called a thought strand, which persists for the duration or until you cast this spell again. The thought strand appears in an unoccupied space within 5 feet of you as a tiny, weightless, semisolid object that can be held and carried like a ribbon. It is otherwise stationary.\n\n-If you cast this spell while concentrating on a spell or an ability that allows you to read or manipulate the thoughts of others (such as detect thoughts or modify memory), you can transform the thoughts or memories you read, rather than your own, into a thought strand.\n\nCasting this spell while holding a thought strand allows you to instantly receive whatever memory, idea, or message the thought strand contains. (Casting detect thoughts on the strand has the same effect.)',
        'level':'Cantrip',
        'casting_time':'Action',
        'range':'Self',
        'components':'Somatic',
        'duration':'8 Hours',
        'school':'Enchantment',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },

        'name': {
        'description':'-',
        'level':'',
        'casting_time':'',
        'range':'',
        'components':'',
        'duration':'',
        'school':'',
        '':'',

    },
}

