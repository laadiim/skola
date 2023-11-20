from weapon import Weapon

class Character:
    
    HAND_LEFT = 0
    HAND_RIGHT = 1

    weapons = [None, None]
    
    def __init__(self, name='', strength=0, agility=0, vitality=0):
        self.name = name
        self.strength = strength
        self.agility = agility
        self._vitality = vitality

    @property
    def vitality(self):
        return self._vitality
    
    @vitality.setter
    def vitality(self, new_vitality):
        self._vitality = new_vitality

    def take_weapon(self, weapon, hand):
        if self.weapons[hand] == None:
            self.weapons[hand] = weapon
            return True
        else:
            return False
        

    def attack(self):
        damage = self.strength
        for hand in self.weapons:
            if hand != None:
                damage += hand.attack
        return damage
    
    def get_defense(self):
        defense = self.agility
        for hand in self.weapons:
            if hand != None:
                defense += hand.defense
        return defense
    
    def defend(self, attack):
        dmg = attack - self.get_defense()
        if dmg < 0:
            return 0
        else:
            self._vitality -= dmg
            return dmg
        
    def is_alive(self):
        if self._vitality > 0:
            return True
        else:
            return False
    
    def __str__(self):
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