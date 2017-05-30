#!/usr/bin/env python3
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()

import random

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

class AnecdoteGenerator:

    def __init__(self, anecdotes_file=top + '/anecdotes.txt'):
        '''
        Constructor
        Args:
            anecdotes_file: file name that contains anecdotes by line
        '''

        self.anecdotes = list()

        try:
            top = Path(__file__).resolve().parents[0].as_posix()
            with open(anecdotes_file, 'r') as afile:
                for anecdote in afile:
                    self.anecdotes.append(anecdote)
        except Exception as e:
            logging.error(str(e))

    def generate(self) -> str or None:
        '''
        Return random anecdote
        '''
        if len(self.anecdotes) > 0:
            return self.anecdotes[random.randint(0, len(self.anecdotes) - 1)]
        else:
            return None
