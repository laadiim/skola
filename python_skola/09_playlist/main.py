from playlist import Playlist
from track import Track
import sys

def inputTrack():
    '''
    Zada skladbu

    Retruns:
        Track
    '''
    title = input('Zadej jmeno skladby: ')
    if title == '':
        return None
    length = input('Zadej delku skladby v sekundach: ')
    rating = input('Zadej rating skladby (0-5): ')
    if rating == '' or length == '' or title == '':
        return None
    if (not (0 <= float(rating) <= 5)) or (int(length) < 0):
        return None
    return Track(title, int(length), float(rating))

def inputPlaylist():
    '''
    Zada playlist

    Returns:
        Playlist
    '''
    tracks = []
    while True:
        track = inputTrack()
        if track == None:
            return Playlist(tracks)
        tracks.append(track)

def preparePlaylist(playlist, minLength):
    '''
    Sesklada novy playlist o delce minLength

    Args:
        playlist: puvodni playlist
        minLength: minimalni delka playlistu

    Returns:
        Playlist
    '''
    playlist.sortByRating()
    new = Playlist(playlist.selectTotalLength(minLength).tracks)
    new.shuffle()
    return new

if __name__ == '__main__':
    playlist = inputPlaylist()
    minLength = int(sys.argv[1])
    print(preparePlaylist(playlist, minLength))
    if playlist.totalLength < minLength:
        print('POZOR, JE KRATKY')