from character import Character
from weapon import Weapon

class RPG:
    
    characters = []
    weapons = []

    def __init__(self):
        pass

    def input_character(self):
        char_name = input('Zadej jmeno postavy: ')
        char_health = int(input('Zivoty postavy: '))
        char_strength = int(input('Zadej silu: '))
        char_agility = int(input('Zadej mrstnost: '))
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