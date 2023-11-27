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
        character.take_weapon(left, character.HAND_LEFT)
        character.take_weapon(right, character.HAND_RIGHT)

    def fight(self, character1, character2):
        while True:
            tmp = (character1.vitality, character2.vitality)
            character2.defend(character1.attack())
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
            character1.defend(character2.attack())
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
            if character1.vitality == tmp[0] and character2.vitality == tmp[1]:
                return 'draw'
            

    def run(self):
        char1 = self.input_character()
        wep1l = self.input_weapon()
        wep1r = self.input_weapon()
        self.equip_character(char1, wep1l, wep1r)
        char2 = self.input_character()
        wep2l = self.input_weapon()
        wep2r = self.input_weapon()
        self.equip_character(char2, wep2l, wep2r)
        print(f'Vitez: {self.fight(char1, char2)}')

            

        
if __name__ == "__main__":
    rpg = RPG()
    rpg.run()
