cr_20_monsters = {
    "Ancient Brass Dragon": {
        "hit_points": "297 (17d20 + 119)",
        "armor_class": 20,
        "speed": "40 ft., burrow 40 ft., fly 80 ft.",
        "size": "Gargantuan",
        "type": "Dragon",
        "alignment": "Chaotic Good",
        "challenge": "20",
        "abilities": {
            "Strength": 27,
            "Dexterity": 10,
            "Constitution": 25,
            "Intelligence": 16,
            "Wisdom": 15,
            "Charisma": 19
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+13",
            "Wisdom": "+9",
            "Charisma": "+11"
        },
        "skills": {
            "Perception": "+16",
            "Stealth": "+7"
        },
        "damage_immunities": "fire",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 26",
        "languages": "Common, Draconic",
        "special_traits": {
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Magic Resistance": "The dragon has advantage on saving throws against spells and other magical effects.",
            "Actions": {
                "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
                "Bite": "Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 20 (2d10 + 9) piercing damage.",
                "Claw": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 16 (2d6 + 9) slashing damage.",
                "Tail": "Melee Weapon Attack: +16 to hit, reach 20 ft., one target. Hit: 18 (2d8 + 9) bludgeoning damage.",
                "Breath Weapons (Recharge 5-6)": "The dragon uses one of the following breath weapons:",
                "Change Shape": "The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies.",
                "Legendary Actions": {
                    "Detect": "The dragon makes a Wisdom (Perception) check.",
                    "Tail Attack": "The dragon makes a tail attack.",
                    "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 24 Dexterity saving throw or take 14 (2d6 + 7) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
                }
            }
        }
    },
    "Ancient White Dragon": {
        "hit_points": "333 (18d20 + 144)",
        "armor_class": 20,
        "speed": "40 ft., burrow 40 ft., fly 80 ft., swim 40 ft.",
        "size": "Gargantuan",
        "type": "Dragon",
        "alignment": "Chaotic Evil",
        "challenge": "20",
        "abilities": {
            "Strength": 26,
            "Dexterity": 10,
            "Constitution": 26,
            "Intelligence": 10,
            "Wisdom": 13,
            "Charisma": 14
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+13",
            "Wisdom": "+7",
            "Charisma": "+8"
        },
        "skills": {
            "Perception": "+14",
            "Stealth": "+6"
        },
        "damage_immunities": "cold",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 24",
        "languages": "Common, Draconic",
        "special_traits": {
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Ice Walk": "The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra moment.",
            "Magic Resistance": "The dragon has advantage on saving throws against spells and other magical effects.",
            "Actions": {
                "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
                "Bite": "Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 20 (2d10 + 9) piercing damage plus 9 (2d8) cold damage.",
                "Claw": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 16 (2d6 + 9) slashing damage.",
                "Tail": "Melee Weapon Attack: +16 to hit, reach 20 ft., one target. Hit: 18 (2d8 + 9) bludgeoning damage.",
                "Cold Breath (Recharge 5-6)": "The dragon exhales an icy blast in a 90-foot cone. Each creature in that area must make a DC 21 Constitution saving throw, taking 72 (16d8) cold damage on a failed save, or half as much damage on a successful one.",
                "Legendary Actions": {
                    "Detect": "The dragon makes a Wisdom (Perception) check.",
                    "Tail Attack": "The dragon makes a tail attack.",
                    "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 24 Dexterity saving throw or take 14 (2d6 + 7) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
                }
            }
        }
    },
    "Pit Fiend": {
        "hit_points": "300 (24d10 + 168)",
        "armor_class": 19,
        "speed": "30 ft., fly 60 ft.",
        "size": "Large",
        "type": "Fiend (Devil)",
        "alignment": "Lawful Evil",
        "challenge": "20",
        "abilities": {
            "Strength": 26,
            "Dexterity": 14,
            "Constitution": 24,
            "Intelligence": 22,
            "Wisdom": 18,
            "Charisma": 24
        },
        "saving_throws": {
            "Dexterity": "+9",
            "Constitution": "+14",
            "Wisdom": "+10",
            "Charisma": "+14"
        },
        "skills": {
            "Perception": "+12"
        },
        "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "damage_immunities": "fire, poison",
        "condition_immunities": "poisoned",
        "senses": "Darkvision 120 ft., Passive Perception 22",
        "languages": "Infernal, telepathy 120 ft.",
        "special_traits": {
            "Devil's Sight": "Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance": "The pit fiend has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons": "The pit fiend's weapon attacks are magical.",
            "Actions": {
                "Multiattack": "The pit fiend can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claw.",
                "Bite": "Melee Weapon Attack: +16 to hit, reach 5 ft., one target. Hit: 19 (3d6 + 9) piercing damage.",
                "Claw": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 15 (2d6 + 9) slashing damage.",
                "Fist": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) bludgeoning damage.",
                "Fireball (Recharge 5-6)": "The pit fiend hurls a fireball at a point it can see within 150 feet of it. Each creature in a 20-foot-radius sphere centered on that point must make a DC 21 Dexterity saving throw. The sphere spreads around corners. A creature takes 63 (18d6) fire damage and 63 (18d6) radiant damage on a failed save, or half as much damage on a successful one.",
                "Fear (Recharge 5-6)": "The pit fiend magically generates intense fear in a 60-foot cone. Each creature in that area must succeed on a DC 21 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
                "Teleport": "The pit fiend magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.",
                "Summon Devil (1/Day)": "The pit fiend chooses what to summon and attempts a magical summoning.",
                "Legendary Actions": {
                    "Detect": "The pit fiend makes a Wisdom (Perception) check.",
                    "Tail Attack": "The pit fiend makes a tail attack.",
                    "Teleport (Costs 2 Actions)": "The pit fiend magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.",
                    "Flame Strike (Costs 3 Actions)": "The pit fiend invokes a divine flame in a 10-foot-radius, 40-foot-high cylinder centered on a point within 120 feet of it. The flame spreads around corners. Each creature in that area must make a DC 21 Dexterity saving throw, taking 63 (14d8) fire damage and 63 (14d8) radiant damage on a failed save, or half as much damage on a successful one."
                }
            }
        }
    }
}
