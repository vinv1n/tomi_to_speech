import pyttsx3
from pyttsx3 import voice
import sys
import os
from gtts import gTTS


class TextToSpeech:
    def __init__(self):
        self.age = 69
        self.lang = 'fi'
        self.rate = 150
        self.lines = []

    def read_file(self):
        self.lines = []
        with open('TextFiles/', 'r') as file:
            self.lines = file.readlines()
        self.create_speech()

    def create_speech(self):

        final_string = ''
        for i in self.lines:
            final_string += i
        engine = pyttsx3.init()
        engine.setProperty(name='rate', value=150)
        engine.setProperty(name='voice', value='fi')
        engine.setProperty('age', 69)
        engine.say(final_string)
        engine.runAndWait()

        # create mp3-file
        self.create_mp3(final_string)

    @staticmethod
    def create_mp3(final_string):
        gtt = gTTS(text=final_string, lang='fi')
        gtt.save('audio.mp3')
        # os.system('mpg123 audio.mp3')

    def run(self, input_file):
        try:
            self.read_file(input_file)
        except KeyboardInterrupt:
            sys.exit('No more tomi :DDD\n'
                     '???\n'
                     'Profit')

if __name__ == '__main__':
    TextToSpeech().run()
