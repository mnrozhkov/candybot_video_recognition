#!/usr/bin/env python3
'''Allows to parse anekdots'''

import urllib.request
import random


class Anekdot:
    '''Parses anekdots'''
    
    def __init__(self):
        '''Initialization method'''
        
        self.site = 'http://5ft.ru/'
        self.new_anekdots = []
        self.__parse__()
        
    def __parse__(self):
        '''Parses anekdot site'''
        
        try:
            response = urllib.request.urlopen(self.site)
        
            
            html = response.read().decode('utf-8', 'ignore')
            find_tag = "span class='content'>"
            find_tag_len = len(find_tag)
            
            start = 0
            while not start == -1:
                start = html.find(find_tag, start)
                if not start  == -1:
                    end = html.find("/span>",start)
                    anekdot_line = html[start + find_tag_len:end]
                    self.new_anekdots.append('\n'.join(anekdot_line.split('<br>')))
                    start = end
        except:
            self.new_anekdots = None

    def random_anekdot(self):
        '''Returns random anekdot or None in case of an error
        Returns:
            random anekdot or None
        '''
        
        if not self.new_anekdots is None:
            index = len(self.new_anekdots)
            if index > 0:
                return self.new_anekdots[random.randint(0, index)]
            else:
                return None
        else:
            return None
