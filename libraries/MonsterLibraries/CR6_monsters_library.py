cr_6_monsters = {
    "Chimera": {
        "hit_points": "114 (12d12 + 36)",
        "armor_class": 14,
        "speed": "30 ft., fly 60 ft.",
        "size": "Large",
        "type": "Monstrosity",
        "alignment": "Chaotic Evil",
        "challenge": "6",
        "abilities": {
            "Strength": 16,
            "Dexterity": 14,
            "Constitution": 16,
            "Intelligence": 3,
            "Wisdom": 12,
            "Charisma": 8
        },
        "saving_throws": {
            "Dexterity": "+5",
            "Constitution": "+6",
            "Wisdom": "+4"
        },
        "skills": {
            "Perception": "+4"
        },
        "damage_immunities": "Fire",
        "senses": "Darkvision 60 ft., passive Perception 14",
        "languages": "Understands Draconic but can't speak",
        "special_traits": {
            "Fire Breath (Recharge 5-6)": "The chimera exhales fire in a 15-foot cone. Each creature in that area must make a DC 14 Dexterity saving throw, taking 31 (7d8) fire damage on a failed save, or half as much damage on a successful one."
        },
        "actions": {
            "Multiattack": "The chimera makes three attacks: one with its bite, one with its horns, and one with its claws.",
            "Bite": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (1d10 + 6) piercing damage.",
            "Horns": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10 (1d8 + 6) bludgeoning damage.",
            "Claws": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 6) slashing damage."
        }
    },
    "Drider": {
        "hit_points": "123 (13d10 + 52)",
        "armor_class": 19,
        "speed": "30 ft., climb 30 ft.",
        "size": "Large",
        "type": "Monstrosity",
        "alignment": "Chaotic Evil",
        "challenge": "6",
        "abilities": {
            "Strength": 16,
            "Dexterity": 16,
            "Constitution": 18,
            "Intelligence": 13,
            "Wisdom": 14,
            "Charisma": 12
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+7",
            "Wisdom": "+5"
        },
        "skills": {
            "Perception": "+5",
            "Stealth": "+6"
        },
        "damage_immunities": "Poison",
        "condition_immunities": "Poisoned",
        "senses": "Darkvision 120 ft., passive Perception 15",
        "languages": "Elvish, Undercommon",
        "special_traits": {
            "Innate Spellcasting": "The drider's innate spellcasting ability is Wisdom (spell save DC 13). The drider can innately cast the following spells, requiring no material components:\n\nAt will: dancing lights\n1/day each: darkness, faerie fire"
        },
        "actions": {
            "Multiattack": "The drider makes three attacks: two with its longsword and one with its longbow.",
            "Longsword": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.",
            "Longbow": "Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) poison damage."
        },
        "reactions": {
            "Parry": "The drider adds 3 to its AC against one melee attack that would hit it. To do so, the drider must see the attacker and be wielding a melee weapon."
        }
    },
    "Invisible Stalker": {
        "hit_points": "104 (16d8 + 32)",
        "armor_class": 14,
        "speed": "50 ft., fly 50 ft.",
        "size": "Medium",
        "type": "Elemental",
        "alignment": "Neutral",
        "challenge": "6",
        "abilities": {
            "Strength": 16,
            "Dexterity": 19,
            "Constitution": 14,
            "Intelligence": 10,
            "Wisdom": 15,
            "Charisma": 11
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Wisdom": "+5"
        },
        "damage_resistances": "Bludgeoning, Piercing, and Slashing from Nonmagical Attacks",
        "damage_immunities": "Poison",
        "condition_immunities": "Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious",
        "senses": "Darkvision 60 ft., passive Perception 12",
        "languages": "Auran",
        "special_traits": {
            "Invisibility": "The stalker is invisible."
        },
        "actions": {
            "Multiattack": "The stalker makes two slam attacks.",
            "Slam": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage."
        },
        "reactions": {
            "Whirlwind": "Each creature in the stalker's space must make a DC 15 Strength saving throw. On a failure, a target takes 15 (3d8 + 2) bludgeoning damage and is flung up to 30 feet away from the stalker in a random direction and knocked prone. If a thrown target strikes an object, such as a wall or floor, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 15 Dexterity saving throw or take the same damage and be knocked prone."
        }
    },
    "Mage": {
        "hit_points": "40 (9d8)",
        "armor_class": 12,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid (any race)",
        "alignment": "Any",
        "challenge": "6",
        "abilities": {
            "Strength": 9,
            "Dexterity": 14,
            "Constitution": 11,
            "Intelligence": 17,
            "Wisdom": 12,
            "Charisma": 11
        },
        "saving_throws": {
            "Intelligence": "+6",
            "Wisdom": "+4"
        },
        "skills": {
            "Arcana": "+9",
            "History": "+6"
        },
        "damage_vulnerabilities": "Acid",
        "damage_immunities": "Cold, Lightning, Necrotic",
        "condition_immunities": "Blinded",
        "senses": "Darkvision 60 ft., passive Perception 11",
        "languages": "Any six languages",
        "spellcasting": {
            "spellcasting_ability": "Intelligence",
            "spell_save_dc": "14",
            "spell_attack_bonus": "+6",
            "spells": {
                "Cantrips (at will)": "fire bolt, light, mage hand, prestidigitation",
                "1st level (4 slots)": "detect magic, mage armor, magic missile, shield",
                "2nd level (3 slots)": "misty step, suggestion",
                "3rd level (3 slots)": "counterspell, fireball, fly",
                "4th level (3 slots)": "greater invisibility, ice storm",
                "5th level (2 slots)": "cone of cold, scrying",
                "6th level (1 slot)": "chain lightning",
                "7th level (1 slot)": "finger of death",
                "8th level (1 slot)": "globe of invulnerability",
                "9th level (1 slot)": "time stop"
            }
        },
        "actions": {
            "Dagger": "Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage."
        },
        "reactions": {
            "Shield": "The mage raises its hand and a shimmering field appears, granting it a +5 bonus to AC until the start of its next turn."
        }
    },
    "Mammoth": {
        "hit_points": "126 (11d12 + 55)",
        "armor_class": 13,
        "speed": "40 ft.",
        "size": "Huge",
        "type": "Beast",
        "alignment": "Unaligned",
        "challenge": "6",
        "abilities": {
            "Strength": 24,
            "Dexterity": 9,
            "Constitution": 21,
            "Intelligence": 3,
            "Wisdom": 11,
            "Charisma": 6
        },
        "saving_throws": {
            "Strength": "+10",
            "Constitution": "+9",
            "Wisdom": "+4"
        },
        "skills": {
            "Perception": "+4"
        },
        "damage_resistances": "Cold",
        "senses": "Passive Perception 14",
        "languages": "--",
        "actions": {
            "Trampling Charge": "If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 18 Strength saving throw or be knocked prone. If the target is prone, the mammoth can make one stomp attack against it as a bonus action."
        }
    },
    "Medusa": {
        "hit_points": "127 (17d8 + 51)",
        "armor_class": 15,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Monstrosity",
        "alignment": "Lawful Evil",
        "challenge": "6",
        "abilities": {
            "Strength": 10,
            "Dexterity": 15,
            "Constitution": 16,
            "Intelligence": 12,
            "Wisdom": 13,
            "Charisma": 15
        },
        "saving_throws": {
            "Dexterity": "+5",
            "Wisdom": "+4",
            "Charisma": "+5"
        },
        "skills": {
            "Deception": "+5",
            "Insight": "+4",
            "Perception": "+4",
            "Stealth": "+5"
        },
        "damage_immunities": "Petrification",
        "condition_immunities": "Petrified",
        "senses": "Darkvision 60 ft., passive Perception 14",
        "languages": "Common",
        "special_traits": {
            "Petrifying Gaze": "When a creature that can see the medusa's eyes starts its turn within 30 feet of the medusa, the medusa can force it to make a DC 14 Constitution saving throw if the medusa isn't incapacitated and can see the creature. If the saving throw fails by 5 or more, the creature is instantly petrified. Otherwise, a creature that fails the save begins to turn to stone and is restrained. The restrained creature must repeat the saving throw at the end of its next turn, becoming petrified on a failure or ending the effect on a success. The petrification lasts until the creature is freed by the greater restoration spell or other magic."
        },
        "actions": {
            "Multiattack": "The medusa makes either three melee attacks--one with its snake hair and two with its shortsword--or two ranged attacks with its longbow.",
            "Snake Hair": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage plus 14 (4d6) poison damage.",
            "Shortsword": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
            "Longbow": "Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit: 5 (1d8 + 2) piercing damage plus 14 (4d6) poison damage."
        },
        "reactions": {
            "Snakes for Hair": "When a creature ends its turn within 30 feet of the medusa and the two of them can see each other, the medusa can force the creature to make a DC 14 Wisdom saving throw if the medusa isn't incapacitated. On a failed save, the creature is magically charmed. While charmed in this way, the creature is incapacitated and has a speed of 0. The charmed creature repeats the saving throw at the end of its next turn. On a success, the effect ends."
        }
    },
    "Vrock": {
        "hit_points": "104 (11d10 + 44)",
        "armor_class": 15,
        "speed": "40 ft., fly 60 ft.",
        "size": "Large",
        "type": "Fiend (Demon)",
        "alignment": "Chaotic Evil",
        "challenge": "6",
        "abilities": {
            "Strength": 17,
            "Dexterity": 15,
            "Constitution": 18,
            "Intelligence": 8,
            "Wisdom": 13,
            "Charisma": 8
        },
        "saving_throws": {
            "Dexterity": "+5",
            "Constitution": "+7",
            "Wisdom": "+4"
        },
        "skills": {
            "Perception": "+4"
        },
        "damage_resistances": "Cold, Lightning, Bludgeoning, Piercing, and Slashing from Nonmagical Attacks",
        "damage_immunities": "Fire, Poison",
        "condition_immunities": "Poisoned",
        "senses": "Darkvision 120 ft., passive Perception 14",
        "languages": "Abyssal, telepathy 120 ft.",
        "special_traits": {
            "Magic Resistance": "The vrock has advantage on saving throws against spells and other magical effects.",
            "Variant: Demon Summoning": "The vrock has a 30 percent chance of summoning 1d4 vrocks, or 1d3 hezrous."
        },
        "actions": {
            "Multiattack": "The vrock makes two attacks: one with its beak and one with its talons.",
            "Beak": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage.",
            "Talons": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage."
        },
        "reactions": {
            "Spores": "When a creature the vrock can see starts its turn within 20 feet of the vrock, the vrock can release spores from its body. The creatures must succeed on a DC 14 Constitution saving throw or be poisoned for 1 minute. The poisoned creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        }
    },
    "Wyvern": {
        "hit_points": "110 (13d12 + 26)",
        "armor_class": 13,
        "speed": "20 ft., fly 80 ft.",
        "size": "Large",
        "type": "Dragon",
        "alignment": "Unaligned",
        "challenge": "6",
        "abilities": {
            "Strength": 19,
            "Dexterity": 10,
            "Constitution": 15,
            "Intelligence": 5,
            "Wisdom": 12,
            "Charisma": 6
        },
        "saving_throws": {
            "Dexterity": "+2",
            "Constitution": "+4",
            "Wisdom": "+3"
        },
        "skills": {
            "Perception": "+5"
        },
        "damage_immunities": "Poison",
        "condition_immunities": "Poisoned",
        "senses": "Darkvision 60 ft., passive Perception 15",
        "languages": "--",
        "actions": {
            "Multiattack": "The wyvern makes two attacks: one with its bite and one with its stinger. While flying, it can use its claws in place of one other attack.",
            "Bite": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) piercing damage.",
            "Claws": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.",
            "Stinger": "Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 11 (2d6 + 4) piercing damage. The target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Young Brass Dragon": {
        "hit_points": "110 (13d10 + 39)",
        "armor_class": 17,
        "speed": "40 ft., burrow 20 ft., fly 80 ft.",
        "size": "Large",
        "type": "Dragon",
        "alignment": "Chaotic Good",
        "challenge": "6",
        "abilities": {
            "Strength": 19,
            "Dexterity": 10,
            "Constitution": 17,
            "Intelligence": 12,
            "Wisdom": 11,
            "Charisma": 15
        },
        "saving_throws": {
            "Dexterity": "+3",
            "Constitution": "+6",
            "Wisdom": "+3",
            "Charisma": "+5"
        },
        "skills": {
            "Perception": "+6",
            "Stealth": "+3"
        },
        "damage_immunities": "Fire",
        "damage_resistances": "Bludgeoning, Piercing, and Slashing from Nonmagical Attacks",
        "condition_immunities": "Blinded",
        "senses": "Blindsight 30 ft., Darkvision 120 ft., passive Perception 16",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Keen Senses": "The dragon has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell."
        },
        "actions": {
            "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) piercing damage.",
            "Claw": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage."
        },
        "legendary_actions": {
            "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 14 Dexterity saving throw or take 11 (2d6 + 4) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        }
    },
    "Young White Dragon": {
        "hit_points": "133 (14d10 + 56)",
        "armor_class": 17,
        "speed": "40 ft., burrow 20 ft., fly 80 ft., swim 40 ft.",
        "size": "Large",
        "type": "Dragon",
        "alignment": "Chaotic Evil",
        "challenge": "6",
        "abilities": {
            "Strength": 18,
            "Dexterity": 10,
            "Constitution": 18,
            "Intelligence": 6,
            "Wisdom": 11,
            "Charisma": 12
        },
        "saving_throws": {
            "Dexterity": "+3",
            "Constitution": "+7",
            "Wisdom": "+3",
            "Charisma": "+4"
        },
        "skills": {
            "Perception": "+6",
            "Stealth": "+3"
        },
        "damage_immunities": "Cold",
        "condition_immunities": "Cold Immunity",
        "senses": "Blindsight 30 ft., Darkvision 120 ft., passive Perception 16",
        "languages": "Common, Draconic",
        "special_traits": {
            "Ice Walk": "The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra movement.",
            "Snow Vision": "The dragon ignores the obscured condition caused by snow."
        },
        "actions": {
            "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) piercing damage plus 4 (1d8) cold damage.",
            "Claw": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage plus 4 (1d8) cold damage.",
            "Cold Breath (Recharge 5-6)": "The dragon exhales a 30-foot cone of icy wind. Each creature in that area must make a DC 15 Constitution saving throw, taking 45 (10d8) cold damage on a failed save, or half as much damage on a successful one."
        }
    }
}
