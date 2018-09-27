import pyttsx3
from pyttsx3 import voice
import sys
import argparse
import os
from gtts import gTTS


class TextToSpeech:
    def __init__(self):
        self.age = 69
        self.lang = 'fi'
        self.rate = 150
        self.lines = []
        self.output_file = ""
        self.input_file = ""

    def read_file(self):
        self.lines = []
        with open(self.input_file, 'r') as f:
            self.lines = f.readlines()

        self.create_speech()

    def create_speech(self):

        final_string = ''
        for i in self.lines:
            final_string += i

        engine = pyttsx3.init()
        engine.setProperty(name='rate', value=1000)
        engine.setProperty(name='voice', value='fi')
        engine.setProperty('age', 69)
        engine.say(final_string)
        engine.runAndWait()

        # create mp3-file
        self.create_mp3(final_string)

    def create_mp3(self, final_string):
        gtt = gTTS(text=final_string, lang='fi')
        gtt.save(self.input_file + '.mp3')
        os.system('mpg123' + self.input_file + '.mp3')

    def run(self, output_file, input_file):
        self.output_file = output_file
        if not os.path.exists(input_file):
            raise IOError("Invalid path to file")
        self.input_file = input_file
        try:
            self.read_file()
        except KeyboardInterrupt:
            sys.exit('No more tomi :DDD\n'
                     '???\n'
                     'Profit')

def main():
    parser = argparse.ArgumentParser(prog="speech")
    parser.add_argument('--output', help="Name of output file", required=False)
    parser.add_argument('--input', help="Path to input file")
    args = vars(parser.parse_args())

    input_file = args.get('input')
    output_file = 'default'
    if args.get('output'):
        output_file = args.get('output')
    try:
        TextToSpeech().run(output_file=output_file, input_file=input_file)
    except IOError as e:
        print("Error {}".format(e))

if __name__ == '__main__':
    main()