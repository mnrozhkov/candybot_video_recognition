#!/usr/bin/env python3
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()

import random


def geneate_anecdote(anecdotes_file=top + '/anecdotes.txt'):
    with open(anecdotes_file, 'r') as afile:
        anecdotes = list()
        for anecdote in afile:
            anecdotes.append(anecdote)
        return anecdotes[random.randint(0, len(anecdotes) - 1)]
