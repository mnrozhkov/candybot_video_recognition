#!/usr/bin/env python3

import unittest
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(top)

from options import PauseDurationOptions

class TestSelectMethod(unittest.TestCase):

    def test(self):
        goto_next_intent_group = [
            ['intent1', 'intent2'],
            ['intent2', 'intent3'],
            ['intent3', 'intent4', 'intent5']
        ]

        pause_options = [
            {
                'duration': 10,
                'goto_next': goto_next_intent_group[0]
            },

            {
                'duration': 20,
                'goto_next': goto_next_intent_group[1]
            },

            {
                'duration': 30,
                'goto_next': goto_next_intent_group[2]
            }
        ]

        pause_duration_options = PauseDurationOptions(options_list=pause_options)

        pause_duration_options.select(0)
        self.assertEqual(pause_duration_options.goto_next, goto_next_intent_group[0])

        pause_duration_options.select(15)
        self.assertEqual(pause_duration_options.goto_next, goto_next_intent_group[1])

        pause_duration_options.select(28)
        self.assertEqual(pause_duration_options.goto_next, goto_next_intent_group[2])

        pause_duration_options.select(34)
        self.assertEqual(pause_duration_options.goto_next, goto_next_intent_group[2])


if __name__ == '__main__':
    unittest.main()
