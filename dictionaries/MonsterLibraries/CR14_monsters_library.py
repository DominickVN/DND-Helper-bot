cr_14_monsters = {
    "Adult Black Dragon": {
        "hit_points": "195 (17d12 + 85)",
        "armor_class": 19,
        "speed": "40 ft., fly 80 ft., swim 40 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Chaotic Evil",
        "challenge": "14",
        "abilities": {
            "Strength": 23,
            "Dexterity": 14,
            "Constitution": 21,
            "Intelligence": 14,
            "Wisdom": 13,
            "Charisma": 17
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+10",
            "Wisdom": "+7",
            "Charisma": "+8"
        },
        "skills": {
            "Perception": "+11",
            "Stealth": "+7"
        },
        "damage_immunities": "acid",
        "damage_resistances": "cold",
        "damage_vulnerabilities": "psychic",
        "condition_immunities": "blinded, prone",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 21",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": {
                "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
                "Bite": "Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 4 (1d8) acid damage.",
                "Claw": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.",
                "Tail": "Melee Weapon Attack: +11 to hit, reach 15 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage.",
                "Frightful Presence": "Each creature of the dragon's choice within 120 feet of it and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
            },
            "Legendary Actions": {
                "Detect": "The dragon makes a Wisdom (Perception) check.",
                "Tail Attack": "The dragon makes a tail attack.",
                "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 19 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
            }
        }
    },
    "Adult Copper Dragon": {
        "hit_points": "184 (16d12 + 80)",
        "armor_class": 18,
        "speed": "40 ft., climb 40 ft., fly 80 ft., swim 40 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Chaotic Good",
        "challenge": "14",
        "abilities": {
            "Strength": 23,
            "Dexterity": 12,
            "Constitution": 21,
            "Intelligence": 18,
            "Wisdom": 15,
            "Charisma": 17
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+10",
            "Wisdom": "+7",
            "Charisma": "+9"
        },
        "skills": {
            "Perception": "+11",
            "Stealth": "+6"
        },
        "damage_immunities": "acid",
        "damage_resistances": "fire",
        "condition_immunities": "charmed",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 21",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": {
                "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
                "Bite": "Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 9 (2d8) acid damage.",
                "Claw": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.",
                "Acid Breath (Recharge 5-6)": "The dragon exhales acid in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 18 Dexterity saving throw, taking 54 (12d8) acid damage on a failed save, or half as much damage on a successful one."
            },
            "Legendary Actions": {
                "Detect": "The dragon makes a Wisdom (Perception) check.",
                "Tail Attack": "The dragon makes a tail attack.",
                "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 21 Dexterity saving throw or take 14 (2d6 + 7) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
            }
        }
    },
    "Ice Devil": {
        "hit_points": "180 (19d10 + 76)",
        "armor_class": 18,
        "speed": "40 ft., fly 120 ft.",
        "size": "Large",
        "type": "Fiend",
        "alignment": "Lawful Evil",
        "challenge": "14",
        "abilities": {
            "Strength": 21,
            "Dexterity": 14,
            "Constitution": 18,
            "Intelligence": 18,
            "Wisdom": 15,
            "Charisma": 18
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+8",
            "Wisdom": "+6",
            "Charisma": "+8"
        },
        "skills": {
            "Deception": "+8",
            "Insight": "+6",
            "Perception": "+6",
            "Persuasion": "+8",
            "Stealth": "+7"
        },
        "damage_resistances": "bludgeoning, piercing, and slashing from nonmagical weapons that aren't silvered",
        "damage_immunities": "cold",
        "condition_immunities": "exhaustion, petrified, poisoned",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 16",
        "languages": "Infernal, Telepathy 120 ft.",
        "special_traits": {
            "Devil's Sight": "Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance": "The devil has advantage on saving throws against spells and other magical effects.",
            "Actions": {
                "Multiattack": "The devil makes three attacks: one with its trident and two with its claws.",
                "Trident": "Melee or Ranged Weapon Attack: +10 to hit, reach 10 ft. or range 20/60 ft., one target. Hit: 13 (2d6 + 6) piercing damage plus 10 (3d6) cold damage.",
                "Claw": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage plus 10 (3d6) cold damage.",
                "Tail": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage."
            },
            "Legendary Actions": {
                "Detect": "The devil makes a Wisdom (Perception) check.",
                "Tail Spike": "The devil flings a tail spike up to 20 feet that then explodes. Each creature within 10 feet of the spike must succeed on a DC 18 Dexterity saving throw or take 14 (4d6) piercing damage and 14 (4d6) cold damage."
            }
        }
    }
}
