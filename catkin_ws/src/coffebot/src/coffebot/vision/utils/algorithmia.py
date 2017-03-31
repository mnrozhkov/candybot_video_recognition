import Algorithmia
import logging

logging.basicConfig(filename='facial_algorithms.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

api_key = None

def get_emotions(photo: bytes) -> dict or None:
    '''Returns emotions by face image
    Args:
        photo: bytes data
    Returns:
        {'emotion1': confidence1, 'emotion2': confidence2, ...}: if data recieved
        None: if failed
    '''

    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/0.1.2')
        img = bytearray(photo)
        emotions = algo.pipe(img).result['results']
        d_emotions = dict()
        for emotion in emotions:
            d_emotions[emotion[1]] = emotion[0]
        return d_emotions

    except Exception as e:
        logging.error(str(e))
        print('Algorithmia:', str(e))
        return None


def celebrities_similarity(photo: bytes) -> list or None:
    '''Returns person similarity to some celebrity
    Args:
        photo: bytes data
    Returns:
        [Celebrity name, confidence]: if data recieved
        None: if failed
    '''
    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/DeepFaceRecognition/0.1.1')
        img = bytearray(photo)
        celebrities = algo.pipe(img).result['results']
        return [' '.join(celebrities[0][1].split('_')), celebrities[0][0]]

    except Exception as e:
        logging.error(str(e))
        return None


def verify_faces(photo1: bytes, photo2: bytes) -> float or None:
    '''Returns two photos similarity
    Args:
        photo1: bytes data
        photo2: bytes data
    Returns:
        similarity information: if data recieved
        None: if failed
    '''
    try:
        data = [bytearray(photo1), bytearray(photo2)]
        client = Algorithmia.client(api_key)
        algo = client.algo('zskurultay/ImageSimilarity/0.1.2')
        return algo.pipe(data)

    except Exception as e:
        logging.error(str(e))
        return None

def gender(photo: bytes) -> dict or None:
    '''Computes gender probabilities
    Args:
        photo: bytes data
    Returns:
        dictionary with gender probablities: if data recieved
        None: if failed
    '''
    try:
        img = bytearray(photo)
        data = {'image': img}
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/GenderClassification/1.0.1')
        response = algo.pipe(img).result['results']
        return {response[0][1]: response[0][0], response[1][1]: response[1][0]}

    except Exception as e:
        logging.error(str(e))
        return None

def age(photo: bytes) -> dict or None:
    '''Returns age groups with probabilies
    Args:
        photo: bytes data
    Returns:
        dictionary with ages probablities: if data recieved
        None: if failed
    '''
    try:
        img = bytearray(photo)
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/AgeClassification/1.0.2')
        response = algo.pipe(img).result['results']
        result = {}
        for item in response:
            result[item[1]] = item[0]
        return result

    except Exception as e:
        logging.error(str(e))
        return None
