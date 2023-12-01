from weapon import Weapon

class Character:
    '''
    Character reprezentuje postavu v RPG hre

    @Author: cakoral
    @Date: 27.11.2023
    '''
    HAND_LEFT = 0
    '''
    Konstanta o hodnote 0
    '''
    HAND_RIGHT = 1
    '''
    Konstanta o hodnote 1
    '''
    
    def __init__(self, name='', strength=0, agility=0, vitality=0):
        '''
        Konstruktor postavy

        Args:
            name: jmeno postavy
            strength: sila postavy
            agility: hbitost postavy
            vitality: zivoty postavy
        '''
        self.name = name
        self.strength = strength
        self.agility = agility
        self._vitality = vitality
        self.weapons = [None, None]
        '''
        Seznam na ulozeni zbrani
        '''

    @property
    def vitality(self):
        '''
        Vraci zivoty postavy

        Returns:
            zivoty
    '''
        return self._vitality
    
    @vitality.setter
    def vitality(self, new_vitality):
        '''
        Setter pro vitality

        Args:
            new_vitality: nove zivoty postavy
        '''
        self._vitality = new_vitality

    def take_weapon(self, weapon, hand):
        '''
        Da postave zbran

        Args:
            weapon: zbran
            hand: ruka (character.HAND_LEFT nebo character.HAND_RIGHT)

        Returns:
            True (prazdna ruka)
            False (plna ruka)
        '''
        if self.weapons[hand] == None:
            self.weapons[hand] = weapon
            print(self.weapons[hand])
            return True
        else:
            return False
        

    def attack(self):
        '''
        Vrati celkovy utok postavy

        Returns:
            utok
        '''
        damage = self.strength
        for hand in self.weapons:
            if hand != None:
                damage += hand.attack
        return damage
    
    def get_defense(self):
        '''
        Vrati celkovou obrannou silu postavy

        Returns:
            obrana
        '''
        defense = self.agility
        for hand in self.weapons:
            if hand != None:
                defense += hand.defense
        return defense
    
    def defend(self, attack):
        '''
        Vrati ubrane zivoty po utoku

        Args:
            attack: prichozi utok

        Returns:
            ubrane zivoty
        '''
        dmg = attack - self.get_defense()
        if dmg < 0:
            return 0
        else:
            self._vitality -= dmg
            return dmg
        
    def is_alive(self):
        '''
        Zjisti jestli je postava nazivu

        Returns:
            True (nazivu)
            False (neni na zivu)
        '''
        if self._vitality > 0:
            return True
        else:
            return False
    
    def __str__(self):
        '''
        String postavy
        '''
        return f'{self.name} [{self._vitality}] ({self.attack()}/{self.get_defense()})'

if __name__ == '__main__':
    postava = Character('postava', 12, 45, 78)
    weapon1 = Weapon('l', 23, 56)
    weapon2 = Weapon('r', 34, 67)
    print(postava.take_weapon(weapon1, postava.HAND_LEFT))
    print(postava.take_weapon(weapon1, postava.HAND_LEFT))
    print(postava.take_weapon(weapon2, postava.HAND_RIGHT))
    print(postava.take_weapon(weapon1, postava.HAND_RIGHT))
    print(postava.__str__())