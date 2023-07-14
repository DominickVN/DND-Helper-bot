cr_9_monsters = {
    "Bone Devil": {
        "hit_points": "142 (15d10 + 60)",
        "armor_class": 19,
        "speed": "40 ft., fly 40 ft.",
        "size": "Large",
        "type": "Fiend",
        "alignment": "Lawful Evil",
        "challenge": "9",
        "abilities": {
            "Strength": 18,
            "Dexterity": 16,
            "Constitution": 18,
            "Intelligence": 13,
            "Wisdom": 14,
            "Charisma": 18
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+8",
            "Intelligence": "+4",
            "Wisdom": "+5",
            "Charisma": "+8"
        },
        "damage_resistances": "Cold; Bludgeoning, Piercing, and Slashing from Nonmagical Attacks that aren't Silvered",
        "damage_immunities": "Fire, Poison",
        "condition_immunities": "Poisoned",
        "senses": "Darkvision 120 ft., passive Perception 12",
        "languages": "Infernal, telepathy 120 ft.",
        "special_traits": {
            "Devil's Sight": "Magical Darkness doesn't impede the devil's Darkvision.",
            "Magic Resistance": "The devil has advantage on saving throws against spells and other magical effects.",
            "Sting": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 9 (1d8 + 5) piercing damage plus 14 (4d6) poison damage, and the target must succeed on a DC 14 Constitution saving throw or be poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        },
        "actions": {
            "Multiattack": "The devil makes three attacks: two with its claws and one with its sting.",
            "Claw": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d6 + 5) slashing damage.",
            "Bone Scimitar": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage plus 14 (4d6) necrotic damage.",
            "Hellfire Ray (Recharge 5-6)": "The devil targets one creature it can see within 120 feet of it. The target must make a DC 14 Dexterity saving throw, taking 21 (6d6) fire damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Clay Golem": {
        "hit_points": "133 (14d10 + 56)",
        "armor_class": 14,
        "speed": "20 ft.",
        "size": "Large",
        "type": "Construct",
        "alignment": "Unaligned",
        "challenge": "9",
        "abilities": {
            "Strength": 20,
            "Dexterity": 9,
            "Constitution": 18,
            "Intelligence": 3,
            "Wisdom": 8,
            "Charisma": 1
        },
        "damage_immunities": "Acid, Poison, Psychic; Bludgeoning, Piercing, and Slashing from Nonmagical Attacks that aren't Adamantine",
        "condition_immunities": "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned",
        "senses": "Darkvision 60 ft., passive Perception 9",
        "special_traits": {
            "Berserk": "Whenever the golem starts its turn with 60 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no creature is near enough to move to and attack, the golem attacks an object, with preference for an object smaller than itself. Once the golem goes berserk, it continues to do so until it is destroyed or regains all its hit points.",
            "Immutable Form": "The golem is immune to any spell or effect that would alter its form.",
            "Magic Resistance": "The golem has advantage on saving throws against spells and other magical effects."
        },
        "actions": {
            "Multiattack": "The golem makes two slam attacks.",
            "Slam": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage."
        }
    },
    "Cloud Giant": {
        "hit_points": "200 (16d10 + 112)",
        "armor_class": 14,
        "speed": "40 ft., fly 60 ft.",
        "size": "Huge",
        "type": "Giant",
        "alignment": "Neutral Good",
        "challenge": "9",
        "abilities": {
            "Strength": 27,
            "Dexterity": 10,
            "Constitution": 22,
            "Intelligence": 12,
            "Wisdom": 16,
            "Charisma": 16
        },
        "saving_throws": {
            "Constitution": "+10",
            "Wisdom": "+7"
        },
        "skills": {
            "Insight": "+7",
            "Perception": "+7"
        },
        "damage_resistances": "Lightning",
        "senses": "Passive Perception 17",
        "languages": "Common, Giant",
        "special_traits": {
            "Keen Smell": "The treant has advantage on Wisdom (Perception) checks that rely on smell.",
            "Innate Spellcasting": "The cloud giant's innate spellcasting ability is Wisdom (spell save DC 15). It can innately cast the following spells, requiring no material components:\n\nAt will: detect magic, fog cloud\n3/day each: feather fall, fly, misty step\n1/day each: control weather, gaseous form, telekinesis"
        },
        "actions": {
            "Multiattack": "The giant makes two greataxe attacks.",
            "Greataxe": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 30 (6d6 + 9) slashing damage."
        }
    },
    "Fire Giant": {
        "hit_points": "162 (13d12 + 78)",
        "armor_class": 18,
        "speed": "30 ft.",
        "size": "Huge",
        "type": "Giant",
        "alignment": "Lawful Evil",
        "challenge": "9",
        "abilities": {
            "Strength": 25,
            "Dexterity": 9,
            "Constitution": 23,
            "Intelligence": 10,
            "Wisdom": 14,
            "Charisma": 13
        },
        "saving_throws": {
            "Constitution": "+10",
            "Wisdom": "+5"
        },
        "damage_immunities": "Fire",
        "senses": "Passive Perception 12",
        "languages": "Giant",
        "special_traits": {
            "Heated Body": "A creature that touches the giant or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.",
            "Innate Spellcasting": "The fire giant's innate spellcasting ability is Charisma (spell save DC 11). It can innately cast the following spells, requiring no material components:\n\nAt will: detect magic\n3/day each: burning hands, fireball\n1/day each: wall of fire"
        },
        "actions": {
            "Multiattack": "The giant makes two greatsword attacks.",
            "Greatsword": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 28 (6d6 + 7) slashing damage."
        }
    },
    "Glabrezu": {
        "hit_points": "157 (15d10 + 75)",
        "armor_class": 17,
        "speed": "40 ft.",
        "size": "Large",
        "type": "Fiend (Demon)",
        "alignment": "Chaotic Evil",
        "challenge": "9",
        "abilities": {
            "Strength": 20,
            "Dexterity": 15,
            "Constitution": 21,
            "Intelligence": 19,
            "Wisdom": 17,
            "Charisma": 16
        },
        "saving_throws": {
            "Constitution": "+9",
            "Intelligence": "+8",
            "Wisdom": "+7",
            "Charisma": "+7"
        },
        "skills": {
            "Perception": "+7",
            "Stealth": "+6"
        },
        "damage_resistances": "Cold, Fire, Lightning; Bludgeoning, Piercing, and Slashing from Nonmagical Attacks",
        "damage_immunities": "Poison",
        "condition_immunities": "Poisoned",
        "senses": "Darkvision 120 ft., passive Perception 17",
        "languages": "Abyssal, telepathy 120 ft.",
        "special_traits": {
            "Innate Spellcasting": "The glabrezu's innate spellcasting ability is Intelligence (spell save DC 16). It can innately cast the following spells, requiring no material components:\n\nAt will: darkness, detect magic, dispel magic\n1/day each: confusion, fly, power word stun"
        },
        "actions": {
            "Multiattack": "The glabrezu makes four attacks: two with its pincers and two with its fists.",
            "Pincer": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage.",
            "Fist": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage."
        },
        "reactions": {
            "Reflective Carapace": "Any time the glabrezu is targeted by a magic missile spell, a line spell, or a spell that requires a ranged attack roll, roll a d6. On a 1 to 5, the glabrezu is unaffected. On a 6, the glabrezu is unaffected, and the effect is reflected back at the caster as though it originated from the glabrezu, turning the caster into the target."
        }
    },
    "Treant": {
        "hit_points": "138 (12d12 + 60)",
        "armor_class": 16,
        "speed": "30 ft.",
        "size": "Huge",
        "type": "Plant",
        "alignment": "Chaotic Good",
        "challenge": "9",
        "abilities": {
            "Strength": 23,
            "Dexterity": 8,
            "Constitution": 21,
            "Intelligence": 12,
            "Wisdom": 16,
            "Charisma": 12
        },
        "saving_throws": {
            "Constitution": "+10",
            "Wisdom": "+7"
        },
        "damage_immunities": "Poison",
        "condition_immunities": "Blinded, Deafened, Exhaustion",
        "senses": "Passive Perception 13",
        "languages": "Common, Druidic, Elvish, Sylvan",
        "special_traits": {
            "False Appearance": "While the treant remains motionless, it is indistinguishable from a normal tree.",
            "Siege Monster": "The treant deals double damage to objects and structures."
        },
        "actions": {
            "Multiattack": "The treant makes two slam attacks.",
            "Slam": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 16 (3d6 + 6) bludgeoning damage."
        },
        "legendary_actions": {
            "Slam (Costs 2 Actions)": "The treant makes one slam attack."
        }
    },
    "Young Blue Dragon": {
        "hit_points": "152 (16d10 + 64)",
        "armor_class": 18,
        "speed": "40 ft., burrow 30 ft., fly 80 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Lawful Evil",
        "challenge": "9",
        "abilities": {
            "Strength": 23,
            "Dexterity": 10,
            "Constitution": 21,
            "Intelligence": 14,
            "Wisdom": 13,
            "Charisma": 17
        },
        "saving_throws": {
            "Dexterity": "+4",
            "Constitution": "+9",
            "Wisdom": "+5",
            "Charisma": "+7"
        },
        "skills": {
            "Perception": "+9",
            "Stealth": "+4"
        },
        "damage_immunities": "Lightning",
        "senses": "Blindsight 30 ft., Darkvision 120 ft., passive Perception 19",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Lightning Breath (Recharge 5-6)": "The dragon exhales lightning in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 16 Dexterity saving throw, taking 55 (10d10) lightning damage on a failed save, or half as much damage on a successful one."
        },
        "actions": {
            "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 19 (2d10 + 8) piercing damage.",
            "Claw": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 15 (2d6 + 8) slashing damage.",
            "Frightful Presence": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 15 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        },
        "legendary_actions": {
            "Detect": "The dragon makes a Wisdom (Perception) check.",
            "Tail Attack": "The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 17 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        }
    },
    "Young Silver Dragon": {
        "hit_points": "168 (16d10 + 80)",
        "armor_class": 18,
        "speed": "40 ft., fly 80 ft., swim 40 ft.",
        "size": "Large",
        "type": "Dragon",
        "alignment": "Lawful Good",
        "challenge": "9",
        "abilities": {
            "Strength": 23,
            "Dexterity": 10,
            "Constitution": 21,
            "Intelligence": 14,
            "Wisdom": 13,
            "Charisma": 17
        },
        "saving_throws": {
            "Dexterity": "+4",
            "Constitution": "+9",
            "Wisdom": "+5",
            "Charisma": "+7"
        },
        "skills": {
            "Perception": "+9",
            "Stealth": "+4"
        },
        "damage_immunities": "Cold",
        "senses": "Blindsight 30 ft., Darkvision 120 ft., passive Perception 19",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Cold Breath (Recharge 5-6)": "The dragon exhales an icy blast in a 30-foot cone. Each creature in that area must make a DC 16 Constitution saving throw, taking 45 (10d8) cold damage on a failed save, or half as much damage on a successful one."
        },
        "actions": {
            "Multiattack": "The dragon can use its Frightful Presence. It then makes two attacks: one with its bite and one with its claws.",
            "Bite": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 15 (2d8 + 6) piercing damage.",
            "Claw": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 11 (2d4 + 6) slashing damage.",
            "Frightful Presence": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 15 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        },
        "legendary_actions": {
            "Detect": "The dragon makes a Wisdom (Perception) check.",
            "Tail Attack": "The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 17 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        }
    }
}
