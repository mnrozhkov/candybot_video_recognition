#!/usr/bin/env python3

import rospy
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(top)

from anecdotes import AnecdoteGenerator

import unittest

class TestAnecdoteGeneration(unittest.TestCase):

    def test_default_anecdote_file(self):
        angen = AnecdoteGenerator()
        anecdote = angen.generate()

        self.assertEqual(type(anecdote), str)
        self.assertGreater(len(anecdote), 0)

    def test_nonexistent_anecdote_file(self):
        angen = AnecdoteGenerator('nonexistent_file')
        anecdote = angen.generate()

        self.assertEqual(anecdote, None)

if __name__ == '__main__':
    rospy.init_node('test_anecdotes')
    unittest.main()
