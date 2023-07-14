cr_15_monsters = {
    "Adult Bronze Dragon": {
        "hit_points": "212 (17d12 + 102)",
        "armor_class": 19,
        "speed": "40 ft., fly 80 ft., swim 40 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Lawful Good",
        "challenge": "15",
        "abilities": {
            "Strength": 25,
            "Dexterity": 10,
            "Constitution": 23,
            "Intelligence": 16,
            "Wisdom": 15,
            "Charisma": 19
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+11",
            "Wisdom": "+8",
            "Charisma": "+10"
        },
        "skills": {
            "Perception": "+14",
            "Stealth": "+6"
        },
        "damage_immunities": "lightning",
        "damage_resistances": "cold",
        "condition_immunities": "paralyzed",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 24",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": {
                "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
                "Bite": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 19 (2d10 + 8) piercing damage.",
                "Claw": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 15 (2d6 + 8) slashing damage.",
                "Tail": "Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 17 (2d8 + 8) bludgeoning damage.",
                "Breath Weapons (Recharge 5-6)": "The dragon uses one of the following breath weapons:",
                "1. Lightning Breath": "The dragon exhales lightning in a 90-foot line that is 5 feet wide. Each creature in that line must make a DC 19 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one.",
                "2. Repulsion Breath": "The dragon exhales repulsion energy in a 60-foot cone. Each creature in that area must succeed on a DC 19 Strength saving throw. On a failed save, the creature is pushed 60 feet away from the dragon.",
                "Legendary Actions": {
                    "Detect": "The dragon makes a Wisdom (Perception) check.",
                    "Tail Attack": "The dragon makes a tail attack.",
                    "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 21 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
                }
            }
        }
    },
    "Adult Green Dragon": {
        "hit_points": "207 (18d12 + 90)",
        "armor_class": 19,
        "speed": "40 ft., fly 80 ft., swim 40 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Lawful Evil",
        "challenge": "15",
        "abilities": {
            "Strength": 23,
            "Dexterity": 12,
            "Constitution": 21,
            "Intelligence": 18,
            "Wisdom": 15,
            "Charisma": 17
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+10",
            "Wisdom": "+8",
            "Charisma": "+9"
        },
        "skills": {
            "Deception": "+9",
            "Insight": "+8",
            "Perception": "+14",
            "Stealth": "+7"
        },
        "damage_immunities": "poison",
        "condition_immunities": "poisoned",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 24",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": {
                "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
                "Bite": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 19 (2d10 + 8) piercing damage plus 10 (3d6) poison damage.",
                "Claw": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 15 (2d6 + 8) slashing damage.",
                "Tail": "Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 17 (2d8 + 8) bludgeoning damage.",
                "Breath Weapon (Recharge 5-6)": "The dragon exhales poisonous gas in a 90-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 63 (18d6) poison damage on a failed save, or half as much damage on a successful one.",
                "Legendary Actions": {
                    "Detect": "The dragon makes a Wisdom (Perception) check.",
                    "Tail Attack": "The dragon makes a tail attack.",
                    "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 21 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
                }
            }
        }
    },
    "Mummy Lord": {
        "hit_points": "97 (13d8 + 39)",
        "armor_class": 17,
        "speed": "20 ft.",
        "size": "Medium",
        "type": "Undead",
        "alignment": "Lawful Evil",
        "challenge": "15",
        "abilities": {
            "Strength": 18,
            "Dexterity": 10,
            "Constitution": 17,
            "Intelligence": 11,
            "Wisdom": 18,
            "Charisma": 16
        },
        "saving_throws": {
            "Constitution": "+9",
            "Wisdom": "+9"
        },
        "skills": {
            "History": "+5",
            "Religion": "+5"
        },
        "damage_immunities": "necrotic, poison, bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
        "senses": "Darkvision 60 ft., Passive Perception 14",
        "languages": "The languages it knew in life",
        "special_traits": {
            "Magic Resistance": "The mummy lord has advantage on saving throws against spells and other magical effects.",
            "Rejuvenation": "A destroyed mummy lord gains a new body in 24 hours if its heart is intact, regaining all its hit points and becoming active again. The new body appears within 5 feet of the mummy lord’s heart.",
            "Actions": {
                "Multiattack": "The mummy lord can use its Dreadful Glare and makes one attack with its rotting fist.",
                "Rotting Fist": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14 (3d6 + 4) bludgeoning damage plus 21 (6d6) necrotic damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic.",
                "Dreadful Glare": "The mummy lord targets one creature it can see within 60 feet of it. If the target can see the mummy lord, it must succeed on a DC 16 Wisdom saving throw against this magic or become frightened until the end of the mummy lord's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all mummy lords for the next 24 hours.",
                "Blinding Dust": "Blinding dust and sand swirls magically around the mummy lord. Each creature within 5 feet of the mummy lord must succeed on a DC 16 Constitution saving throw or be blinded until the end of the creature's next turn.",
                "Summon Undead (1/Day)": "The mummy lord magically summons one mummy or one mummy lord."
            }
        }
    },
    "Purple Worm": {
        "hit_points": "247 (15d20 + 90)",
        "armor_class": 18,
        "speed": "50 ft., burrow 30 ft.",
        "size": "Gargantuan",
        "type": "Monstrosity",
        "alignment": "Unaligned",
        "challenge": "15",
        "abilities": {
            "Strength": 28,
            "Dexterity": 7,
            "Constitution": 22,
            "Intelligence": 1,
            "Wisdom": 8,
            "Charisma": 4
        },
        "saving_throws": {
            "Dexterity": "-1",
            "Constitution": "+11"
        },
        "damage_immunities": "acid",
        "condition_immunities": "blinded, charmed, deafened, frightened, prone",
        "senses": "Blindsight 30 ft., tremorsense 60 ft., Passive Perception 9",
        "languages": "None",
        "special_traits": {
            "Tunneler": "The worm can burrow through solid rock at half its burrow speed and leaves a 10-foot-diameter tunnel in its wake.",
            "Actions": {
                "Multiattack": "The worm makes two attacks: one with its bite and one with its stinger.",
                "Bite": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 22 (3d8 + 9) piercing damage. If the target is a creature, it must succeed on a DC 19 Constitution saving throw or take 42 (12d6) poison damage and become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
                "Stinger": "Melee Weapon Attack: +10 to hit, reach 10 ft., one creature. Hit: 17 (2d10 + 6) piercing damage. If the target is a creature, it must succeed on a DC 19 Constitution saving throw or take 42 (12d6) poison damage and become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
                "Acid Spray (Recharge 5-6)": "The worm exhales a 60-foot cone of acid. Each creature in that area must make a DC 19 Dexterity saving throw, taking 66 (12d10) acid damage on a failed save, or half as much damage on a successful one."
            }
        }
    }
}
