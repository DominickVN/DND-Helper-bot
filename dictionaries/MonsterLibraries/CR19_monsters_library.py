cr_19_monsters = {
    "Balor": {
        "hit_points": "262 (21d12 + 126)",
        "armor_class": 19,
        "speed": "40 ft., fly 80 ft.",
        "size": "Huge",
        "type": "Fiend (Demon)",
        "alignment": "Chaotic Evil",
        "challenge": "19",
        "abilities": {
            "Strength": 26,
            "Dexterity": 15,
            "Constitution": 22,
            "Intelligence": 20,
            "Wisdom": 16,
            "Charisma": 22
        },
        "saving_throws": {
            "Strength": "+14",
            "Dexterity": "+8",
            "Constitution": "+12",
            "Intelligence": "+11",
            "Wisdom": "+9",
            "Charisma": "+12"
        },
        "skills": {
            "Perception": "+9",
            "Stealth": "+8"
        },
        "damage_resistances": "cold, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "damage_immunities": "fire, poison",
        "condition_immunities": "poisoned",
        "senses": "Truesight 120 ft., Passive Perception 19",
        "languages": "Abyssal, telepathy 120 ft.",
        "special_traits": {
            "Death Throes": "When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successful one. The explosion ignites flammable objects in that area that aren't being worn or carried.",
            "Magic Resistance": "The balor has advantage on saving throws against spells and other magical effects.",
            "Actions": {
                "Multiattack": "The balor makes two attacks: one with its longsword and one with its whip.",
                "Longsword": "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) slashing damage plus 13 (3d8) lightning damage. If the balor scores a critical hit, it rolls damage dice three times, instead of twice.",
                "Whip": "Melee Weapon Attack: +14 to hit, reach 30 ft., one target. Hit: 15 (2d6 + 8) slashing damage plus 10 (3d6) fire damage, and the target must succeed on a DC 20 Strength saving throw or be pulled up to 25 feet toward the balor.",
                "Teleport (Recharge 4-6)": "The balor magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see."
            },
            "Legendary Actions": {
                "Attack": "The balor makes one melee or ranged attack.",
                "Fire Storm (Costs 3 Actions)": "The balor casts fire storm. The balor can't use this legendary action if it used the teleport action during its turn."
            }
        }
    }
}
