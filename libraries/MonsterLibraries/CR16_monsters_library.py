cr_16_monsters = {
    "Adult Blue Dragon": {
        "hit_points": "225 (18d12 + 108)",
        "armor_class": 19,
        "speed": "40 ft., burrow 30 ft., fly 80 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Lawful Evil",
        "challenge": "16",
        "abilities": {
            "Strength": 27,
            "Dexterity": 10,
            "Constitution": 25,
            "Intelligence": 16,
            "Wisdom": 15,
            "Charisma": 19
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+12",
            "Wisdom": "+8",
            "Charisma": "+10"
        },
        "skills": {
            "Perception": "+14",
            "Stealth": "+6"
        },
        "damage_immunities": "lightning",
        "damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "frightened, paralyzed",
        "senses": "Blindsight 60 ft., darkvision 120 ft., passive Perception 24",
        "languages": "Common, Draconic",
        "special_traits": {
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": {
                "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
                "Bite": "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 18 (2d10 + 7) piercing damage plus 11 (2d10) lightning damage.",
                "Claw": "Melee Weapon Attack: +14 to hit, reach 5 ft., one target. Hit: 14 (2d6 + 7) slashing damage.",
                "Tail": "Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: 16 (2d8 + 7) bludgeoning damage.",
                "Frightful Presence": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 18 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
                "Lightning Breath (Recharge 5-6)": "The dragon exhales lightning in a 90-foot line that is 10 feet wide. Each creature in that line must make a DC 20 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one."
            }
        }
    },
    "Adult Silver Dragon": {
        "hit_points": "243 (18d12 + 126)",
        "armor_class": 19,
        "speed": "40 ft., fly 80 ft.",
        "size": "Huge",
        "type": "Dragon",
        "alignment": "Lawful Good",
        "challenge": "16",
        "abilities": {
            "Strength": 27,
            "Dexterity": 10,
            "Constitution": 25,
            "Intelligence": 18,
            "Wisdom": 15,
            "Charisma": 20
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+12",
            "Wisdom": "+8",
            "Charisma": "+11"
        },
        "skills": {
            "Perception": "+14",
            "Stealth": "+7"
        },
        "damage_immunities": "cold",
        "damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, paralyzed",
        "senses": "Blindsight 60 ft., darkvision 120 ft., passive Perception 24",
        "languages": "Common, Draconic",
        "special_traits": {
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": {
                "Multiattack": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
                "Bite": "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 19 (2d10 + 8) piercing damage.",
                "Claw": "Melee Weapon Attack: +14 to hit, reach 5 ft., one target. Hit: 15 (2d6 + 8) slashing damage.",
                "Tail": "Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: 17 (2d8 + 8) bludgeoning damage.",
                "Frightful Presence": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 18 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
                "Cold Breath (Recharge 5-6)": "The dragon exhales an icy blast in a 90-foot cone. Each creature in that area must make a DC 20 Constitution saving throw, taking 72 (16d8) cold damage on a failed save, or half as much damage on a successful one."
            }
        }
    },
    "Iron Golem": {
        "hit_points": "210 (20d10 + 100)",
        "armor_class": 20,
        "speed": "30 ft.",
        "size": "Large",
        "type": "Construct",
        "alignment": "Unaligned",
        "challenge": "16",
        "abilities": {
            "Strength": 24,
            "Dexterity": 9,
            "Constitution": 20,
            "Intelligence": 3,
            "Wisdom": 11,
            "Charisma": 1
        },
        "saving_throws": {
            "Constitution": "+9",
            "Wisdom": "+4"
        },
        "damage_immunities": "fire, poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine",
        "condition_immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
        "senses": "Darkvision 120 ft., Passive Perception 10",
        "languages": "Understands the languages of its creator but can't speak",
        "special_traits": {
            "Fire Absorption": "Whenever the golem is subjected to fire damage, it takes no damage and instead regains a number of hit points equal to the fire damage dealt.",
            "Immutable Form": "The golem is immune to any spell or effect that would alter its form.",
            "Magic Resistance": "The golem has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons": "The golem's weapon attacks are magical.",
            "Actions": {
                "Multiattack": "The golem makes two melee attacks.",
                "Slam": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage.",
                "Poison Breath (Recharge 5-6)": "The golem exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC 19 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one."
            }
        }
    },
    "Marilith": {
        "hit_points": "189 (18d10 + 90)",
        "armor_class": 18,
        "speed": "40 ft.",
        "size": "Large",
        "type": "Fiend (Demon)",
        "alignment": "Chaotic Evil",
        "challenge": "16",
        "abilities": {
            "Strength": 18,
            "Dexterity": 20,
            "Constitution": 20,
            "Intelligence": 18,
            "Wisdom": 16,
            "Charisma": 20
        },
        "saving_throws": {
            "Dexterity": "+10",
            "Constitution": "+10",
            "Intelligence": "+9",
            "Wisdom": "+8",
            "Charisma": "+10"
        },
        "skills": {
            "Deception": "+10",
            "Insight": "+8",
            "Perception": "+8",
            "Persuasion": "+10",
            "Stealth": "+10"
        },
        "damage_resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "damage_immunities": "poison",
        "condition_immunities": "poisoned",
        "senses": "Truesight 120 ft., Passive Perception 18",
        "languages": "Abyssal, telepathy 120 ft.",
        "special_traits": {
            "Magic Resistance": "The marilith has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons": "The marilith's weapon attacks are magical.",
            "Reactive": "The marilith can take one reaction on every turn in a combat.",
            "Actions": {
                "Multiattack": "The marilith can make seven attacks: six with its longswords and one with its tail.",
                "Longsword": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.",
                "Tail": "Melee Weapon Attack: +12 to hit, reach 10 ft., one creature. Hit: 15 (2d10 + 4) bludgeoning damage. If the target is a creature other than an undead or a construct, it must succeed on a DC 19 Constitution saving throw or be poisoned until the start of the marilith's next turn.",
                "Teleport": "The marilith magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see."
            }
        }
    },
    "Planetar": {
        "hit_points": "200 (16d10 + 112)",
        "armor_class": 19,
        "speed": "40 ft., fly 120 ft.",
        "size": "Large",
        "type": "Celestial",
        "alignment": "Lawful Good",
        "challenge": "16",
        "abilities": {
            "Strength": 24,
            "Dexterity": 20,
            "Constitution": 24,
            "Intelligence": 19,
            "Wisdom": 22,
            "Charisma": 25
        },
        "saving_throws": {
            "Wisdom": "+11",
            "Charisma": "+13"
        },
        "skills": {
            "Insight": "+11",
            "Perception": "+11"
        },
        "damage_resistances": "radiant; bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, exhaustion, frightened",
        "senses": "Truesight 120 ft., Passive Perception 21",
        "languages": "all, telepathy 120 ft.",
        "special_traits": {
            "Angelic Weapons": "The planetar's weapon attacks are magical. When the planetar hits with any weapon, the weapon deals an extra 5d8 radiant damage (included in the attack).",
            "Divine Awareness": "The planetar knows if it hears a lie.",
            "Innate Spellcasting": "The planetar's spellcasting ability is Charisma (spell save DC 21). The planetar can innately cast the following spells, requiring no material components:",
            "Magic Resistance": "The planetar has advantage on saving throws against spells and other magical effects.",
            "Actions": {
                "Multiattack": "The planetar makes two melee attacks.",
                "Greatsword": "Melee Weapon Attack: +14 to hit, reach 5 ft., one target. Hit: 21 (4d6 + 7) slashing damage plus 22 (5d8) radiant damage.",
                "Healing Touch (3/Day)": "The planetar touches another creature. The target magically regains 30 (6d8 + 3) hit points and is freed from any curse, disease, poison, blindness, or deafness."
            },
            "Divine Spells": {
                "At will": "detect evil and good, invisibility (self only)",
                "1/day each": "blade barrier, dispel evil and good, flame strike, raise dead"
            }
        }
    }
}
