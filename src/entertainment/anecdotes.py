#!/usr/bin/env python3
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()

import random

from utils import ErrorLogger

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
            ErrorLogger(__file__, e)

    def generate(self) -> str or None:
        '''
        Return random anecdote
        '''
        if len(self.anecdotes) > 0:
            return self.anecdotes[random.randint(0, len(self.anecdotes) - 1)]
        else:
            return None
