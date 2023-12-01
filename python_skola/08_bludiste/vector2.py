
class Vector2:
    '''
    Trida reprezentujici 2D souradnice

    @Author: cakoral
    @Date: 01.12.2023
    '''
    def __init__(self, x, y):
        '''
        Konstruktor tridy Vector2

        Args:
            x: souradnice x
            y: souradnice y
        '''
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __add__(self, other):
        '''
        Secte souradnice

        Args:
            other: druhy Vector2

        Returns:
            soucet vektoru
        '''
        return Vector2(self.__x + other.__x, self.__y + other.__y)
    
    def __eq__(self, other):
        '''
        Porovna souradnice

        Args:
            other: druhy Vector2

        Returns:
            bool - je/neni
        '''
        if self.__x == other.__x and self.__y == other.__y:
            return True
        return False
    
    def __str__(self):
        '''
        String tridy
        '''
        return f'{self.__x}; {self.__y}'