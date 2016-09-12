'''Allow to convert audio files form one format to other'''

import soundfile as sf


class AudioConverter:
    '''Allow to convert audio files form one format to other'''

    def wave_to_flac(self, wave_file, flac_file=None):
        '''Converts audio file frome wave format to flac
        Args:
            wave_file: wave file name
        '''
        
        data, samplerate = sf.read(wave_file)
        if flac_file is None:
            flac_file = wave_file[:-4] + '.flac'
        sf.write(flac_file, data, samplerate)
        return flac_file
