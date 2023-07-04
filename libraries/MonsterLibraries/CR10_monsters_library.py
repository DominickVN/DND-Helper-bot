cr_10_monsters = {
    "Aboleth": {
        "hit_points": "135 (18d10 + 36)",
        "armor_class": 17,
        "speed": "10 ft., swim 40 ft.",
        "size": "Large",
        "type": "Aberration",
        "alignment": "Lawful Evil",
        "challenge": "10",
        "abilities": {
            "Strength": 21,
            "Dexterity": 9,
            "Constitution": 15,
            "Intelligence": 18,
            "Wisdom": 15,
            "Charisma": 18
        },
        "saving_throws": {
            "Constitution": "+7",
            "Wisdom": "+6",
            "Charisma": "+8"
        },
        "skills": {
            "History": "+12",
            "Perception": "+10"
        },
        "damage_immunities": "Acid",
        "senses": "Darkvision 120 ft., passive Perception 20",
        "languages": "Deep Speech, telepathy 120 ft.",
        "special_traits": {
            "Amphibious": "The aboleth can breathe air and water.",
            "Mucous Cloud": "While underwater, the aboleth is surrounded by transformative mucus. A creature that touches the aboleth or hits it with a melee attack while within 5 feet of it must make a DC 14 Constitution saving throw. On a failure, the creature is diseased for 1d4 hours. The diseased creature can breathe only underwater.",
            "Probing Telepathy": "If a creature communicates telepathically with the aboleth, the aboleth learns the creature's greatest desires if the aboleth can see the creature."
        },
        "actions": {
            "Multiattack": "The aboleth makes three tentacle attacks.",
            "Tentacle": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Constitution saving throw or become diseased. The disease has no effect for 1 minute and can be removed by any magic that cures disease. After 1 minute, the diseased creature's skin becomes translucent and slimy, the creature can't regain hit points unless it is underwater, and the disease can be removed only by heal or another disease-curing spell of 6th level or higher. When the creature is outside a body of water, it takes 6 (1d12) acid damage every 10 minutes unless moisture is applied to the skin before 10 minutes have passed.",
            "Tail": "Melee Weapon Attack: +9 to hit, reach 10 ft. one target. Hit: 15 (3d6 + 5) bludgeoning damage."
        },
        "legendary_actions": {
            "Detect": "The aboleth makes a Wisdom (Perception) check.",
            "Tail Swipe": "The aboleth makes one tail attack.",
            "Psychic Drain (Costs 2 Actions)": "One creature charmed by the aboleth takes 10 (3d6) psychic damage, and the aboleth regains hit points equal to the damage the creature takes."
        }
    },
    "Deva": {
        "hit_points": "136 (16d10 + 48)",
        "armor_class": 17,
        "speed": "30 ft., fly 90 ft.",
        "size": "Medium",
        "type": "Celestial",
        "alignment": "Lawful Good",
        "challenge": "10",
        "abilities": {
            "Strength": 18,
            "Dexterity": 18,
            "Constitution": 16,
            "Intelligence": 17,
            "Wisdom": 20,
            "Charisma": 20
        },
        "saving_throws": {
            "Wisdom": "+9",
            "Charisma": "+9"
        },
        "skills": {
            "Insight": "+9",
            "Perception": "+9"
        },
        "damage_resistances": "Radiant; bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "Charmed, Exhaustion, Frightened",
        "senses": "Darkvision 120 ft., passive Perception 19",
        "languages": "All, telepathy 120 ft.",
        "special_traits": {
            "Angelic Weapons": "The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra 4d8 radiant damage (included in the attack).",
            "Innate Spellcasting": "The deva's spellcasting ability is Charisma (spell save DC 17). The deva can innately cast the following spells, requiring only verbal components:\n\nAt will: detect evil and good, invisibility (self only)\n3/day each: blade barrier, dispel evil and good, resurrection\n1/day each: commune, raise dead"
        },
        "actions": {
            "Multiattack": "The deva makes two melee attacks.",
            "Mace": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d6 + 6) bludgeoning damage plus 18 (4d8) radiant damage.",
            "Healing Touch (3/Day)": "The deva touches another creature. The target magically regains 20 (4d8 + 2) hit points and is freed from any curse, disease, poison, blindness, or deafness."
        },
        "reactions": {
            "Angelic Aura": "When the deva is reduced to 70 hit points or fewer, it sheds bright light in a 10-foot radius and dim light for an additional 10 feet. Until the end of its next turn, the deva has advantage on all saving throws, and other creatures have disadvantage on attack rolls against it."
        }
    },
    "Guardian Naga": {
        "hit_points": "127 (15d10 + 45)",
        "armor_class": 18,
        "speed": "40 ft.",
        "size": "Large",
        "type": "Monstrosity",
        "alignment": "Lawful Good",
        "challenge": "10",
        "abilities": {
            "Strength": 19,
            "Dexterity": 18,
            "Constitution": 16,
            "Intelligence": 16,
            "Wisdom": 19,
            "Charisma": 16
        },
        "saving_throws": {
            "Dexterity": "+8",
            "Constitution": "+7",
            "Wisdom": "+8",
            "Charisma": "+7"
        },
        "skills": {
            "Perception": "+8"
        },
        "damage_immunities": "Poison",
        "condition_immunities": "Charmed, Poisoned",
        "senses": "Darkvision 60 ft., passive Perception 18",
        "languages": "Common",
        "special_traits": {
            "Rejuvenation": "If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.",
            "Spellcasting": "The naga is a 9th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 16, +8 to hit with spell attacks). The naga has the following cleric spells prepared:\n\nCantrips (at will): light, sacred flame, thaumaturgy\n1st level (4 slots): command, cure wounds, shield of faith\n2nd level (3 slots): hold person, lesser restoration, silence\n3rd level (3 slots): dispel magic, remove curse, revivify\n4th level (3 slots): banishment, freedom of movement\n5th level (2 slots): flame strike, greater restoration\n6th level (1 slot): heal",
            "Reptilian Skin": "The naga has resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons."
        },
        "actions": {
            "Bite": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 8 (1d6 + 5) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 31 (7d8) poison damage on a failed save, or half as much damage on a successful one.",
            "Spit Poison": "The naga spits poison at a creature it can see within 30 feet of it. The target must make a DC 15 Dexterity saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one. If the target fails the save by 5 or more, it is also paralyzed for the same duration as the naga's Stunning Gaze ability."
        },
        "reactions": {
            "Stunning Gaze": "When a creature that can see the naga's eyes starts its turn within 30 feet of the naga, the naga can force it to make a DC 15 Constitution saving throw if the naga isn't incapacitated and can see the creature. If the saving throw fails by 5 or more, the creature is stunned until the end of its next turn."
        }
    },
    "Stone Golem": {
        "hit_points": "178 (17d10 + 85)",
        "armor_class": 17,
        "speed": "30 ft.",
        "size": "Large",
        "type": "Construct",
        "alignment": "Unaligned",
        "challenge": "10",
        "abilities": {
            "Strength": 22,
            "Dexterity": 9,
            "Constitution": 20,
            "Intelligence": 3,
            "Wisdom": 11,
            "Charisma": 1
        },
        "damage_immunities": "Poison, Psychic; bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine",
        "condition_immunities": "Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned",
        "senses": "Darkvision 120 ft., passive Perception 10",
        "languages": "Understands the languages of its creator but can't speak",
        "special_traits": {
            "Immutable Form": "The golem is immune to any spell or effect that would alter its form.",
            "Magic Resistance": "The golem has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons": "The golem's weapon attacks are magical.",
            "Siege Monster": "The golem deals double damage to objects and structures."
        },
        "actions": {
            "Multiattack": "The golem makes two slam attacks.",
            "Slam": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage."
        },
        "reactions": {
            "Slow (Recharge 5-6)": "The golem targets one or more creatures it can see within 10 feet of it. Each target must make a DC 17 Wisdom saving throw against this magic. On a failed save, a target can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the target can take either an action or a bonus action on its turn, not both. These effects last for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        }
    },
    "Young Gold Dragon": {
        "hit_points": "178 (17d10 + 85)",
        "armor_class": 18,
        "speed": "40 ft., fly 80 ft., swim 40 ft.",
        "size": "Large",
        "type": "Dragon",
        "alignment": "Lawful Good",
        "challenge": "10",
        "abilities": {
            "Strength": 23,
            "Dexterity": 14,
            "Constitution": 21,
            "Intelligence": 16,
            "Wisdom": 15,
            "Charisma": 20
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+9",
            "Wisdom": "+6",
            "Charisma": "+9"
        },
        "skills": {
            "Insight": "+6",
            "Perception": "+10",
            "Persuasion": "+9",
            "Stealth": "+6"
        },
        "damage_immunities": "Fire",
        "senses": "Blindsight 30 ft., Darkvision 120 ft., passive Perception 20",
        "languages": "Common, Draconic",
        "special_traits": {
            "Amphibious": "The dragon can breathe air and water.",
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": "Multiattack: The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."
        },
        "actions": {
            "Bite": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage.",
            "Claw": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.",
            "Tail": "Melee Weapon Attack: +10 to hit, reach 15 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage.",
            "Frightful Presence": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."
        },
        "legendary_actions": {
            "Detect": "The dragon makes a Wisdom (Perception) check.",
            "Tail Attack": "The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 18 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        }
    },
    "Young Red Dragon": {
        "hit_points": "178 (17d10 + 85)",
        "armor_class": 18,
        "speed": "40 ft., climb 40 ft., fly 80 ft.",
        "size": "Large",
        "type": "Dragon",
        "alignment": "Chaotic Evil",
        "challenge": "10",
        "abilities": {
            "Strength": 23,
            "Dexterity": 14,
            "Constitution": 21,
            "Intelligence": 16,
            "Wisdom": 13,
            "Charisma": 21
        },
        "saving_throws": {
            "Dexterity": "+6",
            "Constitution": "+9",
            "Wisdom": "+5",
            "Charisma": "+9"
        },
        "skills": {
            "Perception": "+7",
            "Stealth": "+6"
        },
        "damage_immunities": "Fire",
        "senses": "Blindsight 30 ft., Darkvision 120 ft., passive Perception 17",
        "languages": "Common, Draconic",
        "special_traits": {
            "Legendary Resistance (3/Day)": "If the dragon fails a saving throw, it can choose to succeed instead.",
            "Actions": "Multiattack: The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."
        },
        "actions": {
            "Bite": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 7 (2d6) fire damage.",
            "Claw": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.",
            "Tail": "Melee Weapon Attack: +10 to hit, reach 15 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage.",
            "Frightful Presence": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Fire Breath (Recharge 5-6)": "The dragon exhales fire in a 30-foot cone. Each creature in that area must make a DC 17 Dexterity saving throw, taking 56 (16d6) fire damage on a failed save, or half as much damage on a successful one."
        },
        "legendary_actions": {
            "Detect": "The dragon makes a Wisdom (Perception) check.",
            "Tail Attack": "The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions)": "The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 18 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        }
    }
}
