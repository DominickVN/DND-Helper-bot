sixth_level_spells = {
    'arcane gate': {
        'description': 'You create linked teleportation portals that remain open for the duration. Choose two points on the ground that you can see, one point within 10 feet of you and one point within 500 feet of you. A circular portal, 10 feet in diameter, opens over each point. If the portal would open in the space occupied by a creature, the spell fails, and the casting is lost.\n\nThe portals are two-dimensional glowing rings filled with mist, hovering inches from the ground and perpendicular to it at the points you choose. A ring is visible only from one side (your choice), which is the side that functions as a portal.\n\nAny creature or object entering the portal exits from the other portal as if the two were adjacent to each other; passing through a portal from the nonportal side has no effect. The mist that fills each portal is opaque and blocks vision through it. On your turn, you can rotate the rings as a bonus action so that the active side faces in a different direction.',
        'level': 6,
        'casting_time': '1 action',
        'range': '500 feet',
        'components': 'V, S',
        'duration': 'Up to 10 minutes',
        'school': 'Conjuration',


    },
    'blade barrier': {
        'description': 'You create a vertical wall of whirling, razor-sharp blades made of magical energy. The wall appears within range and lasts for the duration. You can make a straight wall up to 100 feet long, 20 feet high, and 5 feet thick, or a ringed wall up to 60 feet in diameter, 20 feet high, and 5 feet thick. The wall provides three-quarters cover to creatures behind it, and its space is difficult terrain.\n\nWhen a creature enters the wall\'s area for the first time on a turn or starts its turn there, the creature must make a Dexterity Saving Throw. On a failed save, the creature takes 6d10 slashing damage. On a successful save, the creature takes half as much damage.',
        'level': 6,
        'casting_time': '1 action',
        'range': '90 feet',
        'components': 'V, S',
        'duration': 'Up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

    },
    'bones of the earth': {
        'description': 'You cause up to six pillars of stone to burst from places on the ground that you can see within range. Each pillar is a cylinder that has a diameter of 5 feet and a height of up to 30 feet. The ground where a pillar appears must be wide enough for its diameter, and you can target the ground under a creature if that creature is medium or smaller. Each pillar has AC 5 and 30 hit points. When reduced to 0 hit points, a pillar crumbles into rubble, which creates an area of difficult terrain with a 10-foot radius that lasts until the rubble is cleared. Each 5-foot-diameter portion of the area requires at least 1 minute to clear by hand.\n\nIf a pillar is created under a creature, that creature must succeed on a Dexterity Saving Throw or be lifted by the pillar. A creature can choose to fail the save.\n\nIf a pillar is prevented from reaching its full height because of a ceiling or other obstacle, a creature on the pillar takes 6d6 bludgeoning damage and is restrained, pinched between the pillar and the obstacle. The restrained creature can use an action to make a Strength or Dexterity Check (the creature\'s choice) against the spell\'s save DC. On a success, the creature is no longer restrained and must either move off the pillar or fall off it.\n\nWhen you cast this spell using a spell slot of 7th level or higher, you can create two additional pillars for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M',
        'duration': 'Up to 1 minute',
        'school': 'Transmutation',


    },
    'chain lightning': {
        'description': 'You create a bolt of lightning that arcs toward a target of your choice that you can see within range. Three bolts then leap from that target to as many as three other targets, each of which must be within 30 feet of the first target. A target can be a creature or an object and can be targeted by only one of the bolts.\n\nA target must make a Dexterity Saving Throw. The target takes 10d8 lightning damage on a failed save, or half as much damage on a successful one.\n\nWhen you cast this spell using a spell slot of 7th level or higher, one additional bolt leaps from the first target to another target for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'circle of death': {
        'description': 'A sphere of negative energy ripples out in a 60-foot-radius sphere from a point within range. Each creature in that area must make a Constitution Saving Throw. A target takes 8d6 necrotic damage on a failed save, or half as much damage on a successful one.\n\nWhen you cast this spell using a spell slot of 7th level or higher, the damage increases by 2d6 for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': '150 feet',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Necromancy',


    },
    'conjure fey': {
        'description': 'You summon a fey creature of challenge rating 6 or lower, or a fey spirit that takes the form of a beast of challenge rating 6 or lower. It appears in an unoccupied space that you can see within range. The fey creature disappears when it drops to 0 hit points or when the spell ends.\n\nThe fey creature is friendly to you and your companions for the duration. Roll initiative for the creature, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you), as long as they don\'t violate its alignment. If you don\'t issue any commands to the fey creature, it defends itself from hostile creatures but otherwise takes no actions.\n\nIf your concentration is broken, the fey creature doesn\'t disappear. Instead, you lose control of the fey creature, it becomes hostile toward you and your companions, and it might attack. An uncontrolled fey creature can\'t be dismissed by you, and it disappears 1 hour after you summoned it.\n\nThe DM has the fey creature\'s statistics.\n\nWhen you cast this spell using a spell slot of 7th level or higher, the challenge rating increases by 1 for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 minute',
        'range': '90 feet',
        'components': 'V, S',
        'duration': 'Up to 1 hour',
        'school': 'Conjuration',
        'concentration': True,

    },
    'contingency': {
        'description': 'Choose a spell of 5th level or lower that you can cast, that has a casting time of 1 action, and that can target you. You cast that spell—called the contingent spell—as part of casting contingency, expending spell slots for both, but the contingent spell doesn\'t come into effect. Instead, it takes effect when a certain circumstance occurs. You describe that circumstance when you cast the two spells. For example, a contingency cast with water breathing might stipulate that water breathing comes into effect when you are engulfed in water or a similar liquid.\n\nThe contingent spell takes effect immediately after the circumstance is met for the first time, whether or not you want it to, and then contingency ends.\n\nThe contingent spell takes effect only on you, even if it can normally target others. You can use only one contingency spell at a time. If you cast this spell again, the effect of another contingency spell on you ends. Also, contingency ends on you if its material component is ever not on your person.',
        'level': 6,
        'casting_time': '10 minutes',
        'range': 'Self',
        'components': 'V, S, M',
        'duration': '10 days',
        'school': 'Evocation',


    },
    'create homunculus': {
        'description': 'While speaking an intricate incantation, you cut yourself with a jewel-encrusted dagger, taking 2d4 piercing damage that can\'t be reduced in any way. You then drip your blood on the spell\'s other components and touch them, transforming them into a special construct called a Homunculus.\n\nThe statistics of the Homunculus are in the Monster Manual. It is your faithful companion, and it dies if you die. Whenever you finish a long rest, you can spend up to half your Hit Dice if the homunculus is on the same plane of existence as you. When you do so, roll each die and add your Constitution Modifier to it. Your hit point maximum is reduced by the total, and the homunculus\'s hit point maximum and current hit points are both increased by it. This process can reduce you to no lower than 1 hit point, and the change to your and the homunculus\'s hit points ends when you finish your next long rest. The reduction to your hit point maximum can\'t be removed by any means before then, except by the homunculus\'s death.\n\nYou can have only one homunculus at a time. If you cast this spell while your homunculus lives, the spell fails.',
        'level': 6,
        'casting_time': '1 hour',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Transmutation',


    },
    'create undead': {
        'description': 'You can cast this spell only at night. Choose up to three corpses of medium or small humanoids within range. Each corpse becomes a Ghoul under your control. (The DM has game statistics for these creatures.)\n\nAs a bonus action on each of your turns, you can mentally command any creature you animated with this spell if the creature is within 120 feet of you (if you control multiple creatures, you can command any or all of them at the same time, issuing the same command to each one). You decide what action the creature will take and where it will move during its next turn, or you can issue a general command, such as to guard a particular chamber or corridor. If you issue no commands, the creature only defends itself against hostile creatures. Once given an order, the creature continues to follow it until its task is complete.\n\nThe creature is under your control for 24 hours, after which it stops obeying any command you have given it. To maintain control of the creature for another 24 hours, you must cast this spell on the creature before the current 24-hour period ends. This use of the spell reasserts your control over up to three creatures you have animated with this spell, rather than animating new ones.\n\nWhen you cast this spell using a 7th-level spell slot, you can animate or reassert control over four Ghouls. When you cast this spell using an 8th-level spell slot, you can animate or reassert control over five Ghouls or two Ghasts or Wights. When you cast this spell using a 9th-level spell slot, you can animate or reassert control over six Ghouls, three Ghasts or Wights, or two Mummies.',
        'level': 6,
        'casting_time': '1 minute',
        'range': '10 feet',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Necromancy',


    },
    'disintegrate': {
        'description': 'A thin green ray springs from your pointing finger to a target that you can see within range. The target can be a creature, an object, or a creation of magical force, such as the wall created by wall of force.\n\nA creature targeted by this spell must make a Dexterity Saving Throw. On a failed save, the target takes 10d6 + 40 force damage. The target is disintegrated if this damage leaves it with 0 hit points.\n\nA disintegrated creature and everything it is wearing and carrying, except magic items, are reduced to a pile of fine gray dust. The creature can be restored to life only by means of a true resurrection or a wish spell.\n\nThis spell automatically disintegrates a large or smaller nonmagical object or a creation of magical force. If the target is a huge or larger object or creation of force, this spell disintegrates a 10-foot-cube portion of it. A magic item is unaffected by this spell.\n\nWhen you cast this spell using a spell slot of 7th level or higher, the damage increases by 3d6 for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Transmutation',


    },
    "drawmij's instant summons": {
        'description': 'You touch an object weighing 10 pounds or less whose longest dimension is 6 feet or less. The spell leaves an invisible mark on its surface and invisibly inscribes the name of the item on the sapphire you use as the material component. Each time you cast this spell, you must use a different sapphire.\n\nAt any time thereafter, you can use your action to speak the item\'s name and crush the sapphire. The item instantly appears in your hand regardless of physical or planar distances, and the spell ends.\n\nIf another creature is holding or carrying the item, crushing the sapphire doesn\'t transport the item to you, but instead you learn who the creature possessing the object is and roughly where that creature is located at that moment.\n\nDispel magic or a similar effect successfully applied to the sapphire ends this spell\'s effect.',
        'level': 6,
        'casting_time': '1 minute',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': 'Until dispelled',
        'school': 'Conjuration',


    },
    'druid grove': {
        'description': 'You invoke the spirits of nature to protect an area outdoors or underground. The area can be as small as a 30-foot cube or as large as a 90-foot cube. Buildings and other structures are excluded from the affected area. If you cast this spell in the same area every day for a year, the spell lasts until dispelled.\n\nThe spell creates the following effects within the area. When you cast this spell, you can specify creatures as friends who are immune to the effects. You can also specify a password that, when spoken aloud, makes the speaker immune to these effects.\n\nThe entire warded area radiates magic. A dispel magic cast on the area, if successful, removes only one of the following effects, not the entire area. That spell\'s caster chooses which effect to end. Only when all its effects are gone is this spell dispelled.\n\nSolid Fog\nYou can fill any number of 5-foot squares on the ground with thick fog, making them heavily obscured. The fog reaches 10 feet high. In addition, every foot of movement through the fog costs 2 extra feet. To a creature immune to this effect, the fog obscures nothing and looks like soft mist, with motes of green light floating in the air.\n\nGrasping Undergrowth\nYou can fill any number of 5-foot squares on the ground that aren\'t filled with fog with grasping weeds and vines, as if they were affected by an entangle spell. To a creature immune to this effect, the weeds and vines feel soft and reshape themselves to serve as temporary seats or beds.\n\nGrove Guardians\nYou can animate up to four trees in the area, causing them to uproot themselves from the ground. These trees have the same statistics as an awakened tree, which appears in the Monster Manual, except they can\'t speak, and their bark is covered with druidic symbols. If any creature not immune to this effect enters the warded area, the grove guardians fight until they have driven off or slain the intruders. The grove guardians also obey your spoken commands (no action required by you) that you issue while in the area. If you don\'t give them commands and no intruders are present, the grove guardians do nothing. The grove guardians can\'t leave the warded area. When the spell ends, the magic animating them disappears, and the trees take root again if possible.\n\nAdditional Spell Effect\nYou can place your choice of one of the following magical effects within the warded area:\n\n•A constant gust of wind in two locations of your choice\n•Spike growth in one location of your choice\n•Wind wall in two locations of your choice\n\nTo a creature immune to this effect, the winds are a fragrant, gentle breeze, and the area of spike growth is harmless.',
        'level': 6,
        'casting_time': '10 minutes',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': '24 hours',
        'school': 'Abjuration',


    },
    'eyebite': {
        'description': 'For the spell\'s duration, your eyes become an inky void imbued with dread power. One creature of your choice within 60 feet of you that you can see must succeed on a Wisdom Saving Throw or be affected by one of the following effects of your choice for the duration. On each of your turns until the spell ends, you can use your action to target another creature but can\'t target a creature again if it has succeeded on a Saving Throw against this casting of eyebite.\n\nAsleep\nThe target falls unconscious. It wakes up if it takes any damage or if another creature uses its action to shake the sleeper awake.\n\nPanicked\nThe target is frightened of you. On each of its turns, the frightened creature must take the dash action and move away from you by the safest and shortest available route, unless there is nowhere to move. If the target moves to a place at least 60 feet away from you where it can no longer see you, this effect ends.\n\nSickened\nThe target has disadvantage on Attack Rolls and Ability Checks. At the end of each of its turns, it can make another Wisdom Saving Throw. If it succeeds, the effect ends.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Up to 1 minute',
        'school': 'Necromancy',
        'concentration': True,

    },
    'find the path': {
        'description': 'This spell allows you to find the shortest, most direct physical route to a specific fixed location that you are familiar with on the same plane of existence. If you name a destination on another plane of existence, a destination that moves (such as a mobile fortress), or a destination that isn\'t specific (such as "a green dragon\'s lair"), the spell fails.\n\nFor the duration, as long as you are on the same plane of existence as the destination, you know how far it is and in what direction it lies. While you are traveling there, whenever you are presented with a choice of paths along the way, you automatically determine which path is the shortest and most direct route (but not necessarily the safest route) to the destination.',
        'level': 6,
        'casting_time': '1 minute',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Up to 24 hours',
        'school': 'Divination',
        'concentration': True,

    },
    'flesh to stone': {
        'description': 'You attempt to turn one creature that you can see within range into stone. If the target\'s body is made of flesh, the creature must make a Constitution Saving Throw. On a failed save, it is restrained as its flesh begins to harden. On a successful save, the creature isn\'t affected.\n\nA creature restrained by this spell must make another Constitution Saving Throw at the end of each of its turns. If it successfully saves against this spell three times, the spell ends. If it fails its saves three times, it is turned to stone and subjected to the petrified condition for the duration. The successes and failures don\'t need to be consecutive; keep track of both until the target collects three of a kind.\n\nIf the creature is physically broken while petrified, it suffers from similar deformities if it reverts to its original state.\n\nIf you maintain your concentration on this spell for the entire possible duration, the creature is turned to stone until the effect is removed.',
        'level': 6,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M',
        'duration': 'Up to 1 minute',
        'school': 'Transmutation',
        'concentration': True,

    },
    'forbiddance': {
        'description': 'You create a ward against magical travel that protects up to 40,000 square feet of floor space to a height of 30 feet above the floor. For the duration, creatures can\'t teleport into the area or use portals, such as those created by the gate spell, to enter the area. The spell proofs the area against planar travel, and therefore prevents creatures from accessing the area by way of the Astral Plane, Ethereal Plane, Feywild, Shadowfell, or the plane shift spell.\n\nIn addition, the spell damages types of creatures that you choose when you cast it. Choose one or more of the following: celestials, elementals, fey, fiends, and undead. When a chosen creature enters the spell\'s area for the first time on a turn or starts its turn there, the creature takes 5d10 radiant or necrotic damage (your choice when you cast this spell).\n\nWhen you cast this spell, you can designate a password. A creature that speaks the password as it enters the area takes no damage from the spell.\n\nThe spell\'s area can\'t overlap with the area of another forbiddance spell. If you cast forbiddance every day for 30 days in the same location, the spell lasts until it is dispelled, and the material components are consumed on the last casting.',
        'level': 6,
        'casting_time': '10 minutes',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': '24 hours',
        'school': 'Abjuration',

        'ritual': True
    },
    'globe of invulnerability': {
        'description': 'An immobile, faintly shimmering barrier springs into existence in a 10-foot radius around you and remains for the duration.\n\nAny spell of 5th level or lower cast from outside the barrier can\'t affect creatures or objects within it, even if the spell is cast using a higher level spell slot. Such a spell can target creatures and objects within the barrier, but the spell has no effect on them. Similarly, the area within the barrier is excluded from the areas affected by such spells.\n\nWhen you cast this spell using a spell slot of 7th level or higher, the barrier blocks spells of one level higher for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Up to 1 minute',
        'school': 'Abjuration',
        'concentration': True,

    },
    'guards and wards': {
        'description': 'You create a ward that protects up to 2,500 square feet of floor space (an area 50 feet square, or one hundred 5-foot squares or twenty-five 10-foot squares). The warded area can be up to 20 feet tall, and shaped as you desire. You can ward several stories of a stronghold by dividing the area among them, as long as you can walk into each contiguous area while you are casting the spell.\n\nWhen you cast this spell, you can specify individuals that are unaffected by any or all of the effects that you choose. You can also specify a password that, when spoken aloud, makes the speaker immune to these effects.\n\nGuards and wards creates the following effects within the warded area.\n\nCorridors\nFog fills all the warded corridors, making them heavily obscured. In addition, at each intersection or branching passage offering a choice of direction, there is a 50 percent chance that a creature other than you will believe it is going in the opposite direction from the one it chooses.\n\nDoors\nAll doors in the warded area are magically locked, as if sealed by an arcane lock spell. In addition, you can cover up to ten doors with an illusion (equivalent to the illusory object function of the minor illusion spell) to make them appear as plain sections of wall.\n\nStairs\nWebs fill all stairs in the warded area from top to bottom, as the web spell. These strands regrow in 10 minutes if they are burned or torn away while guards and wards lasts.\n\nOther Spell Effect\nYou can place your choice of one of the following magical effects within the warded area of the stronghold.\n\nPlace dancing lights in four corridors. You can designate a simple program that the lights repeat as long as guards and wards lasts.\nPlace magic mouth in two locations.\nPlace stinking cloud in two locations. The vapors appear in the places you designate; they return within 10 minutes if dispersed by wind while guards and wards lasts.\nPlace a constant gust of wind in one corridor or room.\nPlace a suggestion in one location. You select an area of up to 5 feet square, and any creature that enters or passes through the area receives the suggestion mentally.\n\nThe whole warded area radiates magic. A dispel magic cast on a specific effect, if successful, removes only that effect.\n\nYou can create a permanently guarded and warded structure by casting this spell there every day for one year.',
        'level': 6,
        'casting_time': '10 minutes',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': '24 hours',
        'school': 'Abjuration',

        'ritual': True
    },
    'harm': {
        'description': 'You unleash a virulent disease on a creature that you can see within range. The target must make a Constitution Saving Throw. On a failed save, it takes 14d6 necrotic damage, or half as much damage on a successful save. The damage can\'t reduce the target\'s hit points below 1. If the target fails the Saving Throw, its hit point maximum is reduced for 1 hour by an amount equal to the necrotic damage it took. Any effect that removes a disease allows a creature\'s hit point maximum to return to normal before that time passes.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Necromancy',


    },
    'heal': {
        'description': 'Choose a creature that you can see within range. A surge of positive energy washes through the creature, causing it to regain 70 hit points. This spell also ends blindness, deafness, and any diseases affecting the target. This spell has no effect on constructs or undead.\n\nWhen you cast this spell using a spell slot of 7th level or higher, the amount of healing increases by 10 for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'hero\'s feast': {
        'description': 'You bring forth a great feast, including magnificent food and drink. The feast takes 1 hour to consume and disappears at the end of that time, and the beneficial effects don\'t set in until this hour is over. Up to twelve creatures can partake of the feast.\n\nA creature that partakes of the feast gains several benefits. The creature is cured of all diseases and poison, becomes immune to poison and being frightened, and makes all Wisdom Saving Throws with advantage. Its hit point maximum also increases by 2d10, and it gains the same number of hit points. These benefits last for 24 hours.',
        'level': 6,
        'casting_time': '10 minutes',
        'range': '30 feet',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'investiture of flame': {
        'description': 'Flames race across your body, shedding bright light in a 30-foot radius and dim light for an additional 30 feet for the spell\'s duration. The flames don\'t harm you. Until the spell ends, you gain the following benefits:\n\n•You are immune to fire damage and have resistance to cold damage.\n•Any creature that moves within 5 feet of you for the first time on a turn or ends its turn there takes 1d10 fire damage.\n•You can use your action to create a line of fire 15 feet long and 5 feet wide extending from you in a direction you choose. Each creature in the line must make a Dexterity Saving Throw. A creature takes 4d8 fire damage on a failed save, or half as much damage on a successful one.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'investiture of ice': {
        'description': 'Until the spell ends, ice rimes your body, and you gain the following benefits:\n\n•You are immune to cold damage and have resistance to fire damage.\n•You can move across difficult terrain created by ice or snow without spending extra movement.\n•The ground in a 10-foot radius around you is icy and is difficult terrain for creatures other than you. The radius moves with you.\n•You can use your action to create a 15-foot cone of freezing wind extending from your outstretched hand in a direction you choose. Each creature in the cone must make a Constitution Saving Throw. A creature takes 4d6 cold damage on a failed save, or half as much damage on a successful one. A creature that fails its save against this effect has its speed halved until the start of your next turn.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'investiture of stone': {
        'description': 'Until the spell ends, bits of rock spread across your body, and you gain the following benefits:\n\n•You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks.\n•You can use your action to create a small earthquake on the ground in a 15-foot radius centered on you. Other creatures on that ground must succeed on a Dexterity Saving Throw or be knocked prone.\n•You can move across difficult terrain made of earth or stone without spending extra movement. You can move through solid earth or stone as if it was air and without destabilizing it, but you can\'t end your movement there. If you do so, you are ejected to the nearest unoccupied space, this spell ends, and you are stunned until the end of your next turn.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'investiture of wind': {
        'description': 'Until the spell ends, wind whirls around you, and you gain the following benefits:\n\n•Ranged Weapon Attacks made against you have disadvantage on the Attack Roll.\n•You gain a flying speed of 60 feet. If you are still flying when the spell ends, you fall, unless you can somehow prevent it.\n•You can use your action to create a 15-foot cube of swirling wind centered on a point you can see within 60 feet of you. Each creature in that area must make a Constitution Saving Throw. A creature takes 2d10 bludgeoning damage on a failed save, or half as much damage on a successful one. If a large or smaller creature fails the save, that creature is also pushed up to 10 feet away from the center of the cube.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'magic jar': {
        'description': 'Your body falls into a catatonic state as your soul leaves it and enters the container you used for the spell\'s material component. While your soul inhabits the container, you are aware of your surroundings as if you were in the container\'s space. You can\'t move or use reactions. The only action you can take is to project your soul up to 100 feet out of the container, either returning to your living body (and ending the spell) or attempting to possess a humanoids body.\n\nYou can attempt to possess any humanoid within 100 feet of you that you can see (creatures warded by a protection from evil and good or magic circle spell can\'t be possessed). The target must make a Charisma Saving Throw. On a failure, your soul moves into the target\'s body, and the target\'s soul becomes trapped in the container. On a success, the target resists your efforts to possess it, and you can\'t attempt to possess it again for 24 hours.\n\nOnce you possess a creature\'s body, you control it. Your game statistics are replaced by the statistics of the creature, though you retain your alignment and your Intelligence, Wisdom, and Charisma Scores. You retain the benefit of your own class features. If the target has any class levels, you can\'t use any of its class features.\n\nMeanwhile, the possessed creature\'s soul can perceive from the container using its own senses, but it can\'t move or take actions at all.\n\nWhile possessing a body, you can use your action to return from the host body to the container if it is within 100 feet of you, returning the host creature\'s soul to its body. If the host body dies while you\'re in it, the creature dies, and you must make a Charisma Saving Throw against your own spellcasting DC. On a success, you return to the container if it is within 100 feet of you. Otherwise, you die.\n\nIf the container is destroyed or the spell ends, your soul immediately returns to your body. If your body is more than 100 feet away from you or if your body is dead when you attempt to return to it, you die. If another creature\'s soul is in the container when it is destroyed, the creature\'s soul returns to its body if the body is alive and within 100 feet. Otherwise, that creature dies.\n\nWhen the spell ends, the container is destroyed.',
        'level': 6,
        'casting_time': '1 minute',
        'range': 'Self',
        'components': 'V, S, M',
        'duration': 'Until dispelled',
        'school': 'Necromancy',


    },
    'mass suggestion': {
        'description': 'You suggest a course of activity (limited to a sentence or two) and magically influence up to twelve creatures of your choice that you can see within range and that can hear and understand you. Creatures that can\'t be charmed are immune to this effect. The suggestion must be worded in such a manner as to make the course of action sound reasonable. Asking the creature to stab itself, throw itself onto a spear, immolate itself, or do some other obviously harmful act automatically negates the effect of the spell.\n\nEach target must make a Wisdom Saving Throw. On a failed save, it pursues the course of action you described to the best of its ability. The suggested course of action can continue for the entire duration. If the suggested activity can be completed in a shorter time, the spell ends when the subject finishes what it was asked to do.\n\nYou can also specify conditions that will trigger a special activity during the duration. For example, you might suggest that a group of soldiers give all their money to the first beggar they meet. If the condition isn\'t met before the spell ends, the activity isn\'t performed.\n\nIf you or any of your companions damage a creature affected by this spell, the spell ends for that creature.\n\nWhen you cast this spell using a 7th-level spell slot, the duration is 10 days. When you use an 8th-level spell slot, the duration is 30 days. When you use a 9th-level spell slot, the duration is a year and a day.',
        'level': 6,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, M',
        'duration': '24 hours',
        'school': 'Enchantment',


    },
    'mental prison': {
        'description': 'You attempt to bind a creature within an illusory cell that only it perceives. One creature you can see within range must make an Intelligence Saving Throw. The target succeeds automatically if it is immune to being charmed. On a successful save, the target takes 5d10 psychic damage, and the spell ends. On a failed save, the target takes 5d10 psychic damage, and you make the area immediately around the target\'s space appear dangerous to it in some way. You might cause the target to perceive itself as being surrounded by fire, floating razors, or hideous maws filled with dripping teeth. Whatever form the illusion takes, the target can\'t see or hear anything beyond it and is restrained for the spell\'s duration. If the target is moved out of the illusion, makes a Melee Attack through it, or reaches any part of its body through it, the target takes 10d10 psychic damage, and the spell ends.',
        'level': 6,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S',
        'duration': '1 minute',
        'school': 'Illusion',


    },
    'move earth': {
        'description': 'Choose an area of terrain no larger than 40 feet on a side within range. You can reshape dirt, sand, or clay in the area in any manner you choose for the duration. You can raise or lower the area\'s elevation, create or fill in a trench, erect or flatten a wall, or form a pillar. The extent of any such changes can\'t exceed half the area\'s largest dimension. So, if you affect a 40-foot square, you can create a pillar up to 20 feet high, raise or lower the square\'s elevation by up to 20 feet, dig a trench up to 20 feet deep, and so on. It takes 10 minutes for these changes to complete.\n\nAt the end of every 10 minutes you spend concentrating on the spell, you can choose a new area of terrain to affect.\n\nBecause the terrain\'s transformation occurs slowly, creatures in the area can\'t usually be trapped or injured by the ground\'s movement.\n\nThis spell can\'t manipulate natural stone or stone construction. Rocks and structures shift to accommodate the new terrain. If the way you shape the terrain would make a structure unstable, it might collapse.\n\nSimilarly, this spell doesn\'t directly affect plant growth. The moved earth carries any plants along with it.',
        'level': 6,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M',
        'duration': 'Up to 2 hours',
        'school': 'Transmutation',
        'concentration': True,

    },
    'otiluke\'s freezing sphere': {
        'description': 'A frigid globe of cold energy streaks from your fingertips to a point of your choice within range, where it explodes in a 60-foot-radius sphere. Each creature within the area must make a Constitution Saving Throw. On a failed save, a creature takes 10d6 cold damage. On a successful save, it takes half as much damage.\n\nIf the globe strikes a body of water or a liquid that is principally water (not including water-based creatures), it freezes the liquid to a depth of 6 inches over an area 30 feet square. This ice lasts for 1 minute. Creatures that were swimming on the surface of frozen water are trapped in the ice. A trapped creature can use an action to make a Strength Check against your Spell Save DC to break free.\n\nYou can refrain from firing the globe after completing the spell, if you wish. A small globe about the size of a sling stone, cool to the touch, appears in your hand. At any time, you or a creature you give the globe to can throw the globe (to a range of 40 feet) or hurl it with a sling (to the sling\'s normal range). It shatters on impact, with the same effect as the normal casting of the spell. You can also set the globe down without shattering it. After 1 minute, if the globe hasn\'t already shattered, it explodes.\n\nWhen you cast this spell using a spell slot of 7th level or higher, the damage increases by 1d6 for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': '300 feet',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Evocation',


    },
    'otto\'s irresistible dance': {
        'description': 'Choose one creature that you can see within range. The target begins a comic dance in place: shuffling, tapping its feet, and capering for the duration. Creatures that can\'t be charmed are immune to this spell.\n\nA dancing creature must use all its movement to dance without leaving its space and has disadvantage on Dexterity Saving Throws and Attack Rolls. While the target is affected by this spell, other creatures have advantage on Attack Rolls against it. As an action, a dancing creature makes a Wisdom Saving Throw to regain control of itself. On a successful save, the spell ends.',
        'level': 6,
        'casting_time': '1 action',
        'range': '30 feet',
        'components': 'V',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'planar ally': {
        'description': 'You beseech an otherworldly entity for aid. The being must be known to you: a god, a primordial, a demon prince, or some other being of cosmic power. That entity sends a celestial, an elemental, or a fiend loyal to it to aid you, making the creature appear in an unoccupied space within range. If you know a specific creature\'s name, you can speak that name when you cast this spell to request that creature, though you might get a different creature anyway (DM\'s choice).\n\nWhen the creature appears, it is under no compulsion to behave in any particular way. You can ask the creature to perform a service in exchange for payment, but it isn\'t obliged to do so. The requested task could range from simple (fly us across the chasm, or help us fight a battle) to complex (spy on our enemies, or protect us during our foray into the dungeon). You must be able to communicate with the creature to bargain for its services.\n\nPayment can take a variety of forms. A celestial might require a sizable donation of gold or magic items to an allied temple, while a fiend might demand a living sacrifice or a gift of treasure. Some creatures might exchange their service for a quest undertaken by you.\n\nAs a rule of thumb, a task that can be measured in minutes requires a payment worth 100 gp per minute. A task measured in hours requires 1,000 gp per hour. And a task measured in days (up to 10 days) requires 10,000 gp per day. The DM can adjust these payments based on the circumstances under which you cast the spell. If the task is aligned with the creature\'s ethos, the payment might be halved or even waived. Nonhazardous tasks typically require only half the suggested payment, while especially dangerous tasks might require a greater gift. Creatures rarely accept tasks that seem suicidal.\n\nAfter the creature completes the task, or when the agreed-upon duration of service expires, the creature returns to its home plane after reporting back to you, if appropriate to the task and if possible. If you are unable to agree on a price for the creature\'s service, the creature immediately returns to its home plane.\n\nA creature enlisted to join your group counts as a member of it, receiving a full share of experience points awarded.',
        'level': 6,
        'casting_time': '10 minutes',
        'range': '60 feet',
        'components': 'V, S, M',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'primordial ward': {
        'description': 'You have resistance to acid, cold, fire, lightning, and thunder damage for the spell\'s duration.\n\nWhen you take damage of one of those types, you can use your reaction to gain immunity to that type of damage, including against the triggering damage. If you do so, the resistances end, and you have the immunity until the end of your next turn, at which time the spell ends.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': '1 hour',
        'school': 'Abjuration',


    },
    'programmed illusion': {
        'description': 'You create an illusion of an object, a creature, or some other visible phenomenon within range that activates when a specific condition occurs. The illusion is imperceptible until then. It must be no larger than a 30-foot cube, and you decide when you cast the spell how the illusion behaves and what sounds it makes. This scripted performance can last up to 5 minutes.\n\nWhen the condition you specify occurs, the illusion springs into existence and performs in the manner you described. Once the illusion finishes performing, it disappears and remains dormant for 10 minutes. After this time, the illusion can be activated again.\n\nThe triggering condition can be as general or as detailed as you like, though it must be based on visual or audible conditions that occur within 30 feet of the area. For example, you could create an illusion of yourself to appear and warn off others who attempt to open a trapped door, or you could set the illusion to trigger only when a creature says the correct word or phrase.\n\nPhysical interaction with the image reveals it to be an illusion, because things can pass through it. A creature that uses its action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your Spell Save DC. If a creature discerns the illusion for what it is, the creature can see through the image, and any noise it makes sounds hollow to the creature.',
        'level': 6,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M',
        'duration': 'Until dispelled',
        'school': 'Illusion',


    },
    'psychic crush': {
        'description': 'You overload the mind of one creature you can see within range, filling its psyche with discordant emotions. The target must make an Intelligence Saving Throw. On a failed save, the target takes 12d6 psychic damage and is stunned for 1 minute. On a successful save, the target takes half as much damage and isn\'t stunned.\n\nThe stunned target can make an Intelligence Saving Throw at the end of each of its turns. On a successful save, the spell ends on the target.',
        'level': 6,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Enchantment',
        'concentration': True,

    },
    'scatter': {
        'description': 'The air quivers around up to five creatures of your choice that you can see within range. An unwilling creature must succeed on a Wisdom Saving Throw to resist this spell. You teleport each affected target to an unoccupied space that you can see within 120 feet of you. That space must be on the ground or on a floor.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Anywhere within 1 mile',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    },
    'soul cage': {
        'description': 'This spell snatches the soul of a humanoid as it dies and traps it inside the tiny cage you use for the material component. A stolen soul remains inside the cage until the spell ends or until you destroy the cage, which ends the spell. While you have a soul inside the cage, you can exploit it in any of the ways described below. You can use a trapped soul up to six times. Once you exploit a soul for the sixth time, it is released, and the spell ends. While a soul is trapped, the dead humanoid it came from can\'t be revived.\n\nSteal Life\nYou can use a bonus action to drain vigor from the soul and regain 2d8 hit points.\n\nQuery Soul\nYou ask the soul a question (no action required) and receive a brief telepathic answer, which you can understand regardless of the language used. The soul knows only what it knew in life, but it must answer you truthfully and to the best of its ability. The answer is no more than a sentence or two and might be cryptic.\n\nBorrow Experience\nYou can use a bonus action to bolster yourself with the soul\'s life experience, making your next Attack Roll, Ability Check, or Saving Throw with advantage. If you don\'t use this benefit before the start of your next turn, it is lost.\n\nEyes of the Dead\nYou can use an action to name a place the humanoid saw in life, which creates an invisible sensor somewhere in that place if it is on the plane of existence you\'re currently on. The sensor remains for as long as you concentrate, up to 10 minutes (as if you were concentrating on a spell). You receive visual and auditory information from the sensor as if you were in its space using your senses.\n\nA creature that can see the sensor (such as one using see invisibility or truesight) sees a translucent image of the tormented humanoid whose soul you caged.',
        'level': 6,
        'casting_time': '1 action',
        'range': '60 feet',
        'components': 'V, S, M',
        'duration': '8 hours',
        'school': 'Necromancy',


    },
    'sunbeam': {
        'description': 'A beam of brilliant light flashes out from your hand in a 5-foot-wide, 60-foot-long line. Each creature in the line must make a Constitution Saving Throw. On a failed save, a creature takes 6d8 radiant damage and is blinded until your next turn. On a successful save, it takes half as much damage and isn\'t blinded by this spell. Undead and oozes have disadvantage on this Saving Throw.\n\nYou can create a new line of radiance as your action on any turn until the spell ends.\n\nFor the duration, a mote of brilliant radiance shines in your hand. It sheds bright light in a 30-foot radius and dim light for an additional 30 feet. This light is sunlight.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 1 minute',
        'school': 'Evocation',
        'concentration': True,

    },
    'tenser\'s transformation': {
        'description': 'You endow yourself with endurance and martial prowess fueled by magic. Until the spell ends, you can\'t cast spells, and you gain the following benefits:\n\n•You gain 50 temporary hit points. If any of these remain when the spell ends, they are lost.\n•You have advantage on Attack Rolls that you make with simple and martial weapons.\n•When you hit a target with a Weapon Attack, that target takes an extra 2d12 force damage.\n•You have proficiency with all armor, shields, simple weapons, and martial weapons.\n•You have proficiency in Strength and Constitution Saving Throws.\n•You can attack twice, instead of once, when you take the attack action on your turn. You ignore this benefit if you already have a feature, like Extra Attack, that gives you extra attacks.\n\nImmediately after the spell ends, you must succeed on a DC 15 Constitution Saving Throw or suffer one level of exhaustion.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Self',
        'components': 'V, S',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Transmutation',
        'concentration': True,

    },
    'transport via plants': {
        'description': 'This spell creates a magical link between a large or larger inanimate plant within range and another plant, at any distance, on the same plane of existence. You must have seen or touched the destination plant at least once before. For the duration, any creature can step into the target plant and exit from the destination plant by using 5 feet of movement.',
        'level': 6,
        'casting_time': '1 action',
        'range': '10 feet',
        'components': 'V, S',
        'duration': '1 round',
        'school': 'Conjuration',


    },
    'true seeing': {
        'description': 'This spell gives the willing creature you touch the ability to see things as they actually are. For the duration, the creature has truesight, notices secret doors hidden by magic, and can see into the Ethereal Plane, all out to a range of 120 feet.',
        'level': 6,
        'casting_time': '1 action',
        'range': 'Touch',
        'components': 'V, S, M',
        'duration': '1 hour',
        'school': 'Divination',


    },
    'wall of ice': {
        'description': 'You create a wall of ice on a solid surface within range. You can form it into a hemispherical dome or a sphere with a radius of up to 10 feet, or you can shape a flat surface made up of ten 10-foot-square panels. Each panel must be contiguous with another panel. In any form, the wall is 1 foot thick and lasts for the duration.\n\nIf the wall cuts through a creature\'s space when it appears, the creature within its area is pushed to one side of the wall and must make a Dexterity Saving Throw. On a failed save, the creature takes 10d6 cold damage, or half as much damage on a successful save.\n\nThe wall is an object that can be damaged and thus breached. It has AC 12 and 30 hit points per 10-foot section, and it is vulnerable to fire damage. Reducing a 10-foot section of wall to 0 hit points destroys it and leaves behind a sheet of frigid air in the space the wall occupied. A creature moving through the sheet of frigid air for the first time on a turn must make a Constitution Saving Throw. That creature takes 5d6 cold damage on a failed save, or half as much damage on a successful one.\n\nWhen you cast this spell using a spell slot of 7th level or higher, the damage the wall deals when it appears increases by 2d6, and the damage from passing through the sheet of frigid air increases by 1d6, for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Evocation',
        'concentration': True,

    },
    'wall of thorns': {
        'description': 'You create a wall of tough, pliable, tangled brush bristling with needle-sharp thorns. The wall appears within range on a solid surface and lasts for the duration. You choose to make the wall up to 60 feet long, 10 feet high, and 5 feet thick or a circle that has a 20-foot diameter and is up to 20 feet high and 5 feet thick. The wall blocks line of sight.\n\nWhen the wall appears, each creature within its area must make a Dexterity Saving Throw. On a failed save, a creature takes 7d8 piercing damage, or half as much damage on a successful save.\n\nA creature can move through the wall, albeit slowly and painfully. For every 1 foot a creature moves through the wall, it must spend 4 feet of movement. Furthermore, the first time a creature enters the wall on a turn or ends its turn there, the creature must make a Dexterity Saving Throw. It takes 7d8 slashing damage on a failed save, or half as much damage on a successful one.\n\nWhen you cast this spell using a spell slot of 7th level or higher, both types of damage increase by 1d8 for each slot level above 6th.',
        'level': 6,
        'casting_time': '1 action',
        'range': '120 feet',
        'components': 'V, S, M',
        'duration': 'Concentration, up to 10 minutes',
        'school': 'Conjuration',
        'concentration': True,

    },
    'wind walk': {
        'description': 'You and up to ten willing creatures you can see within range assume a gaseous form for the duration, appearing as wisps of cloud. While in this cloud form, a creature has a flying speed of 300 feet and has resistance to damage from nonmagical weapons. The only actions a creature can take in this form are the dash action or to revert to its normal form. Reverting takes 1 minute, during which time a creature is incapacitated and can\'t move. Until the spell ends, a creature can revert to cloud form, which also requires the 1-minute transformation.\n\nIf a creature is in cloud form and flying when the effect ends, the creature descends 60 feet per round for 1 minute until it lands, which it does safely. If it can\'t land after 1 minute, the creature falls the remaining distance.',
        'level': 6,
        'casting_time': '1 minute',
        'range': '30 feet',
        'components': 'V, S, M',
        'duration': '8 hours',
        'school': 'Transmutation',


    },
    'word of recall': {
        'description': 'You and up to five willing creatures within 5 feet of you instantly teleport to a previously designated sanctuary. You and any creatures that teleport with you appear in the nearest unoccupied space to the spot you designated when you prepared your sanctuary (see below). If you cast this spell without first preparing a sanctuary, the spell has no effect.\n\nYou must designate a sanctuary by casting this spell within a location, such as a temple, dedicated to or strongly linked to your deity. If you attempt to cast the spell in this manner in an area that isn\'t dedicated to your deity, the spell has no effect.',
        'level': 6,
        'casting_time': '1 action',
        'range': '5 feet',
        'components': 'V',
        'duration': 'Instantaneous',
        'school': 'Conjuration',


    }
}
