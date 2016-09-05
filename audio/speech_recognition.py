'''Uses Google Speech API to recognize text from audio format.
Google Speech API supports only flac mono format'''

import argparse
import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials

SPEECH_DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')

RATE = 16000


def google_speech_recognize(flac_file, lang='ru-RU'):
    '''Allows to recognize text from flac audio file (speech to text)

    Args:
        flac_file: flac file name
        lang: recognition language

    Returns:
        recognized text - if recognition is available
        None - in other case
    '''
    
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    try:
        http = httplib2.Http()
        credentials.authorize(http)

        service = discovery.build('speech', 'v1beta1', http=http,
                                  discoveryServiceUrl=SPEECH_DISCOVERY_URL)
        with open(flac_file, 'rb') as speech:
            speech_content = base64.b64encode(speech.read())

        service_request = service.speech().syncrecognize(
            body={
                'config': {
                    'encoding': 'FLAC',  
                    'sampleRate': RATE,  
                    'languageCode': lang
                },
                'audio': {
                    'content': speech_content.decode('UTF-8')
                    }
                })
        response = service_request.execute()
        try:
            return response['results'][0]['alternatives'][0]['transcript']
        except:
            return None
    except:
        print('Connection error')
        return None
