class Track:
    '''
    Trida reprezentujici skladbu

    @Author: cakoral
    @Date: 04.12.2023
    '''
    def __init__(self, title, length, rating):
        '''
        Konstruktor tridy Track

        Args:
            title: nazev skladby
            length: delka skladby
            rating: hodnoceni skladby
        '''
        self.__title = title
        self.__length = length
        self.__rating = rating

    @property
    def title(self):
        return self.__title
    
    @property
    def length(self):
        return self.__length
    
    @property
    def rating(self):
        return self.__rating
    
    def __str__(self):
        '''
        Vraci string pro objekt
        '''
        rating = int(self.__rating) * '*'
        if self.__rating-int(self.__rating) >= 0.75:
            rating += '*'
        elif self.__rating-int(self.__rating) >= 0.25:
            rating += '.'

        if self.__length%60 < 10:
            sec = '0' + str(self.__length%60)
        else:
            sec = str(self.__length%60)
        return f'{self.__title} [{self.__length//60}:{sec}] ({rating})'