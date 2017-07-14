#!/usr/bin/env python3

import vk
import time
import random

from utils import ErrorLogger


class VkNeewsfeedScanner:
    '''
    newsfeed scanner (vk.com)
    '''

    def __init__(self, access_token: str, group_access_token: str=str(), group_id: int=0, required_hashtag: str=str()):
        '''
        Constructor
        Args:
            access_token: vk access token
            required_hashtag: required hashtag
        '''
        self._session_opened = False
        self._access_token = access_token
        self._group_access_token = group_access_token
        self._group_id = group_id
        self.required_hashtag  = required_hashtag
        try:
            self._open_session()
            self._session_opened = True
        except Exception as e:
            ErrorLogger(__file__, e)

    def _open_session(self) -> None:
        '''
        Open new session with vk api
        '''

        self._session = vk.Session(access_token=self._access_token)
        self._api = vk.API(self._session)

    def generate_hashtag(self) -> str:
        '''
        generate hashtag
        Returns:
            generated hashtag
        '''

        hashtag = self.required_hashtag + ' #i'
        for i in range(4):
            hashtag += str(random.randint(0,9))
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
            group_wall = [0]
            if len(self._group_access_token) > 0 and self._group_id != 0:
                wall = self._api.wall.search(owner_id=-self._group_id, access_token=self._group_access_token, query=hashtag)
            if nf[0] > 0 or group_wall[0] > 0:
                return True
            return False
        return None

    def listen(self, hashtag: str, timeout: int) -> bool:
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
            time.sleep(1)

        return False
