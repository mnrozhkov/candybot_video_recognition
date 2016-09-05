'''Searches inforamtion in Wikipedia'''

import wikipedia


def get_wiki_page(text,lang='ru'):
    '''Searches text into Wikipedia

    Args:
        text: searching text
        lang: Wiki languge

    Returns:
        text from Wikipedia
    '''
    wikipedia.set_lang(lang)
    try:
        return wikipedia.summary(text)
    except:
        print('Connection error')
        return None
