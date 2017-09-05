import unittest
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(top)

from dialog_manager import DialogManager


class TestMakeNextIntentMethod(unittest.TestCase):

    def setUp(self):
        self.test_scheme_path = Path(__file__).resolve().parents[0].as_posix() + '/bot_teacher.scs'
        self.apiai_bot_client_key = 'cd348bcc093b452cb11159f00c23d482'
        self.d_manager = DialogManager(scheme_file=self.test_scheme_path, apiai_bot_client_key=self.apiai_bot_client_key)

    def test_intent_welcome(self):
        self.d_manager.make_next_intent(speech_text='Здравствуйте')
        print('bot answer = {0}'.format(self.d_manager.say_to_user))
        self.assertEqual(self.d_manager.required_intent.name, '2-Approach')

    def test_intent_approach_p10(self):
        self.d_manager.make_next_intent(speech_text='Здравствуйте')
        print('bot answer = {0}'.format(self.d_manager.say_to_user))
        self.assertEqual(self.d_manager.required_intent.name, '2-Approach')

        self.d_manager.make_next_intent(speech_text='вижу вас заинтересовала эта модель', \
                                        pause_duration=10)
        print(self.d_manager.say_to_user)
        self.assertEqual(self.d_manager.required_intent.name, '2.1-Approach-decision-leave')
        self.assertFalse(self.d_manager.required_intent.listen_user)
        self.assertTrue(self.d_manager.required_intent.is_last)

        self.d_manager.make_next_intent()

        self.assertTrue(self.d_manager.scenario_complete)




if __name__ == '__main__':
    unittest.main()
