#!/usr/bin/env python3

import unittest
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(top)

from intents import Intent
from options import PauseDurationOptions

class TestRunMethod(unittest.TestCase):

    def test_with_options(self):

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
        sale_status = {
            'status': 'success',
            'description': 'product sold'
        }

        pause = 25

        intent = Intent(name="intent_",
                        listen_user=True,
                        is_start=True,
                        is_last=True,
                        pause_duration_options=pause_duration_options,
                        sale_status=sale_status
                        )

        intent.run(pause=pause)

        self.assertEqual(intent.name, "intent_")
        self.assertTrue(intent.listen_user)
        self.assertTrue(intent.is_start)
        self.assertTrue(intent.is_last)
        self.assertIn(intent.next_intent_name, goto_next_intent_group[2])
        self.assertIsInstance(sale_status, dict)


    def test_without_options(self):

        sale_status = {
            'status': 'success',
            'description': 'product sold'
        }

        next_intent_name_list = ['i1', 'i2', 'i3']

        intent = Intent(name="intent_",
                        listen_user=True,
                        is_start=True,
                        is_last=True,
                        next_intent_name=next_intent_name_list,
                        sale_status=sale_status
                        )

        intent.run()

        self.assertEqual(intent.name, "intent_")
        self.assertTrue(intent.listen_user)
        self.assertTrue(intent.is_start)
        self.assertTrue(intent.is_last)
        self.assertIn(intent.next_intent_name, next_intent_name_list)
        self.assertIsInstance(sale_status, dict)


if __name__ == '__main__':
    unittest.main()
