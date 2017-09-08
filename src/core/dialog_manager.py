
from typing import List
import time

import os
import json
import random

from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()
import sys
sys.path.append(top)

from options import PauseDurationOptions
from intents import Intent

src_path = Path(__file__).resolve().parents[2].as_posix()
sys.path.append(src_path)

from apiai_service.bot_client import APIAIBot
from utils import ErrorLogger


class DialogManager:
    '''
    dialog manager
    execute intent sequence
    '''

    def __init__(self, scheme_file: str or None=None, apiai_bot_client_key: str=str()):
        '''
        Constructor
        Args:
            scheme_file: scenario filename,
            apiai_bot_client_key: client key for api.ai agent
        '''

        self.scheme = json.load(open(scheme_file, 'r')) if scheme_file is not None and os.path.exists(scheme_file) else dict()
        self.start_settings = self.scheme.get('start')
        self.intent_list = self.scheme.get('intent_list')
        self.required_intent_name_list = self.start_settings.get('intent_name') if isinstance(self.start_settings, dict) else None
        self.required_intent_name = self.required_intent_name_list[random.randint(0, len(self.required_intent_name_list) - 1)] if isinstance(self.required_intent_name_list, list) else None
        self.required_intent = self._build_intent_by_name(self.required_intent_name)

        self.intent_names = self._extract_intent_names()

        self.apiai_bot_client_key = apiai_bot_client_key
        self.bot = APIAIBot(client_key=self.apiai_bot_client_key)

        self.scenario_complete = False

        self.say_to_user = str()

    def _extract_intent_names(self) -> List[str] or None:
        '''
        build and return intent name list
        Returns:
            list of intent names
        '''

        intent_names = list()
        try:
            for intent_dict in self.intent_list:
                intent_name = intent_dict.get('intent_name')
                intent_names.append(intent_name)
            return intent_names
        except Exception as e:
            ErrorLogger(__file__, e)
            return None


    def _build_intent_by_name(self, intent_name: str) -> Intent or None:
        '''
        find intent in scheme by name and build Intent class object
        Args:
            intent_name: name of intent
        Returns:
            if the name exists return built intent
            else return None
        '''
        try:
            if intent_name is None:
                return None

            for intent_item in self.intent_list:
                if intent_item.get('intent_name') == intent_name:
                    pause_duration_options = None
                    options = intent_item.get('options')
                    if isinstance(options, dict):
                        pause_duration_options = PauseDurationOptions(options.get('pause_duration'))
                    intent = Intent(name=intent_item.get('intent_name'), \
                                    listen_user=intent_item.get('listen_user'),
                                    is_start=intent_item.get('is_start'), \
                                    is_last=intent_item.get('is_last'), \
                                    pause_duration_options=pause_duration_options, \
                                    next_intent_name = intent_item.get('goto_next'), \
                                    initiate_intent_with_name=intent_item.get('initiate_intent'), \
                                    workflow_status=intent_item.get('workflow_status')
                                    )
                    return intent
        except Exception as e:
                ErrorLogger(__file__, e)
                return None

    def _append_say_to_user_text(self, text):
        self.say_to_user += text + '.'

    def _initiate_intent(self, intent_name) -> None:
        '''
        initiate intent explicitly
        Args:
            intent_name: name of intent
        '''
        try:
            bot_answer = self.bot.request(intent_name)
            self._append_say_to_user_text(bot_answer['text'])
        except Exception as e:
            ErrorLogger(__file__, e)

    def _process_workflow_status(self, status: dict) -> None:
        '''
        extract sale status description from workflow_status dictionary
        and voice it
        Args:
            status: dictionary with structure:
                {
                    'status': 'status',
                    'description': 'description'
                }
        '''
        self.log_structure['status'] = status
        self._append_say_to_user_text(workflow_status.get('description'))

    def _process_intent_after_complete(self, intent: Intent) -> None:
        '''
        proccess intent after it is complete
        Args:
            intent: Intent class object
        '''

        try:
            if self.required_intent_name != intent.next_intent_name:
                self.required_intent = self._build_intent_by_name(intent.next_intent_name) #build required intent
                self.required_intent_name = intent.next_intent_name

            self._append_say_to_user_text(text=intent.say_to_user)

            print('initiate_intent_with_name:', intent.initiate_intent_with_name)
            if isinstance(intent.initiate_intent_with_name, str):
                self._initiate_intent(intent.initiate_intent_with_name)

            if isinstance(intent.initiate_intent_with_name, dict):
                self._process_workflow_status(status=intent.workflow_status)

            if intent.is_last is True: #check if intent is last (terminate)
                self.scenario_complete = True

        except Exception as e:
            ErrorLogger(__file__, e)

    def make_next_intent(self, speech_text: str=str(), pause_duration: int=int()) -> None:
        '''
        proccess scheme (execute scenario)
        '''

        self.say_to_user = str()
        if self.scenario_complete is False:
            try:
                #make request to bot
                bot_answer = self.bot.request(speech_text) if len(speech_text) > 0 else dict()
                if isinstance(self.required_intent, Intent):
                    if self.required_intent.listen_user is True: #if it is required to listen to user
                        #if initiated in api.ai intent has NO the same name that the required intent
                        if bot_answer.get('intent_name') != self.required_intent_name:
                            self._append_say_to_user_text('Повторите, пожалуйста. Плохо слышно')
                        else: #if the required intent initiated
                            #run required intent object
                            self.required_intent.run(pause=pause_duration, \
                                                say_to_user=bot_answer.get('text'), \
                                                save_intent=bot_answer['actionIncomplete'])
                            #and process it after complete
                            self._process_intent_after_complete(intent=self.required_intent)
                    else: #if it is NOT required to listen to user
                        self.required_intent.run() #run intent and proccess it after complete
                        self._process_intent_after_complete(intent=self.required_intent)
                else: #if required intent is absent
                    if bot_answer.get('intent_name') in self.intent_names: #if initiated in api.ai intent exists in scheme
                        intent_from_set = self._build_intent_by_name(intent_name=bot_answer.get('intent_name')) #build intent object
                        intent_from_set.run(pause=pause) #run it and proccess
                        self._process_intent_after_complete(intent=intent_from_set)
                    else: #if the intent is absent in scheme
                        self._append_say_to_user_text(bot_answer.get('text')) #voice text from bot answer
            except Exception as e:
                ErrorLogger(__file__, e)
