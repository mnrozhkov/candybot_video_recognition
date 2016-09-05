from audio import audio_device as ad

from audio import audio_converter as converter

from audio import speech_recognition as sr

from network import search_info

from audio import text_to_speech as tts

from audio import audio_player as player

frames, format_size = ad.start_microphone_recording()
wav_file = converter.convert_rawdata_to_wav(frames, format_size)
flac_file  = converter.convert_wav_to_flac(wav_file)
text = sr.google_speech_recognize(flac_file)
wiki_page = search_info.get_wiki_page(text)
mp3_file = tts.tts(wiki_page)
player.play_mp3(mp3_file)
