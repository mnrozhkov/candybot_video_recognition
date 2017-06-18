import Algorithmia

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)
api_key = None


def get_face_features(photo: bytes) -> dict or None:
    '''Returns information about emotions, age and gender by face image
    Args:
        photo: bytes data
    Returns:
        most possible face features
        None: if failed
    '''
    
    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('MeisterUrian/FaceFeatures2/0.1.6')
        print(algo.pipe(photo))
    except Exception as e:
        logging.error(str(e))
    
