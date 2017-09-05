from typing import List
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()
import sys
sys.path.append(top)

from options import PauseDurationOptions
import random

class Intent:
    '''
    implement scheme unit
    contain attributes and option using for execution and transition
    '''

    def __init__(self, name: str, listen_user: bool=True,  is_start: bool=False, \
                is_last: bool or None=False, pause_duration_options: PauseDurationOptions or None = None, \
                next_intent_name: List[str] or None = None, \
                initiate_intent_with_name: List[str] or None = None, \
                workflow_status: dict or None = None):

        '''
        Constructor
        Args:
            name: intent name
            soft_config: software configuration
            listen_user: listen to user flag
            is_start: start intent flag
            is_last: intent is last flag
            pause_duration_options: pause duration options object
            next_intent_name: next intent name
            initiate_intent_with_name: initiate intent with the name explicitly
            workflow_status: sale status
        '''

        self.name = name
        self.listen_user = listen_user
        self.is_start = is_start
        self.is_last = is_last

        #select next intent name
        self.next_intent_name = None
        if isinstance(next_intent_name, List[str]):
            self.next_intent_name = next_intent_name[random.randint(0, len(next_intent_name) -1 )]

        self.pause_duration_options = pause_duration_options

        #select initiate intent name
        self.initiate_intent_with_name = None
        if isinstance(initiate_intent_with_name, List[str]):
            self.initiate_intent_with_name = initiate_intent_with_name[random.randint(0, len(initiate_intent_with_name) -1 )]

        self.workflow_status = workflow_status
        self.say_to_user = str()

    def run(self, pause: int=0, say_to_user: str=str(), save_intent: bool=False) -> None:
        '''
        run intent execution
        Args:
        '''
        self.say_to_user = say_to_user
        if isinstance(self.pause_duration_options, PauseDurationOptions): #if intent has options:
            self.pause_duration_options.select(pause)
            goto_next = self.pause_duration_options.goto_next
            if save_intent is True:
                self.next_intent_name = self.name
            else:
                if isinstance(goto_next, list):
                    self.next_intent_name = goto_next[random.randint(0, len(goto_next) - 1)]


    def _start(self):
        pass

    def _fail(self):
        pass

    def _complete(self):
        pass
