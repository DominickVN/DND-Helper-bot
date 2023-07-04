cr_p5_monsters = {
    "Ape": {
        "hit_points": "19 (3d8 + 6)",
        "armor_class": 12,
        "speed": "30 ft., climb 30 ft.",
        "size": "Medium",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Passive Perception 13",
        "ability_scores": {
            "strength": 16,
            "dexterity": 14,
            "constitution": 14,
            "intelligence": 6,
            "wisdom": 12,
            "charisma": 7
        },
        "challenge": "1/2",
        "actions": {
            "Fist": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage."
        },
        "special_abilities": {
            "Multiattack": "The ape makes two fist attacks."
        }
    },
    "Black Bear": {
        "hit_points": "19 (3d8 + 6)",
        "armor_class": 11,
        "speed": "40 ft., climb 30 ft.",
        "size": "Medium",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Passive Perception 13",
        "ability_scores": {
            "strength": 15,
            "dexterity": 10,
            "constitution": 14,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 7
        },
        "challenge": "1/2",
        "actions": {
            "Bite": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
        }
    },
    "Cockatrice": {
        "hit_points": "27 (6d8)",
        "armor_class": 11,
        "speed": "20 ft., fly 40 ft.",
        "size": "Small",
        "type": "Monstrosity",
        "alignment": "Unaligned",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "condition_immunities": "Petrified",
        "damage_immunities": "Petrification",
        "ability_scores": {
            "strength": 6,
            "dexterity": 12,
            "constitution": 11,
            "intelligence": 2,
            "wisdom": 13,
            "charisma": 5
        },
        "challenge": "1/2",
        "actions": {
            "Bite": "Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or be magically petrified. If the target is a Medium or smaller creature, it is also restrained. The petrification lasts until the target is freed by the greater restoration spell or similar magic."
        }
    },
    "Crocodile": {
        "hit_points": "19 (3d10 + 3)",
        "armor_class": 12,
        "speed": "20 ft., swim 30 ft.",
        "size": "Large",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Passive Perception 10",
        "ability_scores": {
            "strength": 15,
            "dexterity": 10,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 5
        },
        "challenge": "1/2",
        "actions": {
            "Bite": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage, and the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the crocodile can't bite another target."
        }
    },
    "Darkmantle": {
        "hit_points": "22 (5d8)",
        "armor_class": 11,
        "speed": "10 ft., fly 30 ft.",
        "size": "Small",
        "type": "Monstrosity",
        "alignment": "Unaligned",
        "senses": "Blindsight 60 ft., Passive Perception 10",
        "ability_scores": {
            "strength": 16,
            "dexterity": 12,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 10,
            "charisma": 5
        },
        "challenge": "1/2",
        "actions": {
            "Crush": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 6 (1d6 + 3) bludgeoning damage, and the darkmantle attaches to the target. If the target is Medium or smaller and the darkmantle has advantage on the attack roll, it attaches by engulfing the target's head, and the target is also blinded and unable to breathe while the darkmantle is attached in this way.",
            "Darkness Aura": "Magical darkness spreads from the darkmantle in a 15-foot radius, and the darkness moves with it. The darkness lasts as long as the darkmantle maintains concentration, up to 10 minutes (as if concentrating on a spell)."
        }
    },
    "Dust Mephit": {
        "hit_points": "17 (5d6)",
        "armor_class": 12,
        "speed": "30 ft., fly 30 ft.",
        "size": "Small",
        "type": "Elemental",
        "subtype": "Air",
        "alignment": "Neutral Evil",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "damage_immunities": "Poison",
        "condition_immunities": "Poisoned",
        "ability_scores": {
            "strength": 5,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 9,
            "wisdom": 11,
            "charisma": 10
        },
        "challenge": "1/2",
        "actions": {
            "Claws": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) slashing damage plus 2 (1d4) poison damage.",
            "Blinding Breath (Recharge 6)": "The mephit exhales a 15-foot cone of blinding dust. Each creature in that area must succeed on a DC 10 Dexterity saving throw or be blinded for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        },
        "special_abilities": {
            "Death Burst": "When the mephit dies, it explodes in a burst of dust. Each creature within 5 feet of it must then succeed on a DC 10 Dexterity saving throw or be blinded for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        }
    },
    "Giant Goat": {
        "hit_points": "19 (3d10 + 3)",
        "armor_class": 11,
        "speed": "40 ft.",
        "size": "Large",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Passive Perception 11",
        "ability_scores": {
            "strength": 17,
            "dexterity": 11,
            "constitution": 12,
            "intelligence": 3,
            "wisdom": 12,
            "charisma": 6
        },
        "challenge": "1/2",
        "actions": {
            "Ram": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) bludgeoning damage."
        }
    },
    "Giant Sea Horse": {
        "hit_points": "16 (3d8 + 3)",
        "armor_class": 13,
        "speed": "0 ft., swim 40 ft.",
        "size": "Large",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Passive Perception 12",
        "ability_scores": {
            "strength": 12,
            "dexterity": 15,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 13,
            "charisma": 5
        },
        "challenge": "1/2",
        "actions": {
            "Ram": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage."
        },
        "special_abilities": {
            "Water Breathing": "The sea horse can breathe only underwater."
        }
    },
    "Giant Wasp": {
        "hit_points": "13 (3d8)",
        "armor_class": 12,
        "speed": "10 ft., fly 50 ft.",
        "size": "Medium",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Passive Perception 10",
        "ability_scores": {
            "strength": 10,
            "dexterity": 14,
            "constitution": 10,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 3
        },
        "challenge": "1/2",
        "actions": {
            "Sting": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Gnoll": {
        "hit_points": "22 (4d8 + 4)",
        "armor_class": 15,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid",
        "subtype": "Gnoll",
        "alignment": "Chaotic Evil",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "ability_scores": {
            "strength": 14,
            "dexterity": 12,
            "constitution": 13,
            "intelligence": 6,
            "wisdom": 10,
            "charisma": 7
        },
        "challenge": "1/2",
        "actions": {
            "Bite": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage.",
            "Spear": "Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack."
        },
        "special_abilities": {
            "Rampage": "When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."
        }
    },
    "Gnome, Deep (Svirfneblin)": {
        "hit_points": "16 (3d6 + 6)",
        "armor_class": 15,
        "speed": "20 ft.",
        "size": "Small",
        "type": "Humanoid",
        "subtype": "Gnome",
        "alignment": "Lawful Good",
        "senses": "Darkvision 120 ft., Passive Perception 10",
        "languages": "Gnomish, Terran, Undercommon",
        "ability_scores": {
            "strength": 15,
            "dexterity": 14,
            "constitution": 14,
            "intelligence": 12,
            "wisdom": 10,
            "charisma": 9
        },
        "challenge": "1/2",
        "actions": {
            "War Pick": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage.",
            "Poisoned Dart": "Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 12 Constitution saving throw or be poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        },
        "special_abilities": {
            "Stone Camouflage": "The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
        }
    },
    "Gray Ooze": {
        "hit_points": "22 (4d8 + 4)",
        "armor_class": 8,
        "speed": "10 ft.",
        "size": "Medium",
        "type": "Ooze",
        "alignment": "Unaligned",
        "senses": "Blindsight 60 ft., Passive Perception 8",
        "condition_immunities": "Blinded, Charmed, Deafened, Exhaustion, Frightened, Prone",
        "ability_scores": {
            "strength": 12,
            "dexterity": 6,
            "constitution": 13,
            "intelligence": 1,
            "wisdom": 6,
            "charisma": 2
        },
        "challenge": "1/2",
        "actions": {
            "Pseudopod": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) acid damage."
        },
        "special_abilities": {
            "Amorphous": "The ooze can move through a space as narrow as 1 inch wide without squeezing."
        }
    },
    "Hobgoblin": {
        "hit_points": "11 (2d8 + 2)",
        "armor_class": 18,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid",
        "subtype": "Goblinoid",
        "alignment": "Lawful Evil",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "languages": "Common, Goblin",
        "ability_scores": {
            "strength": 13,
            "dexterity": 12,
            "constitution": 12,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 9
        },
        "challenge": "1/2",
        "actions": {
            "Longsword": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) slashing damage, or 6 (1d10 + 1) slashing damage if used with two hands.",
            "Longbow": "Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target. Hit: 4 (1d8) piercing damage."
        }
    },
    "Ice Mephit": {
        "hit_points": "21 (6d6)",
        "armor_class": 11,
        "speed": "30 ft., fly 30 ft.",
        "size": "Small",
        "type": "Elemental",
        "subtype": "Cold",
        "alignment": "Neutral Evil",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "damage_immunities": "Cold",
        "condition_immunities": "Frozen",
        "ability_scores": {
            "strength": 7,
            "dexterity": 13,
            "constitution": 10,
            "intelligence": 9,
            "wisdom": 11,
            "charisma": 12
        },
        "challenge": "1/2",
        "actions": {
            "Claws": "Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) slashing damage plus 2 (1d4) cold damage.",
            "Frost Breath (Recharge 6)": "The mephit exhales a 15-foot cone of cold air. Each creature in that area must make a DC 10 Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one."
        },
        "special_abilities": {
            "Death Burst": "When the mephit dies, it explodes in a burst of jagged ice. Each creature within 5 feet of it must make a DC 10 Dexterity saving throw, taking 4 (1d8) slashing damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Lizardfolk": {
        "hit_points": "22 (4d8 + 4)",
        "armor_class": 15,
        "speed": "30 ft., swim 30 ft.",
        "size": "Medium",
        "type": "Humanoid",
        "subtype": "Lizardfolk",
        "alignment": "Neutral",
        "senses": "Passive Perception 10",
        "languages": "Draconic",
        "ability_scores": {
            "strength": 15,
            "dexterity": 10,
            "constitution": 13,
            "intelligence": 7,
            "wisdom": 12,
            "charisma": 7
        },
        "challenge": "1/2",
        "actions": {
            "Multiattack": "The lizardfolk makes two melee attacks, each one with a different weapon.",
            "Bite": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
            "Heavy Club": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage.",
            "Javelin": "Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
        }
    },
    "Magma Mephit": {
        "hit_points": "22 (5d8)",
        "armor_class": 11,
        "speed": "30 ft., fly 30 ft.",
        "size": "Small",
        "type": "Elemental",
        "subtype": "Fire",
        "alignment": "Neutral Evil",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "damage_immunities": "Fire",
        "condition_immunities": "Fire",
        "ability_scores": {
            "strength": 8,
            "dexterity": 12,
            "constitution": 12,
            "intelligence": 7,
            "wisdom": 10,
            "charisma": 10
        },
        "challenge": "1/2",
        "actions": {
            "Claws": "Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) slashing damage plus 2 (1d4) fire damage.",
            "Fire Breath (Recharge 6)": "The mephit exhales a 15-foot cone of fire. Each creature in that area must make a DC 10 Dexterity saving throw, taking 5 (2d4) fire damage on a failed save, or half as much damage on a successful one."
        },
        "special_abilities": {
            "Death Burst": "When the mephit dies, it explodes in a burst of lava. Each creature within 5 feet of it must make a DC 10 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Magmin": {
        "hit_points": "9 (2d8)",
        "armor_class": 14,
        "speed": "30 ft.",
        "size": "Small",
        "type": "Elemental",
        "subtype": "Fire",
        "alignment": "Chaotic Neutral",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "damage_immunities": "Fire",
        "condition_immunities": "Charmed",
        "ability_scores": {
            "strength": 7,
            "dexterity": 15,
            "constitution": 10,
            "intelligence": 8,
            "wisdom": 10,
            "charisma": 10
        },
        "challenge": "1/2",
        "actions": {
            "Touch": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 fire damage plus 3 (1d6) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 3 (1d6) fire damage at the start of each of its turns."
        },
        "special_abilities": {
            "Ignition": "The magmin can cause flammable objects it touches to ignite. The same applies to a creature that touches the magmin, although the touch itself doesn't cause damage."
        }
    },
    "Orc": {
        "hit_points": "15 (2d8 + 6)",
        "armor_class": 13,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid",
        "subtype": "Orc",
        "alignment": "Chaotic Evil",
        "senses": "Darkvision 60 ft., Passive Perception 9",
        "languages": "Common, Orc",
        "ability_scores": {
            "strength": 16,
            "dexterity": 12,
            "constitution": 16,
            "intelligence": 7,
            "wisdom": 11,
            "charisma": 10
        },
        "challenge": "1/2",
        "actions": {
            "Greataxe": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d12 + 3) slashing damage."
        }
    },
    "Reef Shark": {
        "hit_points": "22 (4d8 + 4)",
        "armor_class": 12,
        "speed": "swim 40 ft.",
        "size": "Medium",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Blindsight 30 ft., Passive Perception 10",
        "ability_scores": {
            "strength": 14,
            "dexterity": 13,
            "constitution": 13,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 4
        },
        "challenge": "1/2",
        "actions": {
            "Bite": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
        },
        "special_abilities": {
            "Blood Frenzy": "The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points."
        }
    },
    "Rust Monster": {
        "hit_points": "27 (6d8)",
        "armor_class": 14,
        "speed": "40 ft.",
        "size": "Medium",
        "type": "Monstrosity",
        "subtype": "Beast",
        "alignment": "Unaligned",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "condition_immunities": "Charmed",
        "ability_scores": {
            "strength": 13,
            "dexterity": 12,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 13,
            "charisma": 6
        },
        "challenge": "1/2",
        "actions": {
            "Antennae": "The rust monster corrodes a nonmagical ferrous metal object it can see within 5 feet of it. If the object isn't being worn or carried, the touch destroys a 1-foot cube of it. If the object is being worn or carried by a creature, the creature can make a DC 11 Dexterity saving throw to avoid the rust monster's touch."
        },
        "special_abilities": {
            "Iron Scent": "The rust monster can pinpoint, by scent, the location of ferrous metal within 30 feet of it."
        }
    },
    "Sahuagin": {
        "hit_points": "22 (4d8 + 4)",
        "armor_class": 12,
        "speed": "30 ft., swim 40 ft.",
        "size": "Medium",
        "type": "Humanoid",
        "subtype": "Sahuagin",
        "alignment": "Lawful Evil",
        "senses": "Darkvision 120 ft., Passive Perception 10",
        "languages": "Sahuagin",
        "ability_scores": {
            "strength": 13,
            "dexterity": 11,
            "constitution": 12,
            "intelligence": 12,
            "wisdom": 13,
            "charisma": 9
        },
        "challenge": "1/2",
        "actions": {
            "Bite": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.",
            "Claws": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."
        },
        "special_abilities": {
            "Blood Frenzy": "The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points."
        }
    },
    "Satyr": {
        "hit_points": "31 (7d8)",
        "armor_class": 14,
        "speed": "40 ft.",
        "size": "Medium",
        "type": "Fey",
        "alignment": "Chaotic Good",
        "senses": "Passive Perception 12",
        "languages": "Common, Elvish, Sylvan",
        "ability_scores": {
            "strength": 12,
            "dexterity": 16,
            "constitution": 11,
            "intelligence": 12,
            "wisdom": 10,
            "charisma": 14
        },
        "challenge": "1/2",
        "actions": {
            "Ram": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) bludgeoning damage.",
            "Shortsword": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."
        },
        "special_abilities": {
            "Magic Resistance": "The satyr has advantage on saving throws against spells and other magical effects."
        }
    },
    "Scout": {
        "hit_points": "16 (3d8 + 3)",
        "armor_class": 13,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid",
        "subtype": "Any Race",
        "alignment": "Any Alignment",
        "senses": "Passive Perception 13",
        "languages": "Any One Language",
        "ability_scores": {
            "strength": 11,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 11,
            "wisdom": 13,
            "charisma": 11
        },
        "challenge": "1/2",
        "actions": {
            "Multiattack": "The scout makes two melee attacks or two ranged attacks.",
            "Shortsword": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.",
            "Shortbow": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
        },
        "special_abilities": {
            "Skirmisher": "The scout can move up to half its speed as a reaction when an enemy ends its turn within 5 feet of the scout. This movement doesn't provoke opportunity attacks."
        }
    },
    "Shadow": {
        "hit_points": "16 (3d8 + 3)",
        "armor_class": 12,
        "speed": "40 ft.",
        "size": "Medium",
        "type": "Undead",
        "alignment": "Chaotic Evil",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "damage_resistances": "Acid, Cold, Fire, Lightning, Thunder; Bludgeoning, Piercing, and Slashing from Nonmagical Attacks",
        "damage_immunities": "Necrotic, Poison",
        "condition_immunities": "Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained",
        "ability_scores": {
            "strength": 6,
            "dexterity": 14,
            "constitution": 13,
            "intelligence": 6,
            "wisdom": 10,
            "charisma": 8
        },
        "challenge": "1/2",
        "actions": {
            "Strength Drain": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 9 (2d6 + 2) necrotic damage, and the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest."
        },
        "special_abilities": {
            "Shadow Stealth": "While in dim light or darkness, the shadow can take the Hide action as a bonus action."
        }
    },
    "Swarm of Insects": {
        "hit_points": "22 (5d8)",
        "armor_class": 12,
        "speed": "20 ft., climb 20 ft.",
        "size": "Medium",
        "type": "Swarm of Tiny Beasts",
        "alignment": "Unaligned",
        "senses": "Blindsight 10 ft., Passive Perception 10",
        "condition_immunities": "Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned",
        "ability_scores": {
            "strength": 3,
            "dexterity": 13,
            "constitution": 10,
            "intelligence": 1,
            "wisdom": 7,
            "charisma": 1
        },
        "challenge": "1/2",
        "actions": {
            "Bites": "Melee Weapon Attack: +3 to hit, reach 0 ft., one target in the swarm's space. Hit: 10 (4d4) piercing damage, or 5 (2d4) piercing damage if the swarm has half of its hit points or fewer."
        },
        "special_abilities": {
            "Swarm": "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points."
        }
    },
    "Thug": {
        "hit_points": "32 (5d8 + 10)",
        "armor_class": 11,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid",
        "subtype": "Any Race",
        "alignment": "Any Non-Lawful Alignment",
        "senses": "Passive Perception 10",
        "languages": "Any One Language",
        "ability_scores": {
            "strength": 15,
            "dexterity": 11,
            "constitution": 14,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 11
        },
        "challenge": "1/2",
        "actions": {
            "Multiattack": "The thug makes two melee attacks.",
            "Mace": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage.",
            "Javelin": "Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
        }
    },
    "Warhorse": {
        "hit_points": "19 (3d10 + 3)",
        "armor_class": 11,
        "speed": "60 ft.",
        "size": "Large",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Passive Perception 11",
        "ability_scores": {
            "strength": 18,
            "dexterity": 12,
            "constitution": 13,
            "intelligence": 2,
            "wisdom": 12,
            "charisma": 7
        },
        "challenge": "1/2",
        "actions": {
            "Hooves": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."
        },
        "special_abilities": {
            "Trampling Charge": "If the warhorse moves at least 20 feet straight toward a creature and then hits it with a hooves attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked prone. If the target is prone, the warhorse can make another attack with its hooves against it as a bonus action."
        }
    },
    "Warhorse Skeleton": {
        "hit_points": "22 (3d8 + 9)",
        "armor_class": 13,
        "speed": "60 ft.",
        "size": "Large",
        "type": "Undead",
        "alignment": "Lawful Evil",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "damage_immunities": "Poison",
        "condition_immunities": "Exhaustion, Poisoned",
        "ability_scores": {
            "strength": 18,
            "dexterity": 12,
            "constitution": 15,
            "intelligence": 2,
            "wisdom": 8,
            "charisma": 5
        },
        "challenge": "1/2",
        "actions": {
            "Hooves": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."
        },
        "special_abilities": {
            "Charge": "If the warhorse skeleton moves at least 20 feet straight toward a target and then hits it with a hooves attack on the same turn, the target takes an extra 9 (2d8) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone."
        }
    }
}
