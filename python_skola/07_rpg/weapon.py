class Weapon:    
    '''
    Weapon reprezentuje zbran v RPG hre

    @Author: cakoral
    @Date: 27.11.2023
    '''

    def __init__(self, name = '', attack = 0, defense = 0):
        '''
        Konstruktor tridy Weapon

        Args:
            name: jmeno zbrane
            attack: utok zbrane
            defense: obrana zbrane
        '''
        self.name = name
        self._attack = attack
        self._defense = defense

    def __str__(self):
        '''
        String Weapon
        '''
        return (f'{self.name} [{self._attack}/{self._defense}]')
    
    @property
    def attack(self):
        '''
        Vrati utok zbrane
        '''
        return self._attack
    
    @property
    def defense(self):
        '''
        Vrati obranu zbrane
        '''
        return self._defense
    