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

    def read_file(self, input_file):
        lines = None
        with open(input_file, 'r') as f:
            lines = f.read()

        return lines

    def create_speech(self, lines):

        engine = pyttsx3.init()
        engine.setProperty(name='rate', value=1000)
        engine.setProperty(name='voice', value='fi')
        engine.setProperty('age', 69)
        engine.say(lines)
        engine.runAndWait()


    def create_mp3(self, output_file, lines):
        gtt = gTTS(text=lines, lang='fi')
        gtt.save(output_file + '.mp3')

    def run(self, input_file, output_file="defult", output_type="mp3"):

        if not input_file:
            sys.exit("No input file")

        if not os.path.exists(input_file):
            raise IOError("Invalid path to file")

        lines = self.read_file(input_file)
        if not lines:
            sys.exit("No input text")

        if output_type == "mp3":
            self.create_mp3(output_file, lines)
        elif output_type == "both":
            self.create_speech(lines=lines)
            self.create_mp3(output_file, lines)
        else:
            self.create_speech(lines)


def main():
    parser = argparse.ArgumentParser(prog="speech")
    parser.add_argument('--output', help="Name of output file", required=False)
    parser.add_argument('--input', help="Path to input file")
    parser.add_argument('--type', help="Path to input file")
    args = vars(parser.parse_args())

    input_file = args.get('input')
    output_file = 'default'
    if args.get('output'):
        output_file = args.get('output', "")

    try:
        TextToSpeech().run(output_file=output_file, input_file=input_file, output_type=args.get("type"))
    except IOError as e:
        print("Error {}".format(e))

if __name__ == '__main__':
    main()