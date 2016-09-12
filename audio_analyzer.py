'''Analyzes audio data and make event depending on the speech content'''

from audio.audio_rw import AudioWriter
from audio.converter import AudioConverter
from audio.recognize import AudioRecognizer

import argparse

import pickle

import audio_decision


def main(frames_file, channels, sample_size, rate):
    '''Analyzes raw audio data and determines event by speech content

    Args:
        frames_file: file name which contains raw audio data
        channels: audio data channels number
        sample_size: format sample size
        rate: audio rate
    '''
    
    with open(frames_file, 'rb') as file: #loads raw audio data from file
        audio_frames = pickle.load(file)

    #saves raw audio data as wave file    
    audio_writer = AudioWriter(audio_frames, channels, sample_size, rate)
    wave_file = audio_writer.write()

    #converts wave to flac
    converter = AudioConverter()
    flac_file = converter.wave_to_flac(wave_file)

    #recognizes text from speech
    recognizer = AudioRecognizer(flac_file, rate)
    text = recognizer.recognize()

    #recognizes event name by text content
    event_recognizer = audio_decision.EventRecognizer(text=text)
    event_name, params = event_recognizer.recognize_event()

    #creates and makes event
    event = audio_decision.Event(event_name, params=params)
    event.make()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Sets up analyze')
    parser.add_argument(
        'frames_file', type=str)
    parser.add_argument(
        'channels', type=int)
    parser.add_argument(
        'sample_size', type=int)
    parser.add_argument(
        'rate', type=int)
    
    args = parser.parse_args()

    main(args.frames_file, args.channels, args.sample_size, args.rate)
