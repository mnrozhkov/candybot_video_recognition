from urllib import request, parse
#from gtts import gTTS
import io
import pyaudio
import wave


class Talker:

    def __init__(self, yandex_voice_key: str):
        self.yandex_voice_key = yandex_voice_key
	
    def _play_wav(self, wav_src: bytes) -> None:

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

    def sayyandex(self, text: str) -> None:
        try:
            url = 'https://tts.voicetech.yandex.net/generate?text='
            url += parse.quote(text)
            url += '&format=wav&lang=ru&speaker=ermil&key=' + self.yandex_voice_key
            req = request.urlopen(url)

            self._play_wav(req)
            print('yandex!')
        except Exception as e:
            logging.error(str(e))
            print(str(e))
    
    
