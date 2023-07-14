cr_30_monsters = {
    "Tarrasque": {
        "hit_points": "676 (33d20 + 330)",
        "armor_class": 25,
        "speed": "40 ft., burrow 40 ft.",
        "size": "Gargantuan",
        "type": "Monstrosity",
        "alignment": "Unaligned",
        "challenge": "30",
        "abilities": {
            "Strength": 30,
            "Dexterity": 11,
            "Constitution": 30,
            "Intelligence": 3,
            "Wisdom": 11,
            "Charisma": 11
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+19",
            "Wisdom": "+7",
            "Charisma": "+7"
        },
        "damage_immunities": "fire, poison; bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "blinded, charmed, deafened, frightened, poisoned",
        "senses": "Blindsight 120 ft., Passive Perception 10",
        "languages": "None",
        "special_traits": {
            "Legendary Resistance (5/Day)": "If the tarrasque fails a saving throw, it can choose to succeed instead.",
            "Magic Resistance": "The tarrasque has advantage on saving throws against spells and other magical effects.",
            "Reflective Carapace": "Any time the tarrasque is targeted by a magic missile spell, a line spell, or a spell that requires a ranged attack roll, roll a d6. On a 1 to 5, the tarrasque is unaffected. On a 6, the tarrasque is unaffected, and the effect is reflected back at the caster as though it originated from the tarrasque, turning the caster into the target.\n\n",
            "Actions": {
                "**Multiattack**": "The tarrasque can use its Frightful Presence. It then makes five attacks: one with its bite, two with its claws, one with its horns, and one with its tail.",
                "**Bite**": "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 36 (4d12 + 10) piercing damage. If the target is a creature, it is grappled (escape DC 20). Until this grapple ends, the target is restrained, and the tarrasque can't bite another target.",
                "**Claw**": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 28 (4d8 + 10) slashing damage.",
                "**Horns**": "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 32 (4d10 + 10) piercing damage.",
                "**Tail**": "Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 24 (4d6 + 10) bludgeoning damage. If the target is a creature, it must succeed on a DC 20 Strength saving throw or be knocked prone.",
                "**Frightful Presence**": "Each creature of the tarrasque's choice within 120 feet of it and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, with disadvantage if the tarrasque is within line of sight, ending the effect on itself on a success.",
                "**Swallow**": "The tarrasque makes one bite attack against a Large or smaller creature it is grappling. If the attack hits, the target takes the bite's damage, the target is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the tarrasque, and it takes 56 (16d6) acid damage at the start of each of the tarrasque's turns. If the tarrasque takes 60 damage or more on a single turn from a creature inside it, the tarrasque must succeed on a DC 20 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the tarrasque. If the tarrasque dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 30 feet of movement, exiting prone."
            }
        }
    }
}
