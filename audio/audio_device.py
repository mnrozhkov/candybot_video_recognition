'''This module allows to record audio from microphone '''
import pyaudio
import audioop
import time


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024


def start_microphone_recording(min_amplitude=550):
    '''Starts recording sounds from microphone.
    Args:
        min_amplitude: minimal sound amplitude to start record

    Returns:
        list[raw recorded data list - frames of auodio-record,
             format size]
    '''
    
    audio = pyaudio.PyAudio()
    was_speech = False #detect first "loud" sound
    silence_count = 0 #counter of chunks with silence
    print ("recording...")
    frames = []
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    while True:
        data = stream.read(CHUNK) #read next chunk and add it to array
        amplitude = audioop.rms(data, 2)
        print('amplitude=',amplitude)
        if amplitude >= min_amplitude: 
            was_speech = True           #if speech (sounds) was
            silence_count = 0           #wait for "long" silence
        if was_speech:
            frames.append(data)
        if was_speech and amplitude < min_amplitude:
            silence_count +=1
        if silence_count >= 30: #break if detected "long" silence
            break
        
    print("finished recording")
     
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    return frames, audio.get_sample_size(FORMAT)
