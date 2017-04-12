from urllib import request, parse
#from gtts import gTTS
import io
import pyaudio
import wave


class Talker:

    def __init__(self):

        self.TTSs = {'rhvoice': self._sayrhvoice,
                     'yandex': self._sayyandex,
                     'google': self._saygoogle
                     }

    def _play_wav(self, wav_src):

        #define stream chunk   
        chunk = 1024  

        #open a wav format music  
        f = wave.Wave_read(wav_src) 
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        #close PyAudio  
        p.terminate()

    
    def _sayrhvoice(self, text):
        '''Says text
        Args:
            text: text to say
        '''
        try:
            echo_proc = subprocess.Popen(['echo', text],
                                                 stdout=subprocess.PIPE)
            rhvoice_proc = subprocess.call(['spd-say', '-w', '-o', 'rhvoice',
                                            '-l', 'ru', '-e', '-t', 'male1'],
                                           stdin=echo_proc.stdout)

        except Exception as e:
            logging.error(str(e))


    def _sayyandex(self, text):
        try:
            url = 'https://tts.voicetech.yandex.net/generate?text='
            url += parse.quote(text)
            url += '&format=wav&lang=ru&speaker=ermil&key=49d9bb75-7419-45cc-9988-76052abc6c44'
            req = request.urlopen(url)

            self._play_wav(req)
            print('yandex!')
        except Exception as e:
            logging.error(str(e))
            print(str(e))
        

    def _saygoogle(self, text):
        pass

    def say(self, tts_name, text):
        print('--say--')
        self.TTSs[tts_name](text)

    def tts_names():
        return list(self.TTSs.keys())
