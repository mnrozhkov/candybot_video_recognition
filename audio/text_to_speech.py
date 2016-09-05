'''Allows translate text into speech'''

from gtts import gTTS
import time


def tts(text, lang='ru'):
    '''Translates text into speech

    Args:
        text: translating text
        lang: translating language

    Returns:
        mp3 file name
    '''

    if text is None:
        return None
    try:
        gtts = gTTS(text, lang=lang)
        mp3_file_name = str(time.time()) + '.mp3'
        gtts.save(mp3_file_name)
        return mp3_file_name
    except:
        print('Connection error')
        return None
