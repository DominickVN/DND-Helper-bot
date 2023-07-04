cr_13_monsters = {
    "Adult Brass Dragon": {
        "hit_points": "172 (15d12 + 75)",
        "armor_class": 18,
        "speed": "40 ft., burrow 40 ft., fly 80 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Chaotic Good",
        "challenge": "13",
        "abilities": {
            "Strength": 23,
            "Dexterity": 10,
            "Constitution": 21,
            "Intelligence": 14,
            "Wisdom": 13,
            "Charisma": 17
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+10",
            "Wisdom": "+7",
            "Charisma": "+9"
        },
        "skills": {
            "Perception": "+12",
            "Stealth": "+6"
        },
        "damage_immunities": "fire",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 22",
        "languages": "Common, Draconic",
        "special_traits": {
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": "Multiattack: The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite": "Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage.",
            "Claw": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.",
            "Breath Weapons (Recharge 5-6)": "The dragon uses one of the following breath weapons:",
            "Legendary Actions": "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Fire Breath (Recharge 5-6)": "The dragon exhales fire in a 60-foot cone. Each creature in that area must make a DC 18 Dexterity saving throw, taking 54 (12d8) fire damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Adult White Dragon": {
        "hit_points": "200 (16d12 + 96)",
        "armor_class": 18,
        "speed": "40 ft., burrow 20 ft., fly 80 ft., swim 40 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Chaotic Evil",
        "challenge": "13",
        "abilities": {
            "Strength": 22,
            "Dexterity": 10,
            "Constitution": 22,
            "Intelligence": 8,
            "Wisdom": 12,
            "Charisma": 12
        },
        "saving_throws": {
            "Dexterity": "+5",
            "Constitution": "+10",
            "Wisdom": "+6",
            "Charisma": "+6"
        },
        "skills": {
            "Perception": "+11",
            "Stealth": "+5"
        },
        "damage_immunities": "cold",
        "senses": "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 21",
        "languages": "Common, Draconic",
        "special_traits": {
            "Ice Walk": "The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra movement.",
            "Actions": "Multiattack: The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 19 (2d10 + 8) piercing damage plus 9 (2d8) cold damage.",
            "Claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 15 (2d6 + 8) slashing damage.",
            "Cold Breath (Recharge 5-6)": "The dragon exhales an icy blast in a 60-foot cone. Each creature in that area must make a DC 19 Constitution saving throw, taking 54 (12d8) cold damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Nalfeshnee": {
        "hit_points": "184 (16d10 + 96)",
        "armor_class": 18,
        "speed": "20 ft., fly 60 ft.",
        "size": "Large",
        "type": "Fiend (Demon)",
        "alignment": "Chaotic Evil",
        "challenge": "13",
        "abilities": {
            "Strength": 21,
            "Dexterity": 10,
            "Constitution": 22,
            "Intelligence": 19,
            "Wisdom": 12,
            "Charisma": 15
        },
        "saving_throws": {
            "Intelligence": "+9",
            "Wisdom": "+6",
            "Charisma": "+7"
        },
        "skills": {
            "Arcana": "+9",
            "Deception": "+7",
            "Insight": "+6",
            "Perception": "+6"
        },
        "damage_resistances": "cold, fire, lightning",
        "damage_immunities": "poison; bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "poisoned",
        "senses": "Truesight 120 ft., Passive Perception 16",
        "languages": "Abyssal, telepathy 120 ft.",
        "special_traits": {
            "Magic Resistance": "The nalfeshnee has advantage on saving throws against spells and other magical effects.",
            "Innate Spellcasting": "The nalfeshnee's innate spellcasting ability is Intelligence (spell save DC 17). It can innately cast the following spells, requiring no material components:",
            "Actions": "Multiattack: The nalfeshnee uses Horrific Appearance if it can. It then makes two attacks: one with its bite and one with its claws.",
            "Bite": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 20 (4d6 + 6) piercing damage.",
            "Claws": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 15 (3d6 + 6) slashing damage."
        },
        "spellcasting": {
            "At will": [
                "detect magic",
                "dispel magic",
                "polymorph"
            ],
            "1/day each": [
                "dominate monster",
                "power word stun"
            ]
        }
    },
    "Rakshasa": {
        "hit_points": "110 (13d8 + 52)",
        "armor_class": 16,
        "speed": "40 ft.",
        "size": "Medium",
        "type": "Fiend (Shapechanger)",
        "alignment": "Lawful Evil",
        "challenge": "13",
        "abilities": {
            "Strength": 14,
            "Dexterity": 17,
            "Constitution": 18,
            "Intelligence": 13,
            "Wisdom": 16,
            "Charisma": 20
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Intelligence": "+5",
            "Wisdom": "+6",
            "Charisma": "+9"
        },
        "skills": {
            "Deception": "+16",
            "Insight": "+9",
            "Perception": "+9",
            "Stealth": "+11"
        },
        "damage_immunities": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, frightened",
        "senses": "Darkvision 60 ft., Passive Perception 19",
        "languages": "Common, Infernal",
        "special_traits": {
            "Limited Magic Immunity": "The rakshasa can't be affected or detected by spells of 6th level or lower unless it wishes to be.",
            "Innate Spellcasting": "The rakshasa's innate spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material components:",
            "Shapechanger": "The rakshasa can use its action to polymorph into a Small or Medium humanoid, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Actions": "Multiattack: The rakshasa makes two claw attacks.",
            "Claw": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage. If the target is a creature cursed by the rakshasa's Limited Magic Immunity trait, the target must succeed on a DC 15 Wisdom saving throw or be magically banished to its home plane of existence. If the target's saving throw is successful, the target is no longer cursed by the rakshasa."
        },
        "spellcasting": {
            "At will": [
                "detect thoughts",
                "disguise self",
                "invisibility",
                "major image"
            ],
            "3/day each": [
                "charm person",
                "plane shift",
                "suggestion"
            ],
            "1/day each": [
                "dominate person",
                "project image"
            ]
        }
    },
    "Storm Giant": {
        "hit_points": "230 (20d12 + 100)",
        "armor_class": 16,
        "speed": "50 ft., swim 50 ft.",
        "size": "Huge",
        "type": "Giant",
        "alignment": "Chaotic Good",
        "challenge": "13",
        "abilities": {
            "Strength": 29,
            "Dexterity": 14,
            "Constitution": 20,
            "Intelligence": 16,
            "Wisdom": 18,
            "Charisma": 18
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+10",
            "Wisdom": "+9",
            "Charisma": "+9"
        },
        "skills": {
            "Athletics": "+17",
            "Perception": "+9",
            "Persuasion": "+9"
        },
        "damage_immunities": "lightning, thunder",
        "condition_immunities": "frightened",
        "senses": "Passive Perception 19",
        "languages": "Common, Giant",
        "special_traits": {
            "Amphibious": "The giant can breathe air and water.",
            "Innate Spellcasting": "The giant's innate spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material components:",
            "Actions": "Multiattack: The giant makes two greatsword attacks.",
            "Greatsword": "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 30 (6d6 + 9) slashing damage.",
            "Rock": "Ranged Weapon Attack: +14 to hit, range 60/240 ft., one target. Hit: 35 (4d12 + 9) bludgeoning damage."
        },
        "spellcasting": {
            "At will": [
                "detect magic",
                "feather fall",
                "levitate",
                "lightning bolt"
            ],
            "3/day each": [
                "control weather",
                "gust of wind",
                "water breathing"
            ],
            "1/day each": [
                "chain lightning",
                "hurl lightning",
                "wind walk"
            ]
        }
    },
    "Vampire": {
        "hit_points": "144 (17d8 + 68)",
        "armor_class": 16,
        "speed": "30 ft., fly 30 ft.",
        "size": "Medium",
        "type": "Undead",
        "alignment": "Lawful Evil",
        "challenge": "13",
        "abilities": {
            "Strength": 18,
            "Dexterity": 18,
            "Constitution": 18,
            "Intelligence": 17,
            "Wisdom": 15,
            "Charisma": 18
        },
        "saving_throws": {
            "Wisdom": "+6",
            "Charisma": "+8"
        },
        "skills": {
            "Perception": "+10",
            "Stealth": "+8"
        },
        "damage_resistances": "necrotic, bludgeoning, piercing, and slashing from nonmagical attacks",
        "damage_immunities": "necrotic, poison",
        "condition_immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
        "senses": "Darkvision 120 ft., Passive Perception 20",
        "languages": "Common",
        "special_traits": {
            "Shapechanger": "If the vampire isn't in sunlight or running water, it can use its action to polymorph into a Tiny bat or a Medium cloud of mist, or back into its true form.",
            "Legendary Resistance (3/Day)": "If the vampire fails a saving throw, it can choose to succeed instead.",
            "Misty Escape": "When it drops to 0 hit points outside its resting place, the vampire transforms into a cloud of mist (as in the Shapechanger trait) instead of falling unconscious, provided that it isn't in sunlight or running water. If it can't transform, it is destroyed.",
            "Regeneration": "The vampire regains 20 hit points at the start of its turn if it has at least 1 hit point and isn't in sunlight or running water. If the vampire takes radiant damage or damage from holy water, this trait doesn't function at the start of the vampire's next turn.",
            "Spider Climb": "The vampire can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Actions": "Multiattack: The vampire makes two attacks, only one of which can be a bite attack.",
            "Bite": "Melee Weapon Attack: +10 to hit, reach 5 ft., one willing creature, or a creature that is grappled by the vampire, incapacitated, or restrained. Hit: 7 (1d6 + 4) piercing damage plus 10 (3d6) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken, and the vampire regains hit points equal to that amount. The reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. A humanoid slain in this way and then buried in the ground rises the following night as a vampire spawn under the vampire's control.",
            "Charm": "The vampire targets one humanoid it can see within 30 feet of it. If the target can see the vampire, the target must succeed on a DC 15 Wisdom saving throw against this magic or be charmed by the vampire. The charmed target regards the vampire as a trusted friend to be heeded and protected. Although the target isn't under the vampire's control, it takes the vampire's requests or actions in the most favorable way it can, and it is a willing target for the vampire's bite attack.",
            "Legendary Actions": "The vampire can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The vampire regains spent legendary actions at the start of its turn.",
            "Move": "The vampire moves up to its speed without provoking opportunity attacks.",
            "Unarmed Strike": "The vampire makes one unarmed strike.",
            "Bite (Costs 2 Actions)": "The vampire makes one bite attack."
        }
    }
}
