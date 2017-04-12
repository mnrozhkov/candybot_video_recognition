import Algorithmia

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)
api_key = None


def get_emotion(photo: bytes) -> str or None:
    '''Returns emotions by face image
    Args:
        photo: bytes data
    Returns:
        main_emotion: most possible emotion name
        None: if failed
    '''

    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/0.1.3')
        img = bytearray(photo)
        emotions = algo.pipe(img).result['results'][0]['emotion']
        main_emotion = str()
        confidence = 0.0
        for emotion in emotions:
            if emotion[0] > confidence:
                confidence = emotion[0]
                main_emotion = emotion[1]
        return main_emotion.lower()

    except Exception as e:
        logging.error(str(e))
        print('Algorithmia:', str(e))
        return None


def celebrities_similarity(photo: bytes) -> str or None:
    '''Returns person similarity to some celebrity
    Args:
        photo: bytes data
    Returns:
        Name of the most possible celebrity
        None: if failed
    '''
    try:
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/DeepFaceRecognition/0.1.1')
        img = bytearray(photo)
        celebrities = algo.pipe(img).result['results']
        return ' '.join(celebrities[0][1].split('_'))

    except Exception as e:
        logging.error(str(e))
        return None


def verify_faces(photo1: bytes, photo2: bytes) -> float or None:
    '''Returns two photos similarity
    Args:
        photo1: bytes data
        photo2: bytes data
    Returns:
        similarity confidence: if data recieved
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


def gender(photo: bytes) -> str or None:
    '''Computes gender probabilities
    Args:
        photo: bytes data
    Returns:
        gender name
        None: if failed
    '''
    try:
        img = bytearray(photo)
        data = {'image': img}
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/GenderClassification/1.0.2')
        gender_list = algo.pipe(img).result['results'][0]['gender']
        if gender_list[0][0] > gender_list[1][0]:
            return gender_list[0][1].lower()
        else:
            return gender_list[1][1].lower()

    except Exception as e:
        logging.error(str(e))
        return None


def age(photo: bytes) -> str or None:
    '''Returns age groups with probabilies
    Args:
        photo: bytes data
    Returns:
        the most possible age interval : list with structure [min_age, max_age]
        None: if failed
    '''
    try:
        img = bytearray(photo)
        client = Algorithmia.client(api_key)
        algo = client.algo('deeplearning/AgeClassification/1.0.3')
        ages = algo.pipe(img).result['results'][0]['age']
        str_age_interval = str()
        age_confidence = 0.0
        for age in ages:
            if age[0] > age_confidence:
                age_confidence = age[0]
                str_age_interval = age[1]
                
        age_string_interval = str_age_interval.strip('()').split(', ')
        age_interval = [int(age_string_interval[0]), int(age_string_interval[1])]
        return age_interval

    except Exception as e:
        logging.error(str(e))
        print(str(e))
        return None
