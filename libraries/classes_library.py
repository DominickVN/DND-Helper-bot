# class Wizard:
#     def __init__(self):
#         self.name = 'Wizard'
#         self.hit_die = 'd6'
#         self.primary_ability = 'Intelligence'
#         self.saving_throws = ['Intelligence', 'Wisdom']
#         self.proficiencies = {
#             'armor': [],
#             'weapons': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light crossbows'],
#             'tools': [],
#         }
#         self.equipment = {
#             'required': [
#                 'A spellbook',
#                 'A quarterstaff',
#                 'A component pouch or an arcane focus',
#                 'A scholar\'s pack or an explorer\'s pack',
#             ],
#             'choices': [
#                 'A component pouch',
#                 'An arcane focus',
#             ],
#         }
#         self.features = {
#             1: ['Spellcasting', 'Arcane Recovery'],
#             2: ['Arcane Tradition'],
#             3: ['Ability Score Improvement'],
#             # Add features for other levels
#         }
#         self.abilities = {
#             1: {
#                 'Spellcasting': 'You have learned to cast spells as a wizard, harnessing the magical energies of the arcane. See the Spellcasting section for the wizard class in the Player\'s Handbook for the rules on casting spells.',
#                 'Arcane Recovery': 'You have learned to regain some of your magical energy by studying your spellbook. Once per day, during a short rest, you can recover a number of expended spell slots by spending time studying your spellbook. The total levels of the recovered spell slots can be no greater than half your wizard level (rounded up).',
#             },
#             2: {
#                 'Arcane Tradition': 'At 2nd level, you choose an arcane tradition that shapes your magical abilities and defines your role as a wizard. Choose one of the following traditions: [Insert list of available arcane traditions and their descriptions].',
#             },
#             3: {
#                 'Ability Score Improvement': 'When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can\'t increase an ability score above 20 using this feature.',
#             },
#             # Add abilities for other levels
#         }

#     def get_description(self):
#         description = f"Class: {self.name}\n"
#         description += f"Hit Die: {self.hit_die}\n"
#         description += f"Primary Ability: {self.primary_ability}\n"
#         description += f"Saving Throws: {', '.join(self.saving_throws)}\n"
#         description += "\nProficiencies:\n"
#         description += f"Armor: {', '.join(self.proficiencies['armor'])}\n"
#         description += f"Weapons: {', '.join(self.proficiencies['weapons'])}\n"
#         description += f"Tools: {', '.join(self.proficiencies['tools'])}\n"
#         description += "\nStarting Equipment:\n"
#         description += "Required:\n"
#         description += '\n'.join(f"- {item}" for item in self.equipment['required']) + '\n'
#         description += "Choose one:\n"
#         description += '\n'.join(f"- {item}" for item in self.equipment['choices']) + '\n'
#         description += "\nFeatures:\n"
#         for level, features in self.features.items():
#             description += f"Level {level}:\n"
#             description += '\n'.join(f"- {feature}" for feature in features) + '\n'
#             if level in self.abilities:
#                 description += '\n'.join(f"  {ability}: {description}" for ability, description in self.abilities[level].items()) + '\n'
#         return description
