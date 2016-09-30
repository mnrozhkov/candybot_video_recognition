#!/usr/bin/env python3

'''Allows to determine event name and event parameters by
text content and to make event'''

import subprocess

from network.encyclopedia import Encyclopedia
import subprocess

import argparse


class Sayer:
    '''Says text'''

    def __init__(self, text=None):
        '''Constructor
        Args:
            text: text to say
        '''
        self.text = text

    def say(self):
        if not self.text is None:
            echo_proc = subprocess.Popen(['echo', self.text],
                                         stdout=subprocess.PIPE)
            rhvoice_proc = subprocess.call(['spd-say', '-w', '-o', 'rhvoice',
                                            '-l', 'ru', '-e', '-t', 'male1'],
                                           stdin=echo_proc.stdout)


def say_hello(cap=None):
    '''Says hello
    Args:
        cap=None: not use, just as cap
    '''
    sayer = Sayer('Привет, как дела, дорогОй друг?')
    sayer.say()
    


def say_article(theme=None):
    '''Plays audio with information found in Wikipedia
    Args:
        theme: info theme
    '''

    if theme is None:
        theme = 'википедия'

    encyclopedia = Encyclopedia(theme, lang='ru')
    article = encyclopedia.get_summary()
    
    sayer = Sayer(article)
    sayer.say()
    
def say_unrecognized(cap=None):
    '''Says 'Repeate' in language by default
    Args:
        cap=None: not use, just as cap
    '''
    sayer = Sayer('Повторите')
    sayer.say()        
   


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
        print(text)
        if not text is None:
            self.text = text.lower()
        else:
            self.text = None


    def recognize_event(self):
        '''Recognizes event name and event parameters by text content'''
        if self.text is None:
            return 'unrecognized', None
        lexems = self.text.split(' ')
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


def main(text=None):
    event_recognizer = EventRecognizer(text)
    event_type, params = event_recognizer.recognize_event()

    event = Event(event_type, params)
    event.make()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Gets text and makes event')
    parser.add_argument('text', default=None)
    args = parser.parse_args()

    main(args.text)
