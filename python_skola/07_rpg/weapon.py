class Weapon:    
    
    def __init__(self, name = '', attack = 0, defense = 0):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return (f'{self.name} [{self.attack}/{self.defense}]')
    
    @property
    def attack(self):
        return self.attack
    
    @property
    def defense(self):
        return self.defense