'''Allows to play audio files'''

import pyglet
import time

class Player:
    '''Allows to play audio files'''

    def __init__(self, audio_files_list=None):
        '''Constructor
        Args:
            audio_files_list: list of audio files names
        Raises:
            TypeError: an error occurred if audio_files_list is not list
        '''
        
        self.player = pyglet.media.Player()
        if not audio_files_list is None:
            if isinstance(audio_files_list, list):
                for audio in audio_files_list: #sets all files in queue
                    self.player.queue(pyglet.media.load(audio))
            else:
                raise TypeError

    def add_audio(self, audio):
        '''Adds new audio in queue
        Args:
            audio: audio file name
        '''
        
        self.player.queue(pyglet.media.load(audio))
    
    def play(self):
        '''Plays audio'''
        
        self.player.play()              #starts play audio 
        silence_time_count = 0
        while True:                     #and waits until audio ends
            if self.player._get_time() == 0:
                silence_time_count += 1
            else:
                silence_time_count = 0
            if silence_time_count >= 100000:
                break
        
    def pause(self):
        '''Pauses audio'''
        self.player.pause()

    def stop(self):
        '''Stops audio'''
        self.player.delete()

    def next(self):
        '''Starts play next audio'''
        self.player.next_source()

    
