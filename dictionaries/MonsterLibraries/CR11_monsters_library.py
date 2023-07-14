cr_11_monsters = {
    "Behir": {
        "hit_points": "168 (16d10 + 80)",
        "armor_class": 17,
        "speed": "50 ft., climb 40 ft.",
        "size": "Huge",
        "type": "Monstrosity",
        "alignment": "Neutral",
        "challenge": "11",
        "abilities": {
            "Strength": 23,
            "Dexterity": 16,
            "Constitution": 21,
            "Intelligence": 7,
            "Wisdom": 14,
            "Charisma": 12
        },
        "saving_throws": {
            "Dexterity": "+8",
            "Constitution": "+9",
            "Wisdom": "+6"
        },
        "skills": {
            "Perception": "+9"
        },
        "damage_vulnerabilities": "Lightning",
        "damage_immunities": "Cold",
        "condition_immunities": "Paralyzed",
        "senses": "Darkvision 90 ft., passive Perception 19",
        "languages": "Draconic",
        "special_traits": {
            "Lightning Absorption": "Whenever the behir is subjected to lightning damage, it takes no damage and instead regains a number of hit points equal to the lightning damage dealt.",
            "Actions": "Multiattack: The behir makes two attacks: one with its bite and one to constrict.",
            "Constrict": "Melee Weapon Attack: +10 to hit, reach 10 ft., one creature. Hit: 17 (2d10 + 6) bludgeoning damage plus 17 (2d10 + 6) slashing damage. The target is grappled (escape DC 16) if the behir isn't already constricting a creature, and the target is restrained until this grapple ends.",
            "Lightning Breath (Recharge 5-6)": "The behir exhales a line of lightning in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 16 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one."
        }
    },
    "Djinni": {
        "hit_points": "161 (14d10 + 84)",
        "armor_class": 17,
        "speed": "30 ft., fly 90 ft.",
        "size": "Large",
        "type": "Elemental",
        "alignment": "Chaotic Good",
        "challenge": "11",
        "abilities": {
            "Strength": 21,
            "Dexterity": 15,
            "Constitution": 22,
            "Intelligence": 15,
            "Wisdom": 16,
            "Charisma": 20
        },
        "saving_throws": {
            "Constitution": "+11",
            "Wisdom": "+8",
            "Charisma": "+10"
        },
        "skills": {
            "Perception": "+8",
            "Persuasion": "+10"
        },
        "damage_immunities": "Lightning, Thunder",
        "senses": "Darkvision 120 ft., passive Perception 18",
        "languages": "Auran, Common, Primordial",
        "special_traits": {
            "Innate Spellcasting": "The djinni's innate spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). It can innately cast the following spells, requiring no material components:",
            "Actions": "Multiattack: The djinni makes three scimitar attacks.",
            "Create Whirlwind (Recharge 4-6)": "A 5-foot-radius, 30-foot-tall cylinder of swirling air magically forms on a point the djinni can see within 120 feet of it. The whirlwind lasts as long as the djinni maintains concentration (as if concentrating on a spell). Any creature but the djinni that enters the whirlwind must succeed on a DC 18 Strength saving throw or be restrained by it. The djinni can move the whirlwind up to 60 feet as an action, and creatures restrained by the whirlwind move with it. The whirlwind ends if the djinni loses sight of it."
        },
        "spells": [
            "At will: detect evil and good, detect magic, thunderwave",
            "3/day each: create food and water, tongues, wind walk",
            "1/day each: conjure elemental (air elemental only), gaseous form, invisibility, major image, plane shift"
        ]
    },
    "Efreeti": {
        "hit_points": "200 (16d10 + 112)",
        "armor_class": 17,
        "speed": "40 ft., fly 60 ft.",
        "size": "Large",
        "type": "Elemental",
        "alignment": "Lawful Evil",
        "challenge": "11",
        "abilities": {
            "Strength": 22,
            "Dexterity": 12,
            "Constitution": 24,
            "Intelligence": 16,
            "Wisdom": 15,
            "Charisma": 16
        },
        "saving_throws": {
            "Wisdom": "+7",
            "Charisma": "+7"
        },
        "skills": {
            "Perception": "+7"
        },
        "damage_immunities": "Fire",
        "senses": "Darkvision 120 ft., passive Perception 17",
        "languages": "Ignan, Common",
        "special_traits": {
            "Elemental Demise": "If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind only equipment the djinni was wearing or carrying.",
            "Innate Spellcasting": "The efreeti's innate spellcasting ability is Charisma (spell save DC 15, +7 to hit with spell attacks). It can innately cast the following spells, requiring no material components:",
            "Actions": "Multiattack: The efreeti makes two scimitar attacks.",
            "Heat Metal": "The efreeti magically heats a metal object it can see within 60 feet of it. The object glows red-hot. Any creature in physical contact with the object takes 10 (3d6) fire damage when the effect is invoked. Until the spell ends, the creature takes 10 (3d6) fire damage at the start of each of its turns. A creature can drop the object as an action. If a creature is holding or wearing the object and takes the damage from it, the creature must succeed on a DC 17 Constitution saving throw or drop the object if it can. If it doesn't drop the object, it has disadvantage on attack rolls and ability checks until the start of its next turn."
        },
        "spells": [
            "At will: detect magic, enlarge/reduce, plane shift (self only)",
            "3/day: create bonfire, fireball",
            "1/day: conjure elemental (fire elemental only)"
        ]
    },
    "Gynosphinx": {
        "hit_points": "136 (16d10 + 48)",
        "armor_class": 17,
        "speed": "40 ft., fly 60 ft.",
        "size": "Large",
        "type": "Monstrosity",
        "alignment": "Lawful Neutral",
        "challenge": "11",
        "abilities": {
            "Strength": 18,
            "Dexterity": 15,
            "Constitution": 16,
            "Intelligence": 18,
            "Wisdom": 18,
            "Charisma": 18
        },
        "saving_throws": {
            "Intelligence": "+8",
            "Wisdom": "+8",
            "Charisma": "+8"
        },
        "skills": {
            "Arcana": "+8",
            "History": "+8",
            "Perception": "+8",
            "Religion": "+8"
        },
        "damage_immunities": "Psychic",
        "senses": "Truesight 120 ft., passive Perception 18",
        "languages": "Common, Sphinx",
        "special_traits": {
            "Inscrutable": "The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intentions or sincerity have disadvantage.",
            "Magic Weapons": "The sphinx's weapon attacks are magical.",
            "Spellcasting": "The sphinx is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 16, +8 to hit with spell attacks). It requires no material components to cast its spells. The sphinx has the following wizard spells prepared:",
            "Actions": "Multiattack: The sphinx makes two claw attacks.",
            "Claw": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.",
            "Roar (3/Day)": "The sphinx emits a magical roar. Each time it roars before finishing a long rest, the roar is louder and the effect is different, as detailed below. Each creature within 500 feet of the sphinx and able to hear the roar must make a saving throw."
        },
        "spells": [
            "Cantrips (at will): mage hand, minor illusion, prestidigitation",
            "1st level (4 slots): detect magic, identify, shield",
            "2nd level (3 slots): mirror image, suggestion",
            "3rd level (3 slots): dispel magic, haste",
            "4th level (3 slots): greater invisibility, stone shape",
            "5th level (1 slot): legend lore"
        ]
    },
    "Horned Devil": {
        "hit_points": "148 (17d10 + 51)",
        "armor_class": 18,
        "speed": "20 ft., fly 60 ft.",
        "size": "Large",
        "type": "Fiend",
        "alignment": "Lawful Evil",
        "challenge": "11",
        "abilities": {
            "Strength": 22,
            "Dexterity": 17,
            "Constitution": 17,
            "Intelligence": 12,
            "Wisdom": 16,
            "Charisma": 17
        },
        "saving_throws": {
            "Dexterity": "+7",
            "Constitution": "+7",
            "Wisdom": "+6",
            "Charisma": "+7"
        },
        "skills": {
            "Perception": "+6"
        },
        "damage_resistances": "Cold; Bludgeoning, Piercing, and Slashing from Nonmagical Attacks Not Made with Silvered Weapons",
        "damage_immunities": "Fire, Poison",
        "condition_immunities": "Poisoned",
        "senses": "Darkvision 120 ft., passive Perception 16",
        "languages": "Infernal, Telepathy 120 ft.",
        "special_traits": {
            "Devil's Sight": "Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance": "The devil has advantage on saving throws against spells and other magical effects.",
            "Actions": "Multiattack: The devil makes three melee attacks: one with its bite and two with its claws. Alternatively, it can use Hurl Flame twice.",
            "Bite": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 15 (2d10 + 4) piercing damage plus 10 (3d6) fire damage.",
            "Claw": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 10 (2d6 + 4) slashing damage.",
            "Hurl Flame": "Ranged Spell Attack: +7 to hit, range 150 ft., one target. Hit: 14 (4d6) fire damage. If the target is a flammable object that isn't being worn or carried, it also catches fire."
        },
        "spells": [
            "At will: detect magic",
            "1/day each: wall of fire, fireball"
        ]
    },
    "Remorhaz": {
        "hit_points": "195 (17d10 + 102)",
        "armor_class": 17,
        "speed": "30 ft., burrow 20 ft.",
        "size": "Huge",
        "type": "Monstrosity",
        "alignment": "Unaligned",
        "challenge": "11",
        "abilities": {
            "Strength": 24,
            "Dexterity": 13,
            "Constitution": 22,
            "Intelligence": 4,
            "Wisdom": 10,
            "Charisma": 5
        },
        "saving_throws": {
            "Constitution": "+11"
        },
        "damage_immunities": "Cold",
        "condition_immunities": "Chilled",
        "senses": "Darkvision 60 ft., tremorsense 60 ft., passive Perception 10",
        "languages": "None",
        "special_traits": {
            "Heated Body": "A creature that touches the remorhaz or hits it with a melee attack while within 5 feet of it takes 10 (3d6) fire damage.",
            "Actions": "Bite: Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 40 (6d10 + 7) piercing damage plus 10 (3d6) fire damage. If the target is a creature, it is grappled (escape DC 17). Until this grapple ends, the target is restrained, and the remorhaz can't bite another target.",
            "Swallow": "The remorhaz makes one bite attack against a Medium or smaller creature it is grappling. If the attack hits, the target takes the bite's damage, the target is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the remorhaz, and it takes 21 (6d6) acid damage at the start of each of the remorhaz's turns. A remorhaz can have only one creature swallowed at a time.",
            "Heat": "The remorhaz's body generates intense heat. The creature deals double damage to objects and structures."
        }
    },
    "Roc": {
        "hit_points": "248 (16d12 + 112)",
        "armor_class": 15,
        "speed": "20 ft., fly 120 ft.",
        "size": "Gargantuan",
        "type": "Monstrosity",
        "alignment": "Unaligned",
        "challenge": "11",
        "abilities": {
            "Strength": 28,
            "Dexterity": 10,
            "Constitution": 20,
            "Intelligence": 3,
            "Wisdom": 10,
            "Charisma": 9
        },
        "saving_throws": {
            "Dexterity": "+4",
            "Constitution": "+9",
            "Wisdom": "+4"
        },
        "skills": {
            "Perception": "+4"
        },
        "damage_immunities": "Bludgeoning, Piercing, and Slashing from Nonmagical Attacks",
        "senses": "Passive Perception 14",
        "languages": "None",
        "special_traits": {
            "Keen Sight": "The roc has advantage on Wisdom (Perception) checks that rely on sight.",
            "Actions": "Multiattack: The roc makes two attacks: one with its beak and one with its talons.",
            "Beak": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 27 (4d8 + 9) piercing damage.",
            "Talons": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 23 (4d6 + 9) slashing damage, and the target is grappled (escape DC 19). Until this grapple ends, the target is restrained, and the roc can't use its talons on another target."
        }
    }
}
