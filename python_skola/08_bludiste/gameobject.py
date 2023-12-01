from vector2 import Vector2

class GameObject:
    '''
    Trida reprezentujici objekt ve hre

    @Author: cakoral
    @Date: 01.12.2023
    '''
    def __init__(self, position, symbol):
        '''
        Konstruktor tridy GameObject

        Args:
            position: pozice
            symbol: symbol reprezentujici objekt
        '''
        self.__position = position
        self.symbol = symbol

    @property
    def position(self):
        return self.__position
    
    def move(self, direction):
        '''
        Posune objekt

        Args:
            direction: smer posunu
        '''
        self.__position = self.__position + direction

    def draw(self, gui):
        '''
        Zakresli objekt do GUI

        Args:
            gui: GUI
        '''
        gui.draw(self.__position.x, self.__position.y, self.symbol)