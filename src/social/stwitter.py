#!/usr/bin/env python3

# Import the necessary package to process data in JSON format

import json
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()
import os
os.path.append(top)

# from twython import Twython
from secret import (
    TW_CONSUMER_KEY,
    TW_CONSUMER_SECRET,
    TW_ACCESS_TOKEN_KEY,
    TW_ACCESS_TOKEN_SECRET
)

import random


class TwitterCodeScanner:

    def __init__(self, required_track: str='@funrobots', timeout=300):
        '''
        Constructor
        Args:
            required_track: required track
        '''

        self.CONSUMER_KEY=TW_CONSUMER_KEY
        self.CONSUMER_SECRET=TW_CONSUMER_SECRET
        self.ACCESS_TOKEN=TW_ACCESS_TOKEN_KEY
        self.ACCESS_SECRET=TW_ACCESS_TOKEN_SECRET
        self.oauth = OAuth(self.ACCESS_TOKEN, self.ACCESS_SECRET, self.CONSUMER_KEY, self.CONSUMER_SECRET)
        # Initiate the connection to Twitter Streaming API
        self.twitter_stream = TwitterStream(auth=self.oauth, timeout=30)
        self.required_track = required_track

    def generate_code(self) -> str:
        '''
        generate code
        Returns:
            generated code
        '''

        code = str()
        for i in range(4):
            code += str(random.randint(0,10))
        return code

    def listenTwitter(self, code):
        """
        Listen Twitter for mention of keywords stated in 'track' and 'code'.
        Use Twitter stream API
        Params:
            track: message to track in Tweets
            code: unique code from CandyBot
        Returns:
            True or False decision status on candy dispensing
        """

        # Listen for tweets with required track (@funrobots) and #code
        iterator = self.twitter_stream.statuses.filter(track=self.required_track)
        while True:
            if iterator is not None:
                for tweet in iterator:
                    tw_text = json.loads(json.dumps(tweet)).get('text')
                    # print(tw_text, "\n")  ##for debug
                    if tw_text is not None:
                        if code in tw_text:
                            print("PLEASE, TAKE YOUR CANDY! :)))))))))")
                            return True
                        else:
                            return(False)
                    return False
            return False


#if __name__ == "__main__":
#    ts = TwitterCodeScanner()
#    get_candy = ts.listenTwitter(code='4451')
#    print(get_candy)
