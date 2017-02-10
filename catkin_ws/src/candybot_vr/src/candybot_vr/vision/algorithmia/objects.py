import Algorithmia
import logging

logging.basicConfig(filename='objects_algotithms.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

api_key = 'simAkHd6NFelROawvgBT9ouDB6C1'


def place(photo):
    '''Returns place probabilty by photo
    Args:
        photo: photo file name
    Returns:
        place info: if data recieved
        None: if failed
    '''
    
    try:
        img = bytearray(open(photo, 'rb').read())
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/Places365Classifier/0.1.9')
        result = algo.pipe(img).result['predictions']
        return result
    except Exception as e:
        logging.error(str(e))
        return None

#Does not work!
def get_object(photo):
    '''Returns object name by photo
    Args:
        photo: photo file name
    Returns:
        object info: if data recieved
        None: if failed
    '''
    try:
        img = bytearray(open(photo, 'rb').read())
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/CaffeNet/1.0.1')
        response = algo.pipe(img)
        return response
    except Exception as e:
        logging.error(str(e))
        return None


def memorability(photo):
    '''Returns photo memorability
    Args:
        photo: photo file name
    Returns:
        memorability: float number; if data recieved
        None: if failed
    '''
    try:
        img = bytearray(open(photo, 'rb').read())
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/LargescaleImageMemorability/0.1.3')
        return algo.pipe(img).result['memorability']
    except Exception as e:
        logging.error(str(e))
        return None
