
class World:
    '''
    Trida reprezentujici herni svet

    @Author: cakoral
    @Date: 01.12.2023
    '''
    def __init__(self, data, symbols):
        '''
        Konstruktor tridy World

        Args:
            data: 2D pole s hranicemi
            symbols: pole se znaky
        '''
        self.__data = data
        self.__symbols = symbols
        self.__width = len(data[0])
        self.__height = len(data)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def data(self):
        return self.__data
    
    @property
    def symbols(self):
        return self.__symbols
    
    def is_empty(self, position):
        '''
        Zkontroluje jestli je pozice prazdna

        Args:
            position: pozice

        Returns:
            bool
        '''
        val = self.__data[position.y][position.x]
        if  val == 0:
            return True
        return False
    
    def draw(self, gui):
        '''
        Zakresli svet do GUI

        Args:
            gui: GUI
        '''
        for y in range(self.height):
            for x in range(self.width):
                gui.draw(x, y, self.symbols[self.data[y][x]])

    def val(self, pos):
        '''
        Vrati hodnotu v data na pozici

        Args:
            pos: pozice

        Returns:
            value
        '''
        return self.__data[pos.y][pos.x]