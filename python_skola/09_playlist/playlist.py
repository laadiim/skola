from track import Track
import copy
import random

class Playlist:
    '''
    Trida reprezentujici Playlist

    @Author: cakoral
    @Date: 04.12.2023
    '''
    def __init__(self, tracks):
        '''
        Konstruktor tridy Playlist

        Args:
            tracks: seznam skladeb
        '''
        self.__tracks = copy.copy(tracks)
        ln = 0
        for track in tracks:
            ln += track.length
        self.__totalLength = ln

    @property
    def tracks(self):
        return self.__tracks
    
    @property
    def totalLength(self):
        return self.__totalLength
    
    def sortByRating(self):
        '''
        Seradi playlist podle hodnoceni
        '''
        swapped = False
        for track in self.__tracks:
            print(track.rating)
        print('')
        for i in range(len(self.__tracks)-1):
            for j in range(len(self.__tracks)-i-1):
                if self.__tracks[j].rating < self.__tracks[j + 1].rating:
                    swapped = True
                    self.__tracks[j], self.__tracks[j + 1] = self.__tracks[j + 1], self.__tracks[j]

            if not swapped:
                return
        for track in self.__tracks:
            print(track.rating)

    def __str__(self):
        '''
        Vrati string tridy
        '''
        s = ''
        for track in self.__tracks:
            s += str(track) + '\n'

        if self.__totalLength%60 < 10:
            sec = '0' + str(self.__totalLength%60)
        else:
            sec = str(self.__totalLength%60)
        return f'{s}[{self.__totalLength//60}:{sec}]'

    def shuffle(self):
        '''
        Prohazi nahodne skladby v playlistu
        '''
        for i in range(len(self.__tracks)):
            index = random.randint(0, len(self.__tracks)-1)
            self.__tracks[i], self.__tracks[index] = self.__tracks[index], self.__tracks[i]

    def selectTotalLength(self, minLength):
        '''
        Vytvori novy playlist alespon o delce minLength

        Args:
            minLength: minimalni delka

        Returns:
            playlist
        '''
        if minLength >= self.__totalLength:
            return Playlist(self.__tracks)
        tracks = []
        ln = 0
        for i in range(len(self.__tracks)):
            tracks.append(self.__tracks[i])
            ln += tracks[-1].length
            if ln >= minLength:
                return Playlist(tracks)
