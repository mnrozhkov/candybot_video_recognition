'''Allows to determine event name and event parameters by
text content and to make event'''

from network.encyclopedia import Encyclopedia
from audio.text_to_speech import TextToSpeech
from audio.audio_playback import Player


def say_hello(cap=None):
    '''Says hello
    Args:
        cap=None: not use, just as cap
    '''
    
    player = Player(['Привет.mp3'])
    player.play()


def say_article(theme=None):
    '''Plays audio with information found in Wikipedia
    Args:
        theme: info theme
    '''

    if theme is None:
        theme = 'википедия'

    encyclopedia = Encyclopedia(theme, lang='ru')
    article = encyclopedia.get_summary()
    tts = TextToSpeech(article)
    speech = tts.translate()
    player = Player([speech]);
    player.play()

    
def say_unrecognized(cap=None):
     '''Says 'Repeate' in language by default
    Args:
        cap=None: not use, just as cap
    '''
    
    player = Player(['unrecognized.mp3'])
    player.play()


#event name associates whith functions    
switch_event = {'say_hello': say_hello,
                'say_article': say_article,
                'unrecognized': say_unrecognized}


    
class EventRecognizer:
    '''Recognizes event name and event parameters by text content'''
    
    def __init__(self, text):
        '''Constructor
        Args:
            text: recognizing text
        '''
        
        if not text is None:
            self.text = text.lower()
        else:
            self.text = None


    def recognize_event(self):
        '''Recognizes event name and event parameters by text content'''
        
        lexems = self.text.split(' ')
        if self.text is None:
            return 'unrecognized', None
        if 'расскажи' in lexems:
            lexems.remove('расскажи')
            return 'say_article', ' '.join(lexems)
        else:
            if 'привет' in lexems and not ('расскажи' in lexems):
                lexems.remove('привет')
                return 'say_hello', None
            else:
                return 'say_article', self.text


class Event:
    '''Allows to create event with parameters and to make it'''
    
    def __init__(self, name, params=None):
        '''Constructor
        Args:
            name: event name
            params: event parameters
        '''
        self.name = name
        self.params = params

    def make(self):
        '''Makes event
        Raises:
            UnknownEventError: an error occurred trying to make unknown event

        '''
        try:
            switch_event[self.name](self.params)
        except KeyError:
            raise UnknownEventError()
        

class UnknownEventError(Exception):

    def __init__(self, message='Unknown event!'):
        self.message = message

