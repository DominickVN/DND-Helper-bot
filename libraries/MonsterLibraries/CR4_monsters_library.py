cr_4_monsters = {
    "Black Pudding": {
        "hit_points": "85 (10d10 + 30)",
        "armor_class": 7,
        "speed": "20 ft., climb 20 ft.",
        "size": "Large",
        "type": "Ooze",
        "alignment": "Unaligned",
        "senses": "Blindsight 60 ft. (blind beyond this radius), Passive Perception 8",
        "challenge": "4",
        "abilities": {
            "Strength": 16,
            "Dexterity": 5,
            "Constitution": 20,
            "Intelligence": 1,
            "Wisdom": 6,
            "Charisma": 1
        },
        "damage_immunities": "Acid, Cold, Lightning, Slashing",
        "condition_immunities": "Blinded, Charmed, Deafened, Exhaustion, Frightened, Prone",
        "traits": {
            "Amorphous": "The pudding can move through a space as narrow as 1 inch wide without squeezing.",
            "Corrosive Form": "A creature that touches the pudding or hits it with a melee attack while within 5 feet of it takes 4 (1d8) acid damage. Any nonmagical weapon made of metal or wood that hits the pudding corrodes. After dealing damage, the weapon takes a permanent and cumulative -1 penalty to damage rolls. If its penalty drops to -5, the weapon is destroyed. Nonmagical ammunition made of metal or wood that hits the pudding is destroyed after dealing damage.",
            "Spider Climb": "The pudding can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
        },
        "actions": {
            "Pseudopod": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage plus 18 (4d8) acid damage. In addition, nonmagical armor worn by the target is partly dissolved and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10.",
            "Engulf": "The pudding moves up to its speed. While doing so, it can enter Large or smaller creatures' spaces. Whenever the pudding enters a creature's space, the creature must make a DC 14 Dexterity saving throw. On a successful save, the creature can choose to be pushed 5 feet back or to the side of the pudding. A creature that chooses not to be pushed suffers the consequences of a failed saving throw. On a failed save, the pudding enters the creature's space, and the creature takes 10 (3d6) acid damage and is engulfed. The engulfed creature can't breathe, is restrained, and takes 21 (6d6) acid damage at the start of each of the pudding's turns. When the pudding moves, the engulfed creature moves with it. An engulfed creature can try to escape by taking an action to make a DC 14 Strength check. On a success, the creature escapes and enters a space of its choice within 5 feet of the pudding."
        }
    },
    "Chuul": {
        "hit_points": "93 (11d10 + 33)",
        "armor_class": 16,
        "speed": "30 ft., swim 30 ft.",
        "size": "Large",
        "type": "Aberration",
        "alignment": "Chaotic Evil",
        "senses": "Darkvision 60 ft., Passive Perception 14",
        "languages": "Deep Speech",
        "challenge": "4",
        "abilities": {
            "Strength": 19,
            "Dexterity": 11,
            "Constitution": 16,
            "Intelligence": 5,
            "Wisdom": 11,
            "Charisma": 5
        },
        "saving_throws": {
            "Strength": "+6",
            "Dexterity": "+2",
            "Constitution": "+5",
            "Wisdom": "+2"
        },
        "skills": {
            "Perception": "+4",
            "Stealth": "+2"
        },
        "damage_immunities": "Psychic",
        "condition_immunities": "Charmed",
        "senses": "Darkvision 60 ft., Passive Perception 14",
        "languages": "Deep Speech",
        "traits": {
            "Amphibious": "The chuul can breathe air and water.",
            "Sense Magic": "The chuul senses magic within 120 feet of it at will. This trait otherwise works like the detect magic spell but isn't itself magical."
        },
        "actions": {
            "Multiattack": "The chuul makes two pincer attacks. If the chuul is grappling a creature, the chuul can also use its tentacles once.",
            "Pincer": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage. The target is grappled (escape DC 14) if it is a Large or smaller creature and the chuul doesn't have two other creatures grappled.",
            "Tentacles": "One creature grappled by the chuul must succeed on a DC 13 Constitution saving throw or be poisoned for 1 minute. Until this poison ends, the target is paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        }
    },
    "Couatl": {
        "hit_points": "97 (13d10 + 26)",
        "armor_class": 19,
        "speed": "30 ft., fly 90 ft.",
        "size": "Medium",
        "type": "Celestial",
        "alignment": "Lawful Good",
        "senses": "Darkvision 120 ft., Passive Perception 17",
        "languages": "All, telepathy 120 ft.",
        "challenge": "4",
        "abilities": {
            "Strength": 16,
            "Dexterity": 20,
            "Constitution": 14,
            "Intelligence": 18,
            "Wisdom": 20,
            "Charisma": 18
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+5",
            "Wisdom": "+7",
            "Charisma": "+7"
        },
        "skills": {
            "Arcana": "+8",
            "History": "+8",
            "Insight": "+7",
            "Perception": "+7",
            "Religion": "+8"
        },
        "condition_immunities": "Charmed, Exhaustion, Petrified",
        "senses": "Darkvision 120 ft., Passive Perception 17",
        "languages": "All, telepathy 120 ft.",
        "traits": {
            "Innate Spellcasting": "The couatl's innate spellcasting ability is Charisma (spell save DC 15). It can innately cast the following spells, requiring only verbal components:\n\nAt will: detect evil and good, detect magic, detect thoughts\n1/day each: bless, create food and water, cure wounds, lesser restoration, protection from poison, sanctuary, shield"
        },
        "actions": {
            "Bite": "Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 8 (1d6 + 5) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 24 hours. Until this poison ends, the target is unconscious. Another creature can use an action to shake the target awake.",
            "Constrict": "Melee Weapon Attack: +7 to hit, reach 10 ft., one Medium or smaller creature. Hit: 10 (2d6 + 3) bludgeoning damage, and the target is grappled (escape DC 15). Until this grapple ends, the target is restrained, and the couatl can't constrict another target."
        }
    },
    "Elephant": {
        "hit_points": "76 (8d12 + 24)",
        "armor_class": 12,
        "speed": "40 ft.",
        "size": "Huge",
        "type": "Beast",
        "alignment": "Unaligned",
        "senses": "Passive Perception 13",
        "challenge": "4",
        "abilities": {
            "Strength": 22,
            "Dexterity": 9,
            "Constitution": 17,
            "Intelligence": 3,
            "Wisdom": 11,
            "Charisma": 6
        },
        "skills": {
            "Perception": "+3"
        },
        "damage_immunities": "Poison",
        "condition_immunities": "Charmed, Frightened, Poisoned",
        "senses": "Passive Perception 13",
        "traits": {
            "Trampling Charge": "If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. If the target is prone, the elephant can make one stomp attack against it as a bonus action."
        },
        "actions": {
            "Gore": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) piercing damage."
        }
    },
    "Ettin": {
        "hit_points": "85 (10d10 + 30)",
        "armor_class": 12,
        "speed": "40 ft.",
        "size": "Large",
        "type": "Giant",
        "alignment": "Chaotic Evil",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "Giant, Orc",
        "challenge": "4",
        "abilities": {
            "Strength": 21,
            "Dexterity": 8,
            "Constitution": 17,
            "Intelligence": 6,
            "Wisdom": 10,
            "Charisma": 8
        },
        "saving_throws": {
            "Constitution": "+5",
            "Wisdom": "+2"
        },
        "skills": {
            "Perception": "+2"
        },
        "condition_immunities": "Blinded",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "Giant, Orc",
        "traits": {
            "Two Heads": "The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious.",
            "Wakeful": "When one of the ettin's heads is asleep, its other head is awake."
        },
        "actions": {
            "Multiattack": "The ettin makes two attacks: one with its battleaxe and one with its morningstar.",
            "Battleaxe": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage.",
            "Morningstar": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) piercing damage."
        }
    },
    "Ghost": {
        "hit_points": "45 (10d8)",
        "armor_class": 11,
        "speed": "0 ft., fly 40 ft. (hover)",
        "size": "Medium",
        "type": "Undead",
        "alignment": "Any",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "languages": "Any Languages It Knew In Life",
        "challenge": "4",
        "abilities": {
            "Strength": 7,
            "Dexterity": 13,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 12,
            "Charisma": 17
        },
        "skills": {
            "Stealth": "+3"
        },
        "damage_resistances": "Acid, Fire, Lightning, Thunder; Bludgeoning, Piercing, And Slashing From Nonmagical Attacks",
        "damage_immunities": "Cold, Necrotic, Poison",
        "condition_immunities": "Charmed, Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained",
        "senses": "Darkvision 60 ft., Passive Perception 10",
        "languages": "Any Languages It Knew In Life",
        "traits": {
            "Incorporeal Movement": "The ghost can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.",
            "Ethereal Sight": "The ghost can see 60 ft. into the Ethereal Plane when it is on the Material Plane, and vice versa."
        },
        "actions": {
            "Withering Touch": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 17 (4d6 + 3) necrotic damage.",
            "Etherealness": "The ghost enters the Ethereal Plane from the Material Plane, or vice versa. It is visible on the Material Plane while it is in the Border Ethereal, and vice versa, yet it can't affect or be affected by anything on the other plane."
        }
    },
    "Lamia": {
        "hit_points": "97 (13d8 + 39)",
        "armor_class": 13,
        "speed": "30 ft.",
        "size": "Large",
        "type": "Monstrosity",
        "alignment": "Chaotic Evil",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "Abyssal, Common",
        "challenge": "4",
        "abilities": {
            "Strength": 16,
            "Dexterity": 13,
            "Constitution": 16,
            "Intelligence": 14,
            "Wisdom": 15,
            "Charisma": 16
        },
        "skills": {
            "Deception": "+7",
            "Perception": "+4"
        },
        "saving_throws": {
            "Wisdom": "+4",
            "Charisma": "+6"
        },
        "damage_resistances": "Bludgeoning, Piercing, And Slashing From Nonmagical Attacks",
        "condition_immunities": "Charmed",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "Abyssal, Common",
        "traits": {
            "Innate Spellcasting": "The lamia's innate spellcasting ability is Charisma (spell save DC 14). The lamia can innately cast the following spells, requiring no material components:\n\nAt will: detect thoughts\n3/day: charm person, mirror image"
        },
        "actions": {
            "Multiattack": "The lamia makes two attacks: one with its claws and one with its dagger or two with its claws.",
            "Claws": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage.",
            "Dagger": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 4) piercing damage.",
            "Rejuvenation (1/Day)": "If it has a phylactery, a destroyed lich gains a new body in 1d10 days, regaining all its hit points and becoming active again. The new body appears within 5 feet of the phylactery."
        }
    },
    "Red Dragon Wyrmling": {
        "hit_points": "75 (10d10 + 20)",
        "armor_class": 17,
        "speed": "30 ft., climb 30 ft., fly 60 ft.",
        "size": "Medium",
        "type": "Dragon",
        "alignment": "Chaotic Evil",
        "senses": "Blindsight 30 ft., Darkvision 120 ft., Passive Perception 11",
        "languages": "Draconic",
        "challenge": "4",
        "abilities": {
            "Strength": 17,
            "Dexterity": 15,
            "Constitution": 15,
            "Intelligence": 10,
            "Wisdom": 11,
            "Charisma": 12
        },
        "saving_throws": {
            "Dexterity": "+4",
            "Constitution": "+4",
            "Wisdom": "+2",
            "Charisma": "+3"
        },
        "skills": {
            "Perception": "+2",
            "Stealth": "+4"
        },
        "damage_immunities": "Fire",
        "condition_immunities": "Frightened",
        "senses": "Blindsight 30 ft., Darkvision 120 ft., Passive Perception 11",
        "languages": "Draconic",
        "traits": {
            "Fire Breath (Recharge 5-6)": "The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC 13 Dexterity saving throw, taking 22 (4d10) fire damage on a failed save, or half as much damage on a successful one."
        },
        "actions": {
            "Bite": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage.",
            "Claw": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage."
        }
    },
    "Succubus/Incubus": {
        "hit_points": "66 (12d8 + 12)",
        "armor_class": 15,
        "speed": "30 ft., fly 60 ft.",
        "size": "Medium",
        "type": "Fiend (Shapechanger)",
        "alignment": "Neutral Evil",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "Abyssal, Common, Infernal, Telepathy 60 ft.",
        "challenge": "4",
        "abilities": {
            "Strength": 8,
            "Dexterity": 17,
            "Constitution": 12,
            "Intelligence": 15,
            "Wisdom": 12,
            "Charisma": 20
        },
        "saving_throws": {
            "Dexterity": "+5",
            "Charisma": "+9"
        },
        "skills": {
            "Deception": "+9",
            "Insight": "+4",
            "Perception": "+4",
            "Persuasion": "+9",
            "Stealth": "+7"
        },
        "damage_resistances": "Cold; Bludgeoning, Piercing, And Slashing From Nonmagical Attacks That Aren't Silvered",
        "damage_immunities": "Fire, Poison",
        "condition_immunities": "Charmed, Exhaustion, Poisoned",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "Abyssal, Common, Infernal, Telepathy 60 ft.",
        "traits": {
            "Telepathic Bond": "The fiend ignores the range restriction on its telepathy when communicating with a creature it has charmed. The two don't even need to be on the same plane of existence.",
            "Shapechanger": "The fiend can use its action to polymorph into a Small or Medium humanoid it has seen, or back into its true form. Without wings, the fiend loses its flying speed. Other than its size and speed, its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
        },
        "actions": {
            "Claw (Fiend Form Only)": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage plus 7 (2d6) psychic damage.",
            "Charm": "One humanoid the fiend can see within 30 feet of it must succeed on a DC 15 Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's verbal or telepathic commands. If the target suffers any harm or receives a suicidal command, it can repeat the saving throw, ending the effect on a success. If the target successfully saves against the effect, or if the effect on it ends, the target is immune to this fiend's Charm for the next 24 hours."
        }
    },
    "Wereboar": {
        "hit_points": "78 (12d8 + 24)",
        "armor_class": 10,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid (Human, Shapechanger)",
        "alignment": "Neutral Evil",
        "senses": "Passive Perception 11",
        "languages": "Common (can't speak in boar form)",
        "challenge": "4",
        "abilities": {
            "Strength": 17,
            "Dexterity": 10,
            "Constitution": 15,
            "Intelligence": 7,
            "Wisdom": 11,
            "Charisma": 8
        },
        "saving_throws": {
            "Constitution": "+4"
        },
        "skills": {
            "Perception": "+2"
        },
        "damage_immunities": "Bludgeoning, Piercing, And Slashing Damage From Nonmagical Attacks Not Made With Silvered Weapons In Animal Form",
        "condition_immunities": "Charmed, Frightened",
        "senses": "Passive Perception 11",
        "languages": "Common (can't speak in boar form)",
        "traits": {
            "Shapechanger": "The wereboar can use its action to polymorph into a boar-humanoid hybrid or into a boar, or back into its true form, which is humanoid. Its statistics, other than its AC, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
        },
        "actions": {
            "Multiattack (Humanoid or Hybrid Form Only)": "The wereboar makes two attacks, only one of which can be with its tusks.",
            "Maul (Humanoid or Hybrid Form Only)": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage.",
            "Tusks (Hybrid Form Only)": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
        }
    },
    "Weretiger": {
        "hit_points": "120 (16d8 + 48)",
        "armor_class": 12,
        "speed": "30 ft.",
        "size": "Medium",
        "type": "Humanoid (Human, Shapechanger)",
        "alignment": "Neutral",
        "senses": "Passive Perception 13",
        "languages": "Common (can't speak in tiger form)",
        "challenge": "4",
        "abilities": {
            "Strength": 17,
            "Dexterity": 15,
            "Constitution": 16,
            "Intelligence": 10,
            "Wisdom": 13,
            "Charisma": 11
        },
        "saving_throws": {
            "Constitution": "+5"
        },
        "skills": {
            "Perception": "+3",
            "Stealth": "+4"
        },
        "damage_immunities": "Bludgeoning, Piercing, And Slashing Damage From Nonmagical Attacks Not Made With Silvered Weapons In Animal Form",
        "condition_immunities": "Charmed, Frightened",
        "senses": "Passive Perception 13",
        "languages": "Common (can't speak in tiger form)",
        "traits": {
            "Shapechanger": "The weretiger can use its action to polymorph into a tiger-humanoid hybrid or into a tiger, or back into its true form, which is humanoid. Its statistics, other than its AC, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
        },
        "actions": {
            "Multiattack (Humanoid or Hybrid Form Only)": "The weretiger makes two attacks: one with its bite and one with its claws or two with its claws.",
            "Bite (Tiger or Hybrid Form Only)": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage.",
            "Claws (Tiger or Hybrid Form Only)": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) slashing damage."
        }
    }
}
