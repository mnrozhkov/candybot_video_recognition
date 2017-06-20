import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import io
import numpy
from PIL import Image
import base64
import cv2

from utils import ErrorLogger


def ndarray2format(raw_img: numpy.ndarray, format: str='png') -> bytes:
    '''
    Converts numpy.ndarray to some binary format (png, jpeg, ...)
    '''
    try:
        fp = io.BytesIO() #create io stream
        img = Image.fromarray(raw_img) #grab image from ndarray
        img.save(fp=fp, format=format) #save image in stream
        fp.seek(0) #move stream cursor to start
        return fp.read() #return stream content (bytes)
    except Exception as e:
        ErrorLogger(__file__, e)
        return None


def ndarray2str(raw_img: numpy.ndarray, format: str='png') -> str:
    '''
    Converts numpy.ndarray to string
    '''
    try:
        bimg = cv2.imencode('.' + format, raw_img)[1].tostring()
        return base64.b64encode(bimg).decode('utf-8')
    except Exception as e:
        ErrorLogger(__file__, e)
        return None

def str2ndarray(string: str) -> numpy.ndarray:
    try:
        b64str = base64.b64decode(string.encode('utf-8'))
        nparr = numpy.fromstring(b64str, numpy.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return image
    except Exception as e:
        ErrorLogger(__file__, e)
        return None
