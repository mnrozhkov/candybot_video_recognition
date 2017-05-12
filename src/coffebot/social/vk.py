import vk
import time
import random

#ключ доступа
access_token = ''
#открытие сессии и получение доступа к api

class VkNeewsfeedScanner:
    '''
    newsfeed scanner (vk.com)
    '''

    def __init__(self, access_token):
        '''
        constructor
        takes access token
        '''
        self.access_token = access_token
        self._open_session()

    def _open_session(self):
        '''
        open new session with vk api
        '''

    	self._session = vk.Session(access_token=self._access_token)
    	self._api = vk.API(self._ssession)

    def generate_hashtag(self) -> str:
        '''
        generate hashtag
        returns string
        '''
    	hashtag = '#'
    	for i in range(4):
    		hashtag += str(random.randint(0,10))
    	return hashtag

    def search_hashtag(self, hashtag: str) -> bool:
        '''
        search post with specified hashtag among news from newsfeed
        '''

    	nf = self._api.newsfeed.search(q=hashtag)
    	if(nf[0] > 0):
    		return True
    	return False

    def listen(hashtag: str, timeout: int) -> bool:
        '''
        scan newsfeed for post with specified hashtag during timeout (in seconds)
        '''

    	start = time.time()
    	while time.time() - start < timeout:
    		if self.search_hashtag(hashtag) is True:
    			return True
    		time.sleep(0.1)

    	return False
