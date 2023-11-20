class Weapon:    
    
    def __init__(self, name = '', attack = 0, defense = 0):
        self.name = name
        self._attack = attack
        self._defense = defense

    def __str__(self):
        return (f'{self.name} [{self._attack}/{self._defense}]')
    
    @property
    def attack(self):
        return self._attack
    
    @attack.setter
    def attack(self, new_attack):
        self._attack = new_attack
    
    
    @property
    def defense(self):
        return self._defense
    
    @defense.setter
    def defense(self, new_defense):
        self._defense = new_defense