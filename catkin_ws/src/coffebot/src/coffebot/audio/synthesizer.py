from urllib import request, parse

from player import Player

class Talker:

    def __init__(self, yandex_voice_key: str):
        self.yandex_voice_key = yandex_voice_key
        self._player = Player()

    def text_to_speech(self, text: str) -> bytes:
        try:
            url = 'https://tts.voicetech.yandex.net/generate?text='
            url += parse.quote(text)
            url += '&format=wav&lang=ru&speaker=ermil&key=' + self.yandex_voice_key
            req = request.urlopen(url)

            return req.read()
            print('yandex!')
        except Exception as e:
            logging.error(str(e))
            print(str(e))
