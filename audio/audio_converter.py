'''Allows to convert audio from raw data to wave audio format
and from wave to flac'''

import wave

import time


import soundfile


CHANNELS = 1
RATE = 16000


def convert_rawdata_to_wav(rawdata, format_size, wav_file_name=None):
    '''Converst raw data to wave audio format

    Args:
        rawdata: raw audio data list (audio frames)
        wav_file_name: file name to save raw data as wave-file

    Returns:
        wave file name
    '''

    if wav_file_name is None:
        wav_file_name = str(time.time()) + '.wav'
    waveFile = wave.open(wav_file_name, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(format_size)
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(rawdata))
    waveFile.close()
    return wav_file_name


def convert_wav_to_flac(wave_file):
    '''Converts wave audio file to flac format. Flac file has the same name
that wave file, but with .flac extension

    Args:
        wave_file: wave file name

    Returns:
        flac file name
    '''
    data, samplerate = soundfile.read(wave_file)
    flac_file = wave_file[:-4] + '.flac'
    soundfile.write(flac_file, data, samplerate)
    print('samplerate=', samplerate)
    return flac_file
