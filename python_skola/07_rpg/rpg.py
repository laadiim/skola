from character import Character
from weapon import Weapon

class RPG:
    
    characters = []
    weapons = []

    def __init__(self):
        pass

    def input_character(self):
        char_name = input('Zadej jmeno postavy: ')
        char_strength = int(input('Zadej silu: '))
        char_agility = int(input('Zadej mrstnost: '))
        char_health = int(input('Zivoty postavy: '))
        char = Character(char_name, char_strength, char_agility, char_health)
        self.characters.append(char)
        return char

    def input_weapon(self):
        wep_name = input('Zadej jmeno zbrane: ')
        if wep_name == '':
            print('Nope')
            return
        wep_attack = int(input('Zadej utok: '))
        wep_defense = int(input('Zadej obranu: '))
        wep = Weapon(wep_name, wep_attack, wep_defense)
        self.weapons.append(wep)
        return wep
    
    def equip_character(self, character, left, right):
        character.take_weapon(left, 0)
        character.take_weapon(right, 1)

    def fight(self, character1, character2):
        while True:
            tmp = (character1.vitality, character2.vitality)
            character2.defend(character1.attack())
            character1.defend(character2.attack())
            if character1.vitality == tmp[0] and character2.vitality == tmp[1]:
                return 'draw'
            if not character1.is_alive():
                if character2.is_alive():
                    return character2
                else:
                    return 'draw'
            if not character2.is_alive():
                if character1.is_alive():
                    return character1
                else:
                    return 'draw'
            

        
rpg = RPG()
rpg.fight(Character('Golias', 3, 0, 10), Character('David', 1, 1, 20))