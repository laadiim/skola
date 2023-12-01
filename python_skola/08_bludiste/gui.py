from vector2 import Vector2

class Gui:
    '''
    Trida reprezentujici GUI

    @Author: cakoral
    @Date: 01.12.2023
    '''
    
    controls = {
        'w': (0, -1),
        's': (0, 1),
        'd': (1, 0),
        'a': (-1, 0),
        '8': (0, -1),
        '2': (0, 1),
        '6': (1, 0),
        '4': (-1, 0)
    }
    
    def __init__(self, width, height):
        '''
        Konstruktor tridy Gui

        Args:
            width: sirka
            height: vyska
        '''
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
    
    def draw(self, x, y, symbol):
        '''
        Zapise symbol do GUI

        Args:
            x: souradnice x
            y: souradnice y
        '''
        self.canvas[y][x] = symbol

    def show(self):
        '''
        Vytiskne GUI
        '''
        for row in self.canvas:
            print(''.join(row))
                
    def clear(self):
        '''
        Vycisti GUI
        '''
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def input_direction(self):
        '''
        Zadani pohybu

        Returns:
            souradnice pohybu
        '''
        dir = input('Zadej smer: ').lower()
        if dir in self.controls.keys():
            return Vector2(self.controls[dir][0], self.controls[dir][1])
        return Vector2(0, 0)