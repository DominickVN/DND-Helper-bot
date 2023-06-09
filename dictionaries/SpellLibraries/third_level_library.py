third_level_spells = {
    'animate dead': {
        'description': 'This spell creates an undead servant. Choose a pile of bones or a corpse of a medium or small humanoid within range. Your spell imbues the target with a foul mimicry of life, raising it as an undead creature. The target becomes a Skeleton if you chose bones or a Zombie if you chose a corpse (the DM has the creature\'s game statistics).\n\nOn each of your turns, you can use a bonus action to mentally command any creature you made with this spell if the creature is within 60 feet of you (if you control multiple creatures, you can command any or all of them at the same time, issuing the same command to each one). You decide what action the creature will take and where it will move during its next turn, or you can issue a general command, such as to guard a particular chamber or corridor. If you issue no commands, the creature only defends itself against hostile creatures. Once given an order, the creature continues to follow it until its task is complete.\n\nThe creature is under your control for 24 hours, after which it stops obeying any command you\'ve given it. To maintain control of the creature for another 24 hours, you must cast this spell on the creature again before the current 24-hour period ends. This use of the spell reasserts your control over up to four creatures you have animated with this spell, rather than animating a new one.\n\nWhen you cast this spell using a spell slot of 4th level or higher, you animate or reassert control over two additional undead creatures for each slot level above 3rd. Each of the creatures must come from a different corpse or pile of bones.',
        'level': 3,
        'casting_time': '1 minute',
        'range': '10 feet',
        'components': 'V, S, M (a drop of blood, a piece of flesh, and a pinch of bone dust)',
        'duration': 'Instantaneous',
        'school': 'Necromancy',

    },
    'aura of vitality': {
        'description': 'Healing energy radiates from you in an aura with a 30-foot radius. Until the spell ends, the aura moves with you, centered on you. You can use a bonus action to cause one creature in the aura (including you) to regain 2d6 hit points.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'beacon of hope': {
        'description': 'This spell bestows hope and vitality. Choose any number of creatures within range. For the duration, each target has advantage on Wisdom Saving Throws and Death Saving Throws, and regains the maximum number of hit points possible from any healing.',
        'level': 3,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Abjuration',
        'concentration': True,

    },
    'bestow curse': {
        'description': 'You touch a creature, and that creature must succeed on a Wisdom Saving Throw or become cursed for the duration of the spell. When you cast this spell, choose the nature of the curse from the following options:\n\n•Choose one Ability Score. While cursed, the target has disadvantage on Ability Checks and Saving Throws made with that Ability Score.\n•While cursed, the target has disadvantage on Attack Rolls against you.\n•While cursed, the target must make a Wisdom Saving Throw at the start of each of its turns. If it fails, it wastes its action that turn doing nothing.\n•While the target is cursed, your attacks and spells deal an extra 1d8 necrotic damage to the target.\n\nA remove curse spell ends this effect. At the DM\'s option, you may choose an alternative curse effect, but it should be no more powerful than those described above. The DM has final say on such a curse\'s effect.\n\nIf you cast this spell using a spell slot of 4th level or higher, the duration is concentration, up to 10 minutes. If you use a spell slot of 5th level or higher, the duration is 8 hours. If you use a spell slot of 7th level or higher, the duration is 24 hours. If you use a 9th level spell slot, the spell lasts until it is dispelled. Using a spell slot of 5th level or higher grants a duration that doesn\'t require concentration.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Necromancy',
        'concentration': True,

    },
    'blinding smite': {
        'description': 'The next time you hit a creature with a Melee Weapon Attack during this spell\'s duration, your weapon flares with bright light, and the attack deals an extra 3d8 radiant damage to the target. Additionally, the target must succeed on a Constitution Saving Throw or be blinded until the spell ends.\n\nA creature blinded by this spell makes another Constitution Saving Throw at the end of each of its turns. On a successful save, it is no longer blinded.',
        'level': 3,
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'blink': {
        'description': 'Roll a d20 at the end of each of your turns for the duration of the spell. On a roll of 11 or higher, you vanish from your current plane of existence and appear in the Ethereal Plane (the spell fails and the casting is wasted if you were already on that plane). At the start of your next turn, and when the spell ends if you are on the Ethereal Plane, you return to an unoccupied space of your choice that you can see within 10 feet of the space you vanished from. If no unoccupied space is available within that range, you appear in the nearest unoccupied space (chosen at random if more than one space is equally near). You can dismiss this spell as an action.\n\nWhile on the Ethereal Plane, you can see and hear the plane you originated from, which is cast in shades of gray, and you can\'t see anything there more than 60 feet away. You can only affect and be affected by other creatures on the Ethereal Plane. Creatures that aren\'t there can\'t perceive you or interact with you, unless they have the ability to do so.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '1 minute',
        'school': 'Transmutation',


    },
    'call lightning': {
        'description': 'A storm cloud appears in the shape of a cylinder that is 10 feet tall with a 60-foot radius, centered on a point you can see within range directly above you. The spell fails if you can\'t see a point in the air where the storm cloud could appear (for example, if you are in a room that can\'t accommodate the cloud).\n\nWhen you cast the spell, choose a point you can see under the cloud. A bolt of lightning flashes down from the cloud to that point. Each creature within 5 feet of that point must make a Dexterity Saving Throw. A creature takes 3d10 lightning damage on a failed save, or half as much damage on a successful one. On each of your turns until the spell ends, you can use your action to call down lightning in this way again, targeting the same point or a different one.\n\nIf you are outdoors in stormy conditions when you cast this spell, the spell gives you control over the existing storm instead of creating a new one. Under such conditions, the spell\'s damage increases by 1d10.\n\nWhen you cast this spell using a spell slot of 4th or higher level, the damage increases by 1d10 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Conjuration',
        'concentration': True,

    },
    'catnap': {
        'description': 'You make a calming gesture, and up to three willing creatures of your choice that you can see within range fall unconscious for the spell\'s duration. The spell ends on a target early if it takes damage or someone uses an action to shake or slap it awake. If a target remains unconscious for the full duration, that target gains the benefit of a short rest, and it can\'t be affected by this spell again until it finishes a long rest.\n\nWhen you cast this spell using a spell slot of 4th level or higher, you can target one additional willing creature for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'S, M (a pinch of sand)',
        'duration': '10 minutes',
        'school': 'Enchantment',


    },
    'clairvoyance': {
        'description': 'You create an invisible sensor within range in a location familiar to you (a place you have visited or seen before) or in an obvious location that is unfamiliar to you (such as behind a door, around a corner, or in a grove of trees). The sensor remains in place for the duration, and it can\'t be attacked or otherwise interacted with.\n\nWhen you cast the spell, you choose seeing or hearing. You can use the chosen sense through the sensor as if you were in its space. As your action, you can switch between seeing and hearing.\n\nA creature that can see the sensor (such as a creature benefiting from see invisibility or truesight) sees a luminous, intangible orb about the size of your fist.',
        'level': 3,
        'casting_time': '10 minutes',
        'range': '1 mile',
        'components': 'V, S, M (a focus worth at least 100 gp, either a jeweled horn for hearing or a glass eye for seeing)',
        'duration': 'Up to 10 minutes',
        'school': 'Divination',
        'concentration': True,

    },
    'conjure animals': {
        'description': 'You summon fey spirits that take the form of beasts and appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:\n\n•One beast of challenge rating 2 or lower\n•Two beasts of challenge rating 1 or lower\n•Four beasts of challenge rating 1/2 or lower\n•Eight beasts of challenge rating 1/4 or lower\n\nEach beast is also considered fey, and it disappears when it drops to 0 hit points or when the spell ends.\n\nThe summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don\'t issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.\n\nThe DM has the creatures\' statistics.\n\nWhen you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 5th-level slot, three times as many with a 7th-level slot, and four times as many with a 9th-level slot.',
        'level': 3,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Conjuration',
        'concentration': True,

    },
    'conjure barrage': {
        'description': 'You throw a nonmagical weapon or fire a piece of nonmagical ammunition into the air to create a cone of identical weapons that shoot forward and then disappear. Each creature in a 60-foot cone must succeed on a Dexterity Saving Throw. A creature takes 3d8 damage on a failed save, or half as much damage on a successful one. The damage type is the same as that of the weapon or ammunition used as a component.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M (one piece of nonmagical ammunition or a thrown weapon)',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'counterspell': {
        'description': 'You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, make an Ability Check using your spellcasting ability. The DC equals 10 + the spell\'s level. On a success, the creature\'s spell fails and has no effect.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the interrupted spell has no effect if its level is less than or equal to the level of the spell slot you used.',
        'level': 3,
        'casting_time': '1 reaction',
        'range': '60 feet',
        'components': 'S',
        'duration': 'Instantaneous',
        'school': 'Abjuration',


    },
    'create food and water': {
        'description': 'You create 45 pounds of food and 30 gallons of water on the ground or in containers within range, enough to sustain up to fifteen humanoids or five steeds for 24 hours. The food is bland but nourishing, and spoils if uneaten after 24 hours. The water is clean and doesn\'t go bad.',
        'level': 3,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'crusader\'s mantle': {
        'description': 'Holy power radiates from you in an aura with a 30-foot radius, awakening boldness in friendly creatures. Until the spell ends, the aura moves with you, centered on you. While in the aura, each nonhostile creature in the aura (including you) deals an extra 1d4 radiant damage when it hits with a Weapon Attack.',
        'level': 3,
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'daylight': {
        'description': 'A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet.\n\nIf you chose a point on an object you are holding or one that isn\'t being worn or carried, the light shines from the object and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light.\n\nIf any of this spell\'s area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled.',
        'level': 3,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Evocation',


    },
    'dispel magic': {
        'description': 'Choose one creature, object, or magical effect within range. Any spell of 3rd level or lower on the target ends. For each spell of 4th level or higher on the target, make an Ability Check using your spellcasting ability. The DC equals 10 + the spell\'s level. On a successful check, the spell ends.\n\nWhen you cast this spell using a spell slot of 4th level or higher, you automatically end the effects of a spell on the target if the spell\'s level is equal to or less than the level of the spell slot you used.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Abjuration',


    },
    'elemental weapon': {
        'description': 'A nonmagical weapon you touch becomes a magic weapon. Choose one of the following damage types: acid, cold, fire, lightning, or thunder. For the duration, the weapon has a +1 bonus to Attack Rolls and deals an extra 1d4 damage of the chosen type when it hits.\n\nWhen you cast this spell using a spell slot of 5th or 6th level, the bonus to Attack Rolls increases to +2 and the extra damage increases to 2d4. When you use a spell slot of 7th level or higher, the bonus increases to +3 and the extra damage increases to 3d4.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Transmutation',
        'concentration': True,

    },
    'enemies abound': {
        'description': 'You reach into the mind of one creature you can see and force it to make an Intelligence Saving Throw. A creature automatically succeeds if it is immune to being frightened. On a failed save, the target loses the ability to distinguish friend from foe, regarding all creatures it can see as enemies until the spell ends. Each time the target takes damage, it can repeat the Saving Throw, ending the effect on itself on a success.\n\nWhenever the affected creature chooses another creature as a target, it must choose the target at random from among the creatures it can see within range of the attack, spell, or other ability it\'s using. If an enemy provokes an opportunity attack from the affected creature, the creature must make that attack if it is able to.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'erupting earth': {
        'description': 'Choose a point you can see on the ground within range. A fountain of churned earth and stone erupts in a 20-foot cube centered on that point. Each creature in that area must make a Dexterity Saving Throw. A creature takes 3d12 bludgeoning damage on a failed save, or half as much damage on a successful one. Additionally, the ground in that area becomes difficult terrain until cleared. Each 5-foot-square portion of the area requires at least 1 minute to clear by hand.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d12 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M (a piece of obsidian)',
        'duration': 'Instantaneous',
        'school': 'Transmutation',


    },
    'fast friends': {
        'description': 'When you need to make sure something gets done, you can\'t rely on vague promises, sworn oaths, or binding contracts of employment. When you cast this spell, choose one humanoid within range that can see and hear you, and that can understand you. The creature must succeed on a Wisdom Saving Throw or become charmed by you for the duration. While the creature is charmed in this way, it undertakes to perform any services or activities you ask of it in a friendly manner, to the best of its ability.\n\nYou can set the creature new tasks when a previous task is completed, or if you decide to end its current task. If the service or activity might cause harm to the creature, or if it conflicts with the creature\'s normal activities and desires, the creature can make another Wisdom Saving Throw to try to end the effect. This save is made with advantage if you or your companions are fighting the creature. If the activity would result in certain death for the creature, the spell ends.\n\nWhen the spell ends, the creature knows it was charmed by you.\n\nWhen you cast this spell using a spell slot of 4th level or higher, you can target one additional creature for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'fear': {
        'description': 'You project a phantasmal image of a creature\'s worst fears. Each creature in a 30-foot cone must succeed on a Wisdom Saving Throw or drop whatever it is holding and become frightened for the duration.\n\nWhile frightened by this spell, a creature must take the dash action and move away from you by the safest available route on each of its turns, unless there is nowhere to move. If the creature ends its turn in a location where it doesn\'t have line of sight to you, the creature can make a Wisdom Saving Throw. On a successful save, the spell ends for that creature.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self (30-foot cone)',
        'components': 'V, S, M (a white feather or the heart of a hen)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Illusion',
        'concentration': True,

    },
    'feign death': {
        'description': 'You touch a willing creature and put it into a cataleptic state that is indistinguishable from death.\n\nFor the spell\'s duration, or until you use an action to touch the target and dismiss the spell, the target appears dead to all outward inspection and to spells used to determine the target\'s status. The target is blinded and incapacitated, and its speed drops to 0. The target has resistance to all damage except psychic damage. If the target is diseased or poisoned when you cast the spell, or becomes diseased or poisoned while under the spell\'s effect, the disease and poison have no effect until the spell ends.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a pinch of graveyard dirt)',
        'duration': '1 hour',
        'school': 'Necromancy',


    },
    'fireball': {
        'description': 'A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame. Each creature in a 20-foot-radius sphere centered on that point must make a Dexterity Saving Throw. A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one.\n\nThe fire spreads around corners. It ignites flammable objects in the area that aren\'t being worn or carried.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S, M (a tiny ball of bat guano and sulfur)',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'flame arrows': {
        'description': 'You touch a quiver containing arrows or bolts. When a target is hit by a Ranged Weapon Attack using a piece of ammunition drawn from the quiver, the target takes an extra 1d6 fire damage. The spell\'s magic ends on a piece of ammunition when it hits or misses, and the spell ends when twelve pieces of ammunition have been drawn from the quiver.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the number of pieces of ammunition you can affect with this spell increases by two for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a drop of oil and a small piece of flint)',
        'duration': '1 hour',
        'school': 'Transmutation',


    },
    'fly': {
        'description': 'You touch a willing creature. The target gains a flying speed of 60 feet for the duration. When the spell ends, the target falls if it is still aloft, unless it can stop the fall.\n\nWhen you cast this spell using a spell slot of 4th level or higher, you can target one additional creature for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a wing feather from any bird)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'gaseous form': {
        'description': 'You transform a willing creature you touch, along with everything it\'s wearing and carrying, into a misty cloud for the duration. The spell ends if the creature drops to 0 hit points. An incorporeal creature isn\'t affected.\n\nWhile in this form, the target\'s only method of movement is a flying speed of 10 feet. The target can enter and occupy the space of another creature. The target has resistance to nonmagical damage, and it has advantage on Strength, Dexterity, and Constitution Saving Throws. The target can pass through small holes, narrow openings, and even mere cracks, though it treats liquids as though they were solid surfaces. The target can\'t fall and remains hovering in the air even when stunned or otherwise incapacitated.\n\nWhile in the form of a misty cloud, the target can\'t talk or manipulate objects, and any objects it was carrying or holding can\'t be dropped, used, or otherwise interacted with. The target can\'t attack or cast spells.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a bit of gauze and a wisp of smoke)',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Transmutation',
        'concentration': True,

    },
    'glyph of warding': {
        'description': 'When you cast this spell, you inscribe a glyph that later unleashes a magical effect. You inscribe it either on a surface (such as a table or a section of floor or wall) or within an object that can be closed (such as a book, a scroll, or a treasure chest) to conceal the glyph. The glyph can cover an area no larger than 10 feet in diameter. If the surface or object is moved more than 10 feet from where you cast this spell, the glyph is broken, and the spell ends without being triggered.\n\nThe glyph is nearly invisible and requires a successful Intelligence (Investigation) check against your Spell Save DC to be found.\n\nYou decide what triggers the glyph when you cast the spell. For glyphs inscribed on a surface, the most typical triggers include touching or standing on the glyph, removing another object covering the glyph, approaching within a certain distance of the glyph, or manipulating the object on which the glyph is inscribed. For glyphs inscribed within an object, the most common triggers include opening that object, approaching within a certain distance of the object, or seeing or reading the glyph. Once a glyph is triggered, this spell ends.\n\nYou can further refine the trigger so the spell activates only under certain circumstances or according to physical characteristics (such as height or weight), creature kind (for example, the ward could be set to affect aberrations or drow), or alignment. You can also set conditions for creatures that don\'t trigger the glyph, such as those who say a certain password.\n\nWhen you inscribe the glyph, choose explosive runes or a spell glyph.\n\nExplosive Runes\n•When triggered, the glyph erupts with magical energy in a 20-foot-radius sphere centered on the glyph. The sphere spreads around corners. Each creature in the area must make a Dexterity Saving Throw. A creature takes 5d8 acid, cold, fire, lightning, or thunder damage on a failed Saving Throw (your choice when you create the glyph), or half as much damage on a successful one.\n\nSpell Glyph\n•You can store a prepared spell of 3rd level or lower in the glyph by casting it as part of creating the glyph. The spell must target a single creature or an area. The spell being stored has no immediate effect when cast in this way. When the glyph is triggered, the stored spell is cast. If the spell has a target, it targets the creature that triggered the glyph. If the spell affects an area, the area is centered on that creature. If the spell summons hostile creatures or creates harmful objects or traps, they appear as close as possible to the intruder and attack it. If the spell requires concentration, it lasts until the end of its full duration.\n\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage of an explosive runes glyph increases by 1d8 for each slot level above 3rd. If you create a spell glyph, you can store any spell of up to the same level as the slot you use for the glyph of warding.',
        'level': 3,
        'casting_time': '1 hour',
        'range': 'Touch',
        'components': 'V, S, M (incense and powdered diamond worth at least 200 gp, which the spell consumes)',
        'duration': 'Until dispelled or triggered',
        'school': 'Abjuration',


    },
    'haste': {
        'description': 'Choose a willing creature that you can see within range. Until the spell ends, the target\'s speed is doubled, it gains a +2 bonus to AC, it has advantage on Dexterity Saving Throws, and it gains an additional action on each of its turns. That action can be used only to take the attack (one Weapon Attack only), dash, disengage, hide, or use an object action.\n\nWhen the spell ends, the target can\'t move or take actions until after its next turn, as a wave of lethargy sweeps over it.',
        'level': 3,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a shaving of licorice root)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'hunger of hadar': {
        'description': 'You open a gateway to the dark between the stars, a region infested with unknown horrors. A 20-foot-radius sphere of blackness and bitter cold appears, centered on a point within range and lasting for the duration. This void is filled with a cacophony of soft whispers and slurping noises that can be heard up to 30 feet away. No light, magical or otherwise, can illuminate the area, and creatures fully within the area are blinded.\n\nThe void creates a warp in the fabric of space, and the area is difficult terrain. Any creature that starts its turn in the area takes 2d6 cold damage. Any creature that ends its turn in the area must succeed on a Dexterity Saving Throw or take 2d6 acid damage as milky, otherworldly tentacles rub against it.',
        'level': 3,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S, M (a pickled octopus tentacle)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

    },
    'hypnotic pattern': {
        'description': 'You create a twisting pattern of colors that weaves through the air inside a 30-foot cube within range. The pattern appears for a moment and vanishes. Each creature in the area who sees the pattern must make a Wisdom Saving Throw. On a failed save, the creature becomes charmed for the duration. While charmed by this spell, the creature is incapacitated and has a speed of 0.\n\nThe spell ends for an affected creature if it takes any damage or if someone else uses an action to shake the creature out of its stupor.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'S, M (a glowing stick of incense or a crystal vial filled with phosphorescent material)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Illusion',
        'concentration': True,

    },
    'leomunds tiny hut': {
        'description': 'A 10-foot-radius immobile dome of force springs into existence around and above you and remains stationary for the duration. The spell ends if you leave its area.\n\nNine creatures of medium size or smaller can fit inside the dome with you. The spell fails if its area includes a larger creature or more than nine creatures. Creatures and objects within the dome when you cast this spell can move through it freely. All other creatures and objects are barred from passing through it. Spells and other magical effects can\'t extend through the dome or be cast through it. The atmosphere inside the space is comfortable and dry, regardless of the weather outside.\n\nUntil the spell ends, you can command the interior to become dimly lit or dark. The dome is opaque from the outside, of any color you choose, but it is transparent from the inside.',
        'level': 3,
        'casting_time': '1 minute',
        'range': 'Self',
        'components': 'V, S, M (a small crystal bead)',
        'duration': '8 hours',
        'school': 'Evocation',


    },
    'life transference': {
        'description': 'You sacrifice some of your health to mend another creature\'s injuries. You take 4d8 necrotic damage, and one creature of your choice that you can see within range regains a number of hit points equal to twice the necrotic damage you take.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d8 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Necromancy',


    },
    'lightning arrow': {
        'description': 'The next time you make a Ranged Weapon Attack during the spell\'s duration, the weapon\'s ammunition, or the weapon itself if it\'s a thrown weapon, transforms into a bolt of lightning. Make the Attack Roll as normal. The target takes 4d8 lightning damage on a hit, or half as much damage on a miss, instead of the weapon\'s normal damage.\n\nWhether you hit or miss, each creature within 10 feet of the target must make a Dexterity Saving Throw. Each of these creatures takes 2d8 lightning damage on a failed save, or half as much damage on a successful one.\n\nThe piece of ammunition or weapon then returns to its normal form.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage for both effects of the spell increases by 1d8 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 bonus action',
        'range': 'Self',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'lightning bolt': {
        'description': 'A stroke of lightning forming a line 100 feet long and 5 feet wide blasts out from you in a direction you choose. Each creature in the line must make a Dexterity Saving Throw. A creature takes 8d6 lightning damage on a failed save, or half as much damage on a successful one.\n\nThe lightning ignites flammable objects in the area that aren\'t being worn or carried.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self (100-foot line)',
        'components': 'V, S, M (a bit of fur and a rod of amber, crystal, or glass)',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'magic circle': {
        'description': 'You create a 10-foot-radius, 20-foot-tall cylinder of magical energy centered on a point on the ground that you can see within range. Glowing runes appear wherever the cylinder intersects with the floor or other surface.\n\nChoose one or more of the following types of creatures: celestials, elementals, fey, fiends, or undead. The circle affects a creature of the chosen type in the following ways:\n\n•The creature can\'t willingly enter the cylinder by nonmagical means. If the creature tries to use teleportation or interplanar travel to do so, it must first succeed on a Charisma Saving Throw.\n•The creature has disadvantage on Attack Rolls against targets within the cylinder.\n•Targets within the cylinder can\'t be charmed, frightened, or possessed by the creature.\n\nWhen you cast this spell, you can elect to cause its magic to operate in the reverse direction, preventing a creature of the specified type from leaving the cylinder and protecting targets outside it.',
        'level': 3,
        'casting_time': '1 minute',
        'range': '10 feet',
        'components': 'V, S, M (holy water or powdered silver and iron worth at least 100 gp, which the spell consumes)',
        'duration': '1 hour',
        'school': 'Abjuration',


    },
    'major image': {
        'description': 'You create the image of an object, a creature, or some other visible phenomenon that is no larger than a 20-foot cube. The image appears at a spot that you can see within range and lasts for the duration. It seems completely real, including sounds, smells, and temperature appropriate to the thing depicted. You can\'t create sufficient heat or cold to cause damage, a sound loud enough to deal thunder damage or deafen a creature, or a smell that might sicken a creature (like a troglodyte\'s stench).\n\nAs long as you are within range of the illusion, you can use your action to cause the image to move to any other spot within range. As the image changes location, you can alter its appearance so that its movements appear natural for the image. For example, if you create an image of a creature and move it, you can alter the image so that it appears to be walking. Similarly, you can cause the illusion to make different sounds at different times, even making it carry on a conversation, for example.\n\nPhysical interaction with the image reveals it to be an illusion, because things can pass through it. A creature that uses its action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your Spell Save DC. If a creature discerns the illusion for what it is, the creature can see through the image, and its other sensory qualities become faint to the creature.\n\nWhen you cast this spell using a spell slot of 6th level or higher, the spell lasts until dispelled, without requiring your concentration.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M (a bit of fleece)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Illusion',
        'concentration': True,

    },
    'mass healing word': {
        'description': 'As you call out words of restoration, up to six creatures of your choice that you can see within range regain hit points equal to 1d4 + your Spellcasting Ability Modifier. This spell has no effect on undead or constructs.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the healing increases by 1d4 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 bonus action',
        'range': '60 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'meld into stone': {
        'description': 'You step into a stone object or surface large enough to fully contain your body, melding yourself and all the equipment you carry with the stone for the duration. Using your movement, you step into the stone at a point you can touch. Nothing of your presence remains visible or otherwise detectable by nonmagical senses.\n\nWhile merged with the stone, you can\'t see what occurs outside it, and any Wisdom (Perception) checks you make to hear sounds outside it are made with disadvantage. You remain aware of the passage of time and can cast spells on yourself while merged in the stone. You can use your movement to leave the stone where you entered it, which ends the spell. You otherwise can\'t move.\n\nMinor physical damage to the stone doesn\'t harm you, but its partial destruction or a change in its shape (to the extent that you no longer fit within it) expels you and deals 6d6 bludgeoning damage to you. The stone\'s complete destruction (or transmutation into a different substance) expels you and deals 50 bludgeoning damage to you. If expelled, you fall prone in an unoccupied space closest to where you first entered.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': '8 hours',
        'school': 'Transmutation',


    },
    'melfs minute meteors': {
        'description': 'You create six tiny meteors in your space. They float in the air and orbit you for the spell\'s duration. When you cast the spell—and as a bonus action on each of your turns thereafter—you can expend one or two of the meteors, sending them streaking toward a point or points you choose within 120 feet of you. Once a meteor reaches its destination or impacts against a solid surface, the meteor explodes. Each creature within 5 feet of the point where the meteor explodes must make a Dexterity Saving Throw. A creature takes 2d6 fire damage on a failed save, or half as much damage on a successful one.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the number of meteors created increases by two for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

    },
    'nondetection': {
        'description': 'For the duration, you hide a target that you touch from divination magic. The target can be a willing creature or a place or an object no larger than 10 feet in any dimension. The target can\'t be targeted by any divination magic or perceived through magical scrying sensors.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (a pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes)',
        'duration': '8 hours',
        'school': 'Abjuration',


    },
    'phantom steed': {
        'description': 'A large quasi-real, horselike creature appears on the ground in an unoccupied space of your choice within range. You decide the creature\'s appearance, but it is equipped with a saddle, bit, and bridle. Any of the equipment created by the spell vanishes in a puff of smoke if it is carried more than 10 feet away from the steed.\n\nFor the duration, you or a creature you choose can ride the steed. The creature uses the statistics for a Riding Horse, except it has a speed of 100 feet and can travel 10 miles in an hour, or 13 miles at a fast pace. When the spell ends, the steed gradually fades, giving the rider 1 minute to dismount. The spell ends if you use an action to dismiss it or if the steed takes any damage.',
        'level': 3,
        'casting_time': '1 minute',
        'range': '30 feet',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Illusion',


    },
    'plant growth': {
        'description': 'This spell channels vitality into plants within a specific area. There are two possible uses for the spell, granting either immediate or long-term benefits.\n\nIf you cast this spell using 1 action, choose a point within range. All normal plants in a 100-foot radius centered on that point become thick and overgrown. A creature moving through the area must spend 4 feet of movement for every 1 foot it moves.\n\nYou can exclude one or more areas of any size within the spell\'s area from being affected.\n\nIf you cast this spell over 8 hours, you enrich the land. All plants in a half-mile radius centered on a point within range become enriched for 1 year. The plants yield twice the normal amount of food when harvested.',
        'level': 3,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Transmutation',


    },
    'protection from energy': {
        'description': 'For the duration, the willing creature you touch has resistance to one damage type of your choice: acid, cold, fire, lightning, or thunder.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Abjuration',
        'concentration': True,

    },
    'psionic blast': {
        'description': 'You unleash a destructive wave of mental power in a 30-foot cone. Each creature in the area must make a Dexterity Saving Throw. On a failed save, a target takes 5d8 force damage, is pushed 20 feet directly away from you, and is knocked prone. On a successful save, a target takes half as much damage and isn\'t pushed or knocked prone.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d8 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self (30-foot cone)',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'remove curse': {
        'description': 'At your touch, all curses affecting one creature or object end. If the object is a cursed magic item, its curse remains, but the spell breaks its owner\'s attunement to the object so it can be removed or discarded.'
        'discarded.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Abjuration',


        },
    'revivify': {
        'description': 'You touch a creature that has died within the last minute. That creature returns to life with 1 hit point. This spell can\'t return to life a creature that has died of old age, nor can it restore any missing body parts.'
        'missing body parts.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M (diamonds worth 300 gp, which the spell consumes)',
        'duration': 'Instantaneous',
        'school': 'Necromancy',


        },
    'sending': {
        'description': 'You send a short message of twenty-five words or less to a creature with which you are familiar. The creature hears the message in its mind, recognizes you as the sender if it knows you, and can answer in a like manner immediately. The spell enables creatures with Intelligence Scores of at least 1 to understand the meaning of your message.\n\nYou can send the message across any distance and even to other planes of existence, but if the target is on a different plane than you, there is a 5 percent chance that the message doesn\'t arrive.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Unlimited',
        'components': 'V, S, M (a short piece of fine copper wire)',
        'duration': '1 round',
        'school': 'Evocation',


        },
    'sleet storm': {
        'description': 'Until the spell ends, freezing rain and sleet fall in a 20-foot-tall cylinder with a 40-foot radius centered on a point you choose within range. The area is heavily obscured, and exposed flames in the area are doused.\n\nThe ground in the area is covered with slick ice, making it difficult terrain. When a creature enters the spell\'s area for the first time on a turn or starts its turn there, it must make a Dexterity Saving Throw. On a failed save, it falls prone.\n\nIf a creature starts its turn in the spell\'s area and is concentrating on a spell, the creature must make a successful Constitution Saving Throw against your Spell Save DC or lose concentration.',
        'level': 3,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S, M (a pinch of dust and a few drops of water)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

        },
    'slow': {
        'description': 'You alter time around up to six creatures of your choice in a 40-foot cube within range. Each target must succeed on a Wisdom Saving Throw or be affected by this spell for the duration.\n\nAn affected target\'s speed is halved, it takes a -2 penalty to AC and Dexterity Saving Throws, and it can\'t use reactions. On its turn, it can use either an action or a bonus action, not both. Regardless of the creature\'s abilities or magic items, it can\'t make more than one melee or Ranged Attack during its turn.\n\nIf the creature attempts to cast a spell with a casting time of 1 action, roll a d20. On an 11 or higher, the spell doesn\'t take effect until the creature\'s next turn, and the creature must use its action on that turn to complete the spell. If it can\'t, the spell is wasted.\n\nA creature affected by this spell makes another Wisdom Saving Throw at the end of each of its turns. On a successful save, the effect ends for it.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M (a drop of molasses)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

        },
    'speak with dead': {
        'description': 'You grant the semblance of life and Intelligence to a corpse of your choice within range, allowing it to answer the questions you pose. The corpse must still have a mouth and can\'t be undead. The spell fails if the corpse was the target of this spell within the last 10 days.\n\nUntil the spell ends, you can ask the corpse up to five questions. The corpse knows only what it knew in life, including the languages it knew. Answers are usually brief, cryptic, or repetitive, and the corpse is under no compulsion to offer a truthful answer if you are hostile to it or it recognizes you as an enemy. This spell doesn\'t return the creature\'s soul to its body, only its animating spirit. Thus, the corpse can\'t learn new information, doesn\'t comprehend anything that has happened since it died, and can\'t speculate about future events.',
        'level': 3,
        'casting_time': '1 action',
        'range': '10 feet',
        'components': 'V, S, M (burning incense)',
        'duration': '10 minutes',
        'school': 'Necromancy',


        },
    'speak with plants': {
        'description': 'You imbue plants within 30 feet of you with limited sentience and animation, giving them the ability to communicate with you and follow your simple commands. You can question plants about events in the spell\'s area within the past day, gaining information about creatures that have passed, weather, and other circumstances.\n\nYou can also turn difficult terrain caused by plant growth (such as thickets and undergrowth) into ordinary terrain that lasts for the duration. Or you can turn ordinary terrain where plants are present into difficult terrain that lasts for the duration, causing vines and branches to hinder pursuers, for example.\n\nPlants might be able to perform other tasks on your behalf, at the DM\'s discretion. The spell doesn\'t enable plants to uproot themselves and move about, but they can freely move branches, tendrils, and stalks.\n\nIf a plant creature is in the area, you can communicate with it as if you shared a common language, but you gain no magical ability to influence it.\n\nThis spell can cause the plants created by the entangle spell to release a restrained creature.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self (30-foot radius)',
        'components': 'V, S',
        'duration': '10 minutes',
        'school': 'Transmutation',


        },
    'spirit guardians': {
        'description': 'You call forth spirits to protect you. They flit around you to a distance of 15 feet for the duration. If you are good or neutral, their spectral form appears angelic or fey (your choice). If you are evil, they appear fiendish.\n\nWhen you cast this spell, you can designate any number of creatures you can see to be unaffected by it. An affected creature\'s speed is halved in the area, and when the creature enters the area for the first time on a turn or starts its turn there, it must make a Wisdom Saving Throw. On a failed save, the creature takes 3d8 radiant damage (if you are good or neutral) or 3d8 necrotic damage (if you are evil). On a successful save, the creature takes half as much damage.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d8 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self (15-foot radius)',
        'components': 'V, S, M (a holy symbol)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Conjuration',
        'concentration': True,

        },
    'stinking cloud': {
        'description': 'You create a 20-foot-radius sphere of yellow, nauseating gas centered on a point within range. The cloud spreads around corners, and its area is heavily obscured. The cloud lingers in the air for the duration.\n\nEach creature that is completely within the cloud at the start of its turn must make a Constitution Saving Throw against poison. On a failed save, the creature spends its action that turn retching and reeling. Creatures that don\'t need to breathe or are immune to poison automatically succeed on this Saving Throw.\n\nA moderate wind (at least 10 miles per hour) disperses the cloud after 4 rounds. A strong wind (at least 20 miles per hour) disperses it after 1 round.',
        'level': 3,
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S, M (a rotten egg or several skunk cabbage leaves)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Conjuration',
        'concentration': True,

        },
    'summon lesser demons': {
        'description': 'You utter foul words, summoning demons from the chaos of the Abyss. Roll on the following table to determine what appears.\n╔═════╤═══════════════════════════════════════════════╗\n║ d6  │ Demons Summoned                               ║\n╠═════╪═══════════════════════════════════════════════╣\n║ 1-2 │ Two demons of challenge rating 1 or lower     ║\n╟─────┼───────────────────────────────────────────────╢\n║ 3-4 │ Four demons of challenge rating 1/2 or lower  ║\n╟─────┼───────────────────────────────────────────────╢\n║ 5-6 │ Eight demons of challenge rating 1/4 or lower ║\n╚═════╧═══════════════════════════════════════════════╝\nThe DM chooses the demons, such as manes or dretches, and you choose the unoccupied spaces you can see within range where they appear. A summoned demon disappears when it drops to 0 hit points or when the spell ends.\n\nThe demons are hostile to all creatures, including you. Roll initiative for the summoned demons as a group, which has its own turns. The demons pursue and attack the nearest non-demons to the best of their ability.\n\nAs part of casting the spell, you can form a circle on the ground with the blood used as a material component. The circle is large enough to encompass your space. While the spell lasts, the summoned demons can\'t cross the circle or harm it, and they can\'t target anyone within it. Using the material component in this manner consumes it when the spell ends.\n\nWhen you cast this spell using a spell slot of 6th or 7th level, you summon twice as many demons. If you cast it using a spell slot of 8th or 9th level, you summon three times as many demons.',
        'level': 3,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 hour',
        'school': 'Conjuration',
        'concentration': True,

        },
    'thunder step': {
        'description': 'You teleport yourself to an unoccupied space you can see within range. Immediately after you disappear, a thunderous boom sounds, and each creature within 10 feet of the space you left must make a Constitution Saving Throw, taking 3d10 thunder damage on a failed save, or half as much damage on a successful one. The thunder can be heard from up to 300 feet away.\n\nYou can bring along objects as long as their weight doesn\'t exceed what you can carry. You can also teleport one willing creature of your size or smaller who is carrying gear up to its carrying capacity. The creature must be within 5 feet of you when you cast this spell, and there must be an unoccupied space within 5 feet of your destination space for the creature to appear in; otherwise, the creature is left behind.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d10 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


        },
    'tidal wave': {
        'description': 'You conjure up a wave of water that crashes down on an area within range. The area can be up to 30 feet long, up to 10 feet wide, and up to 10 feet tall. Each creature in that area must make a Dexterity Saving Throw. On a failed save, a creature takes 4d8 bludgeoning damage and is knocked prone. On a successful save, a creature takes half as much damage and isn\'t knocked prone. The water then spreads out across the ground in all directions, extinguishing unprotected flames in its area and within 30 feet of it, and then it vanishes.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M (a drop of water)',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


        },
    'tiny servant': {
        'description': 'You touch one tiny, nonmagical object that isn\'t attached to another object or a surface and isn\'t being carried by another creature. The target animates and sprouts little arms and legs, becoming a creature under your control until the spell ends or the creature drops to 0 hit points. See the Tiny Servant for its statistics.\n\nAs a bonus action, you can mentally command the creature if it is within 120 feet of you. (If you control multiple creatures with this spell, you can command any or all of them at the same time, issuing the same command to each one.) You decide what action the creature will take and where it will move during its next turn, or you can issue a simple, general command, such as to fetch a key, stand watch, or stack some books. If you issue no commands, the servant does nothing other than defend itself against hostile creatures. Once given an order, the servant continues to follow that order until its task is complete.\n\nWhen the creature drops to 0 hit points, it reverts to its original form, and any remaining damage carries over to that form.\n\nWhen you cast this spell using a spell slot of 4th level or higher, you can animate two additional objects for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 minute',
        'range': 'Touch',
        'components': 'V, S, M (a miniature silver spoon)',
        'duration': '8 hours',
        'school': 'Transmutation',


        },
    'tongues': {
        'description': 'This spell grants the creature you touch the ability to understand any spoken language it hears. Moreover, when the target speaks, any creature that knows at least one language and can hear the target understands what it says.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, M (a small clay model of a ziggurat)',
        'duration': '1 hour',
        'school': 'Divination',


        },
    'vampiric touch': {
        'description': 'The touch of your shadow-wreathed hand can siphon life force from others to heal your wounds. Make a Melee Spell Attack against a creature within your reach. On a hit, the target takes 3d6 necrotic damage, and you regain hit points equal to half the amount of necrotic damage dealt. Until the spell ends, you can make the attack again on each of your turns as an action.\n\nWhen you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd.',
        'level': 3,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Necromancy',
        'concentration': True,

        },
    'wall of sand': {
        'description': 'You create a wall of swirling sand on the ground at a point you can see within range. You can make the wall up to 30 feet long, 10 feet high, and 10 feet thick, and it vanishes when the spell ends. It blocks line of sight but not movement. A creature is blinded while in the wall\'s space and must spend 3 feet of movement for every 1 foot it moves there.',
        'level': 3,
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S, M (a handful of sand)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

        },
    'wall of water': {
        'description': 'You create a wall of water on the ground at a point you can see within range. You can make the wall up to 30 feet long, 10 feet high, and 1 foot thick, or you can make a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick. The wall vanishes when the spell ends. The wall\'s space is difficult terrain.\n\nAny Ranged Weapon Attack that enters the wall\'s space has disadvantage on the Attack Roll, and fire damage is halved if the fire effect passes through the wall to reach its target. Spells that deal cold damage that pass through the wall cause the area of the wall they pass through to freeze solid (at least a 5-foot-square section is frozen). Each 5-foot-square frozen section has AC 5 and 15 hit points. Reducing a frozen section to 0 hit points destroys it. When a section is destroyed, the wall\'s water doesn\'t fill it.',
        'level': 3,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M (a drop of water)',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

        },
    'water breathing': {
        'description': 'This spell grants up to ten willing creatures you can see within range the ability to breathe underwater until the spell ends. Affected creatures also retain their normal mode of respiration.',
        'level': 3,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a short reed or piece of straw)',
        'duration': '24 hours',
        'school': 'Transmutation',


        },
    'water walk': {
        'description': 'This spell grants the ability to move across any liquid surface—such as water, acid, mud, snow, quicksand, or lava—as if it were harmless solid ground (creatures crossing molten lava can still take damage from the heat). Up to ten willing creatures you can see within range gain this ability for the duration.\n\nIf you target a creature submerged in a liquid, the spell carries the target to the surface of the liquid at a rate of 60 feet per round.',
        'level': 3,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V, S, M (a piece of cork)',
        'duration': '1 hour',
        'school': 'Transmutation',


        },
    'wind wall': {
        'description': 'A wall of strong wind rises from the ground at a point you choose within range. You can make the wall up to 50 feet long, 15 feet high, and 1 foot thick. You can shape the wall in any way you choose so long as it makes one continuous path along the ground. The wall lasts for the duration.\n\nWhen the wall appears, each creature within its area must make a Strength Saving Throw. A creature takes 3d8 bludgeoning damage on a failed save, or half as much damage on a successful one.\n\nThe strong wind keeps fog, smoke, and other gases at bay. Small or smaller flying creatures or objects can\'t pass through the wall. Loose, lightweight materials brought into the wall fly upward. Arrows, bolts, and other ordinary projectiles launched at targets behind the wall are deflected upward and automatically miss. (Boulders hurled by giants or siege engines, and similar projectiles, are unaffected.) Creatures in gaseous form can\'t pass through it.',
        'level': 3,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M (a tiny fan and a feather of exotic origin)',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

        }

}


