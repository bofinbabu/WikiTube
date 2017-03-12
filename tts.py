from __future__ import unicode_literals
import logging
from watson_developer_cloud import TextToSpeechV1
import time

class TTS(object):
    def __init__(self, tts_username, tts_password, voice):
        self._logger = logging.getLogger(self.__class__.__name__)
        file_handler = logging.FileHandler('TTS.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
        formatter.datefmt = '%a, %d %b %Y %H:%M:%S'
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        self.voice = voice #'en-US_AllisonVoice'
        self.text_to_speech = TextToSpeechV1(username=tts_username, password=tts_password)
    def tts_wav(self, text):
        try:
            return self.text_to_speech.synthesize(text, voice=self.voice)
        except:
            self._logger.error('TTS Failed')
    def tts_wav_file(self, text):
        try:
            filename = unicode(time.asctime()).replace(' ', '_') + u'_' + self.voice + u'.wav'
            with open(filename, 'wb') as af:
                af.write(self.text_to_speech.synthesize(text, voice=self.voice))
        except:
            self._logger.error('TTS_to_file Failed')