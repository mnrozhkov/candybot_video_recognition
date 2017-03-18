import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import io
import numpy
from PIL import Image
import base64
import cv2
import pyaudio
import wave

def ndarray2format(raw_img: numpy.ndarray, format: str='png'):
    '''
    Converts numpy.ndarray to some binary format (png, jpeg, ...)
    '''
    fp = io.BytesIO() #create io stream
    img = Image.fromarray(raw_img) #grab image from ndarray
    img.save(fp=fp, format=format) #save image in stream
    fp.seek(0) #move stream cursor to start
    return fp.read() #return stream content (bytes)


def ndarray2str(raw_img: numpy.ndarray, format: str='png'):
    '''
    Converts numpy.ndarray to string
    '''
    bimg = cv2.imencode('.' + format, raw_img)[1].tostring() 
    return base64.b64encode(bimg).decode('utf-8')

    
def str2ndarray(string: str):
    nparr = numpy.fromstring(string.encode('utf-8'), uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image


def raw_audio2wav(raw_audio: bytes, pyaudio_config: dict):
    
    samp_size = pyaudio.PyAudio().get_sample_size(pyaudio_config['format'])
    f = io.BytesIO()
    wave_writer = wave.Wave_write(f)
    wave_writer.setnchannels(pyaudio_config['channels'])
    wave_writer.setsampwidth(samp_size)
    wave_writer.setframerate(pyaudio_config['rate'])
    wave_writer.writeframes(raw_audio)

    f.seek(0)
    return f.read()
        
