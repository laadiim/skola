from character import Character
from weapon import Weapon

class RPG:
    '''
    RPG reprezentuje rpg hru

    @Author: cakoral
    @Date: 27.11.2023
    '''
    def __init__(self):
        '''
        Konstruktor RPG
        '''
        pass

    def input_character(self):
        '''
        Zada udaje o postave

        Returns:
            postava
        '''
        char_name = input('Zadej jmeno postavy: ')
        char_strength = int(input('Zadej silu: '))
        char_agility = int(input('Zadej mrstnost: '))
        char_health = int(input('Zivoty postavy: '))
        char = Character(char_name, char_strength, char_agility, char_health)
        return char

    def input_weapon(self):
        '''
        Zada udaje o zbrani

        Returns:
            zbran
        '''
        wep_name = input('Zadej jmeno zbrane: ')
        if wep_name == '':
            print('Nope')
            return
        wep_attack = int(input('Zadej utok: '))
        wep_defense = int(input('Zadej obranu: '))
        wep = Weapon(wep_name, wep_attack, wep_defense)
        return wep
    
    def equip_character(self, character, left, right):
        '''
        Da postave zbrane

        Args:
            character: postava
            left: leva zbran
            right: prava zbran
        '''
        character.take_weapon(left, character.HAND_LEFT)
        character.take_weapon(right, character.HAND_RIGHT)

    def fight(self, character1, character2):
        '''
        Spusti souboj

        Args:
            character1: prvni postava
            character2: druha postava

        Return:
            vitez nebo remiza
        '''
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
        '''
        Spusti hru
        '''
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
