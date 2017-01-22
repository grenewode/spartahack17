from random import choice
# from textblob import TextBlob
from textblob import Blobber
from textblob.taggers import NLTKTagger, PatternTagger
from room import Room
from resources.phrases import phrases
import re


def extract_tags(tag_list):
    return [tag[1] for tag in tag_list]


def extract_words(tag_list):
    return [tag[0] for tag in tag_list]


def extract(tag_list):
    return (extract_words(tag_list), extract_tags(tag_list))


def run_command(engine, string, blobber):
    tags = blobber(string.lower()).pos_tags
    words, tags = extract(tags)
    print(words, tags, tags == ['VB', 'NN'])
    if tags == ['VB', 'NN']:
        verb, noun = tuple(words)
        # print(verb, noun)
        return engine.room.search_and_do(noun, verb, engine.player, engine)
    elif tags == ['VB', 'DT', 'NN']:
        verb, noun = (words[0], words[2])
        return engine.room.search_and_do(noun, verb, engine.player, engine)
    elif len(tags) == 1:
        return engine.player.do_action(words[0], None, engine)


class Engine:

    def __init__(self, types):
        self.types = types
        self.room = None
        self.player = None
        self.it = None
        self.running = True

    def goto_new_room(self):
        self.room = self.build(Room)
        self.show_long_description(self.room.describe())

    def show_long_description(self, description):
        print(*self.room.describe(), sep='\n')

    def parse_string(self, string):
        if string == "quit":
            self.running = False
            return

        if run_command(self, string, Blobber(pos_tagger=NLTKTagger())):
            return
        if run_command(self, string, Blobber(pos_tagger=PatternTagger())):
            return

        print('dont know how to ' + string)

    def report_error(self, error):
        print('error: {}'.format(error))

    def say(self, message):
        if message in phrases:
            print(choice(phrases[message]))
        else:
            print('shit')

    def build(self, typeinfo, *args, **kwargs):
        candidates = [world_object_type
                      for world_object_type in self.types
                      if issubclass(world_object_type, typeinfo)]
        return choice(candidates)(self, *args, **kwargs)
