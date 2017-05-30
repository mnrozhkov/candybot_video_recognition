#!/usr/bin/env python3

import vk
import time
import random

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)


class VkNeewsfeedScanner:
    '''
    newsfeed scanner (vk.com)
    '''

    def __init__(self, access_token: str, required_hashtag: str=str()):
        '''
        Constructor
        Args:
            access_token: vk access token
            required_hashtag: required hashtag
        '''
        self._session_opened = False
        self.access_token = access_token
        self.required_hashtag  = required_hashtag
        try:
            self._open_session()
            self._session_opened = True
        except Exception as e:
            logging.error(str(e))

    def _open_session(self) -> None:
        '''
        Open new session with vk api
        '''

    	self._session = vk.Session(access_token=self._access_token)
    	self._api = vk.API(self._ssession)

    def generate_hashtag(self) -> str:
        '''
        generate hashtag
        Returns:
            generated hashtag
        '''

    	hashtag = self.required_hashtag + '#'
    	for i in range(4):
    		hashtag += str(random.randint(0,10))
    	return hashtag

    def search_hashtag(self, hashtag: str) -> bool or None:
        '''
        Search post with specified hashtag among news from newsfeed
        Args:
            hashtag: additional hashtag
        Returns:
            True : if post with required and additional tags found
            False: if post with required and additional tags not found
            None: could not take access to vk api
        '''
        if self._session_opened is True:
        	nf = self._api.newsfeed.search(q=hashtag)
        	if(nf[0] > 0):
        		return True
    	    return False
        return None

    def listen(hashtag: str, timeout: int) -> bool:
        '''
        Scan newsfeed for post with specified hashtag during timeout (in seconds)
        Args:
            hashtag: additional hashtag
        Returns:
            True : if post with required and additional tags found
            False: if post with required and additional tags not found
            None: could not take access to vk api
        '''

    	start = time.time()
    	while time.time() - start < timeout:
            search_result = self.search_hashtag(hashtag)

            if search_result is None:
                return None

    		if search_result is True:
    			return True
    		time.sleep(0.1)

    	return False