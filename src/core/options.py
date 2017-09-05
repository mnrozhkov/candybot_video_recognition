from utils import ErrorLogger
from typing import List

class Options:
    '''
    interface class for options
    '''

    def __init__(self, options_list):
        pass

    def select(self, parameter):
        pass


class PauseDurationOptions(Options):
    '''
    work with pause duration options in intent
    '''

    def __init__(self, options_list: List[dict]):
        '''
        Constructor
        Args:
            options_list: list of pause duration option dictionaries
        '''

        self.goto_next = None
        self.options_list = options_list

    def select(self, pause_parameter) -> None:
        '''
        select option depending pause_parameter value
        Args:
             pause_parameter: integer pause duration value in seconds
        '''
        try:
            min_option_value = 1000000
            for option in self.options_list:
                if option['duration'] > pause_parameter and option['duration'] < min_option_value:
                    self.goto_next = option['goto_next']
                    min_option_value = option['duration']
        except Exception as e:
            ErrorLogger(__file__, e)
