'''Plays audio file'''

import pyglet


def play_mp3(mp3_file):
    '''Plays mp3_file

    Args:
        mp3_file: mp3 file name

    Returns:
        Nothing
    '''
    if not mp3_file is None:
        try:
            player = pyglet.media.Player()
            player.queue(pyglet.media.load(mp3_file))
            player.play()
            print('Если хотите закончить прослушивание, нажмите q')
            c = sys.stdin.read(1)
            if c == 'q':
                player.delete()
        except:
            print('File not found')
