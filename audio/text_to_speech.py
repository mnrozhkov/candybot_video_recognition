'''Allows to translate text to speech'''

from gtts import gTTS
import time

class TextToSpeech:
    '''Allows to translate text to speech'''
    
    def __init__(self, text, lang='ru', speech_file=None):
        '''Constructor
        Args:
            text: translating text
            lang: text language
            speech_file: file name to save speech
        '''
        
        self.text = text
        self.lang = lang
        self.speech_file = speech_file

    def translate(self):
        '''Translates text to speech'''
        
        tts = gTTS(self.text, lang=self.lang)
        if self.speech_file is None:
            self.speech_file = str(time.time()) + '.mp3'
        tts.save(self.speech_file)
        return self.speech_file
