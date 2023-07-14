cr_8_monsters = {
    "Assassin": {
        "hit_points": "78 (12d8 + 24)",
        "armor_class": 15,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid",
        "alignment": "Neutral Evil",
        "challenge": "8",
        "abilities": {
            "Strength": 11,
            "Dexterity": 16,
            "Constitution": 14,
            "Intelligence": 13,
            "Wisdom": 11,
            "Charisma": 14
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Intelligence": "+4"
        },
        "skills": {
            "Acrobatics": "+7",
            "Deception": "+6",
            "Perception": "+4",
            "Stealth": "+11"
        },
        "damage_immunities": "Poison",
        "condition_immunities": "Charmed, Frightened, Poisoned",
        "senses": "Passive Perception 14",
        "languages": "Thieves' Cant plus any two languages",
        "special_traits": {
            "Assassinate": "During its first turn, the assassin has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the assassin scores against a surprised creature is a critical hit.",
            "Evasion": "If the assassin is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the assassin instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.",
            "Sneak Attack": "Once per turn, the assassin deals an extra 14 (4d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally of the assassin that isn't incapacitated and the assassin doesn't have disadvantage on the attack roll."
        },
        "actions": {
            "Multiattack": "The assassin makes two shortsword attacks.",
            "Shortsword": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Chain Devil": {
        "hit_points": "85 (10d8 + 40)",
        "armor_class": 16,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Fiend (Devil)",
        "alignment": "Lawful Evil",
        "challenge": "8",
        "abilities": {
            "Strength": 18,
            "Dexterity": 15,
            "Constitution": 18,
            "Intelligence": 11,
            "Wisdom": 12,
            "Charisma": 14
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+7",
            "Wisdom": "+4",
            "Charisma": "+5"
        },
        "damage_resistances": "Cold; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "damage_immunities": "Fire, Poison",
        "condition_immunities": "Poisoned",
        "senses": "Darkvision 120 ft., passive Perception 11",
        "languages": "Infernal, telepathy 120 ft.",
        "special_traits": {
            "Devil's Sight": "Magical darkness doesn't impede the devil's darkvision.",
            "Hellish Weapons": "The devil's weapon attacks are magical and deal an extra 9 (2d8) fire damage (included in the attacks).",
            "Innate Spellcasting": "The devil's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast the following spells, requiring no material components:\n\nAt will: darkness, dispel magic",
            "Magic Resistance": "The devil has advantage on saving throws against spells and other magical effects.",
            "Multiattack": "The devil makes two attacks with its chains.",
            "Unnerving Mask": "The devil has advantage on Charisma (Intimidation) checks made to interact with devils."
        },
        "actions": {
            "Multiattack": "The devil makes two attacks with its chains. It can use Hurl Chain in place of one chain attack.",
            "Chain": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) slashing damage. The target is grappled (escape DC 14) if the devil isn't already grappling a creature. Until this grapple ends, the target is restrained and takes 7 (2d6) piercing damage at the start of each of its turns.",
            "Hurl Chain": "Ranged Weapon Attack: +8 to hit, range 30/60 ft., one target not already grappled by the devil. Hit: The target is grappled (escape DC 14) if the devil isn't already grappling a creature. Until this grapple ends, the target is restrained and takes 7 (2d6) piercing damage at the start of each of its turns. The devil can't use the same chain on another target."
        }
    },
    "Cloaker": {
        "hit_points": "78 (12d8 + 24)",
        "armor_class": 14,
        "speed": "10 ft., fly 40 ft.",
        "size": "Large",
        "type": "Aberration",
        "alignment": "Lawful Neutral",
        "challenge": "8",
        "abilities": {
            "Strength": 17,
            "Dexterity": 15,
            "Constitution": 14,
            "Intelligence": 13,
            "Wisdom": 12,
            "Charisma": 13
        },
        "saving_throws": {
            "Dexterity": "+5",
            "Wisdom": "+4"
        },
        "skills": {
            "Perception": "+4",
            "Stealth": "+8"
        },
        "damage_resistances": "Psychic",
        "damage_immunities": "Force, Thunder",
        "condition_immunities": "Prone",
        "senses": "Blindsight 60 ft., passive Perception 14",
        "languages": "Deep Speech, Undercommon",
        "special_traits": {
            "Echolocation": "The cloaker can't use its blindsight while deafened.",
            "False Appearance": "While the cloaker remains motionless without its underside exposed, it is indistinguishable from a dark leather cloak.",
            "Light Sensitivity": "While in bright light, the cloaker has disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight.",
            "Moan": "Any creature that starts its turn within 60 feet of the cloaker and can hear the cloaker's moan must succeed on a DC 13 Wisdom saving throw or become frightened until the start of its next turn. If a creature's saving throw is successful, the creature is immune to the cloaker's moan for the next 24 hours."
        },
        "actions": {
            "Multiattack": "The cloaker makes two attacks: one with its bite and one with its tail.",
            "Bite": "Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 10 (2d6 + 3) piercing damage, and if the target is Large or smaller, the cloaker attaches to it. If the cloaker has advantage against the target, the cloaker attaches to the target's head, and the target is blinded and unable to breathe while the cloaker is attached. While attached, the cloaker can make this attack only against the target and has advantage on the attack roll. The cloaker can detach itself by spending 5 feet of its movement. A creature, including the target, can take its action to detach the cloaker by succeeding on a DC 16 Strength check.",
            "Tail": "Melee Weapon Attack: +6 to hit, reach 10 ft., one creature. Hit: 7 (1d8 + 3) slashing damage."
        }
    },
    "Frost Giant": {
        "hit_points": "138 (12d12 + 60)",
        "armor_class": 15,
        "speed": "40 ft.",
        "size": "Huge",
        "type": "Giant",
        "alignment": "Neutral Evil",
        "challenge": "8",
        "abilities": {
            "Strength": 23,
            "Dexterity": 9,
            "Constitution": 21,
            "Intelligence": 9,
            "Wisdom": 10,
            "Charisma": 12
        },
        "saving_throws": {
            "Constitution": "+8",
            "Wisdom": "+3"
        },
        "skills": {
            "Perception": "+3"
        },
        "damage_immunities": "Cold",
        "senses": "Passive Perception 13",
        "languages": "Giant",
        "special_traits": {
            "Frost Camouflage": "The giant has advantage on Dexterity (Stealth) checks made to hide in snowy terrain.",
            "Keen Smell": "The giant has advantage on Wisdom (Perception) checks that rely on smell."
        },
        "actions": {
            "Multiattack": "The giant makes two greataxe attacks.",
            "Greataxe": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 25 (3d12 + 6) slashing damage.",
            "Rock": "Ranged Weapon Attack: +9 to hit, range 60/240 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage."
        },
        "reactions": {
            "Frost Breath (Recharge 5-6)": "The giant exhales frigid air in a 15-foot cone. Each creature in that area must make a DC 16 Constitution saving throw, taking 45 (10d8) cold damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Hezrou": {
        "hit_points": "136 (13d10 + 65)",
        "armor_class": 16,
        "speed": "30 ft.",
        "size": "Large",
        "type": "Fiend (Demon)",
        "alignment": "Chaotic Evil",
        "challenge": "8",
        "abilities": {
            "Strength": 19,
            "Dexterity": 17,
            "Constitution": 20,
            "Intelligence": 5,
            "Wisdom": 12,
            "Charisma": 13
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+8",
            "Wisdom": "+4"
        },
        "damage_resistances": "Cold, Fire, Lightning",
        "damage_immunities": "Poison",
        "condition_immunities": "Poisoned",
        "senses": "Darkvision 120 ft., passive Perception 11",
        "languages": "Abyssal, telepathy 120 ft.",
        "special_traits": {
            "Magic Resistance": "The hezrou has advantage on saving throws against spells and other magical effects.",
            "Stench": "Any creature that starts its turn within 10 feet of the hezrou must succeed on a DC 14 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creature is immune to the hezrou's stench for 24 hours."
        },
        "actions": {
            "Multiattack": "The hezrou makes two attacks: one with its bite and one with its claws.",
            "Bite": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 21 (4d6 + 7) piercing damage.",
            "Claws": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) slashing damage.",
            "Spore Cloud (1/Day)": "A 20-foot-radius sphere of spores extends out from the hezrou, centered on it. The sphere spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it."
        },
        "reactions": {
            "Teleport": "The hezrou magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."
        }
    },
    "Hydra": {
        "hit_points": "172 (15d12 + 75)",
        "armor_class": 15,
        "speed": "30 ft., swim 30 ft.",
        "size": "Huge",
        "type": "Monstrosity",
        "alignment": "Unaligned",
        "challenge": "8",
        "abilities": {
            "Strength": 20,
            "Dexterity": 12,
            "Constitution": 20,
            "Intelligence": 2,
            "Wisdom": 10,
            "Charisma": 7
        },
        "saving_throws": {
            "Dexterity": "+5",
            "Constitution": "+9"
        },
        "skills": {
            "Perception": "+6"
        },
        "senses": "Darkvision 60 ft., passive Perception 16",
        "languages": "—",
        "special_traits": {
            "Hold Breath": "The hydra can hold its breath for 1 hour.",
            "Multiple Heads": "The hydra has five heads. While it has more than one head, the hydra has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious.",
            "Regeneration": "The hydra regains 10 hit points at the start of its turn. If the hydra takes radiant damage, this trait doesn't function at the start of the hydra's next turn. The hydra dies only if all its heads die.",
            "Wakeful": "While the hydra sleeps, at least one of its heads is awake."
        },
        "actions": {
            "Multiattack": "The hydra makes as many bite attacks as it has heads.",
            "Bite": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) piercing damage."
        }
    },
    "Spirit Naga": {
        "hit_points": "75 (10d8 + 30)",
        "armor_class": 15,
        "speed": "40 ft.",
        "size": "Large",
        "type": "Monstrosity",
        "alignment": "Chaotic Evil",
        "challenge": "8",
        "abilities": {
            "Strength": 18,
            "Dexterity": 17,
            "Constitution": 16,
            "Intelligence": 16,
            "Wisdom": 15,
            "Charisma": 16
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+6",
            "Wisdom": "+5",
            "Charisma": "+6"
        },
        "skills": {
            "Arcana": "+6",
            "Perception": "+5",
            "Stealth": "+6"
        },
        "damage_immunities": "Poison",
        "condition_immunities": "Charmed, Poisoned",
        "senses": "Darkvision 60 ft., passive Perception 15",
        "languages": "Abyssal, Common",
        "special_traits": {
            "Innate Spellcasting": "The naga's innate spellcasting ability is Charisma (spell save DC 14). It can innately cast the following spells, requiring no material components:\n\nAt will: mage hand (the hand is invisible)\n3/day each: darkness, poison spray\n1/day each: charm person, hold person, invisibility, suggestion"
        },
        "actions": {
            "Bite": "Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 8 (1d6 + 5) piercing damage, and the target must make a DC 13 Constitution saving throw, taking 31 (7d8) poison damage on a failed save, or half as much damage on a successful one.",
            "Constrict": "Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 11 (2d6 + 4) bludgeoning damage plus 16 (3d10) poison damage, and the target is grappled (escape DC 14). Until this grapple ends, the target is restrained, and the naga can't constrict another target."
        }
    },
    "Tyrannosaurus Rex": {
        "hit_points": "136 (13d12 + 52)",
        "armor_class": 13,
        "speed": "50 ft.",
        "size": "Huge",
        "type": "Beast",
        "alignment": "Unaligned",
        "challenge": "8",
        "abilities": {
            "Strength": 25,
            "Dexterity": 10,
            "Constitution": 19,
            "Intelligence": 2,
            "Wisdom": 12,
            "Charisma": 9
        },
        "saving_throws": {
            "Constitution": "+7",
            "Wisdom": "+4"
        },
        "skills": {
            "Perception": "+4"
        },
        "senses": "Passive Perception 14",
        "languages": "—",
        "special_traits": {
            "Keen Smell": "The tyrannosaurus has advantage on Wisdom (Perception) checks that rely on smell."
        },
        "actions": {
            "Multiattack": "The tyrannosaurus makes two attacks: one with its bite and one with its tail.",
            "Bite": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 33 (4d12 + 7) piercing damage. If the target is a Medium or smaller creature, it is grappled (escape DC 17). Until this grapple ends, the target is restrained, and the tyrannosaurus can't bite another target.",
            "Tail": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage."
        }
    },
    "Young Bronze Dragon": {
        "hit_points": "142 (15d10 + 60)",
        "armor_class": 18,
        "speed": "40 ft., fly 80 ft., swim 40 ft.",
        "size": "Large",
        "type": "Dragon",
        "alignment": "Lawful Good",
        "challenge": "8",
        "abilities": {
            "Strength": 21,
            "Dexterity": 10,
            "Constitution": 19,
            "Intelligence": 14,
            "Wisdom": 13,
            "Charisma": 17
        },
        "saving_throws": {
            "Dexterity": "+3",
            "Constitution": "+7",
            "Wisdom": "+4",
            "Charisma": "+6"
        },
        "skills": {
            "Insight": "+4",
            "Perception": "+6",
            "Stealth": "+3"
        },
        "damage_immunities": "Lightning",
        "senses": "Blindsight 30 ft., darkvision 120 ft., passive Perception 16",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": "Multiattack: The dragon makes three attacks: one with its bite and two with its claws.",
            "Bite": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) piercing damage.",
            "Claw": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.",
            "Breath Weapons (Recharge 5-6)": "The dragon uses one of the following breath weapons:",
            "Lightning Breath": "The dragon exhales lightning in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 15 Dexterity saving throw, taking 55 (10d10) lightning damage on a failed save, or half as much damage on a successful one.",
            "Repulsion Breath": "The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 15 Strength saving throw. On a failed save, the creature is pushed 40 feet away from the dragon."
        }
    },
    "Young Green Dragon": {
        "hit_points": "136 (16d10 + 48)",
        "armor_class": 18,
        "speed": "40 ft., fly 80 ft., swim 40 ft.",
        "size": "Large",
        "type": "Dragon",
        "alignment": "Lawful Evil",
        "challenge": "8",
        "abilities": {
            "Strength": 19,
            "Dexterity": 12,
            "Constitution": 17,
            "Intelligence": 16,
            "Wisdom": 13,
            "Charisma": 15
        },
        "saving_throws": {
            "Dexterity": "+4",
            "Constitution": "+5",
            "Wisdom": "+4",
            "Charisma": "+5"
        },
        "skills": {
            "Deception": "+5",
            "Perception": "+4",
            "Stealth": "+4"
        },
        "damage_immunities": "Poison",
        "condition_immunities": "Poisoned",
        "senses": "Blindsight 30 ft., darkvision 120 ft., passive Perception 14",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": "Multiattack: The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) piercing damage plus 7 (2d6) poison damage.",
            "Claw": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.",
            "Frightful Presence": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 13 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Poison Breath (Recharge 5-6)": "The dragon exhales poisonous gas in a 30-foot cone. Each creature in that area must make a DC 15 Constitution saving throw, taking 42 (12d6) poison damage on a failed save, or half as much damage on a successful one."
        }
    }
}
