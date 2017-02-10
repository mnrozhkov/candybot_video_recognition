import Algorithmia
import logging

logging.basicConfig(filename='facial_algorithms.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

api_key = 'simAkHd6NFelROawvgBT9ouDB6C1'

def get_emotions(photo):
    '''Returns emotions by face image
    Args:
        photo: photo file name
    Returns:
        {'emotion1': confidence1, 'emotion2': confidence2, ...}: if data recieved
        None: if failed
    '''
    
    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/0.1.2')
        img = bytearray(photo.read())
        emotions = algo.pipe(img).result['results']
        d_emotions = dict()
        for emotion in emotions:
            d_emotions[emotion[1]] = emotion[0]
        return d_emotions
        
    except Exception as e:
        logging.error(str(e))
        return None


def celebrities_similarity(photo):
    '''Returns person similarity to some celebrity
    Args:
        photo: photo file name
    Returns:
        [Celebrity name, confidence]: if data recieved
        None: if failed
    '''
    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/DeepFaceRecognition/0.1.1')
        img = bytearray(photo.read())
        celebrities = algo.pipe(img).result['results']
        return [' '.join(celebrities[0][1].split('_')), celebrities[0][0]]
        
    except Exception as e:
        logging.error(str(e))
        return None


def verify_faces(photo1, photo2):
    '''Returns two photos similarity 
    Args:
        photo1: photo1 file name
        photo2: photo2 file name
    Returns:
        similarity information: if data recieved
        None: if failed
    '''
    try:
        data = [bytearray(photo1.read()), bytearray(photo2.read())]
        client = Algorithmia.client(api_key)
        algo = client.algo('zskurultay/ImageSimilarity/0.1.2')
        return algo.pipe(data)
    
    except Exception as e:
        logging.error(str(e))
        return None

def gender(photo):
    '''Computes gender probabilities
    Args:
        photo: photo file name
    Returns:
        dictionary with gender probablities: if data recieved
        None: if failed
    '''
    try:
        img = bytearray(photo.read())
        data = {'image': img}
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/GenderClassification/1.0.1')
        response = algo.pipe(img).result['results']
        return {response[0][1]: response[0][0], response[1][1]: response[1][0]}
    
    except Exception as e:
        logging.error(str(e))
        return None

def age(photo):
    '''Returns age groups with probabilies
    Args:
        photo: photo file name
    Returns:
        dictionary with ages probablities: if data recieved
        None: if failed
    '''
    try:
        img = bytearray(photo.read())
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
