'''Allows recognize text from speech'''

import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials

SPEECH_DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')

class AudioRecognizer:
    '''Allows recognize text from speech'''
    
    def __init__(self, flac_file, rate=16000, lang='ru-RU'):
        '''Constructor
        Args:
            flac_file: flac file name
            rate: audio rate
            lang: audio language
        '''
        self.flac_file = flac_file
        self.rate = rate
        self.lang = lang

    def recognize(self):
        '''Recognizes text from speech'''
        
        credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
        http = httplib2.Http()
        credentials.authorize(http)

        service = discovery.build('speech', 'v1beta1', http=http,
                                  discoveryServiceUrl=SPEECH_DISCOVERY_URL)
        with open(self.flac_file, 'rb') as speech:
            speech_content = base64.b64encode(speech.read())

        service_request = service.speech().syncrecognize(
            body={
                'config': {
                    'encoding': 'FLAC',  
                    'sampleRate': self.rate,  
                    'languageCode': self.lang
                },
                'audio': {
                    'content': speech_content.decode('UTF-8')
                    }
                })
        response = service_request.execute()
        try:
            return response['results'][0]['alternatives'][0]['transcript']
        except KeyError:
            return None
    
    
