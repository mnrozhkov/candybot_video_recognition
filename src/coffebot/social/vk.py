#!/usr/bin/env python3

import vk
import time
import random


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

        self.access_token = access_token
        self.required_hashtag  = required_hashtag
        self._open_session()

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

    def search_hashtag(self, hashtag: str) -> bool:
        '''
        Search post with specified hashtag among news from newsfeed
        Args:
            hashtag: additional hashtag
        Returns:
            True : if post with required and additional tags found
            False: in other case
        '''

    	nf = self._api.newsfeed.search(q=hashtag)
    	if(nf[0] > 0):
    		return True
    	return False

    def listen(hashtag: str, timeout: int) -> bool:
        '''
        Scan newsfeed for post with specified hashtag during timeout (in seconds)
        Args:
            hashtag: additional hashtag
        Returns:
            True : if post with required and additional tags found
            False: in other case
        '''

    	start = time.time()
    	while time.time() - start < timeout:
    		if self.search_hashtag(hashtag) is True:
    			return True
    		time.sleep(0.1)

    	return False
