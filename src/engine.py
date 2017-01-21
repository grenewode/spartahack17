from random import choice
from textblob import TextBlob

WORLD_OBJECT_TYPES = []


def register(clazz):
    # global WORLD_OBJECT_TYPES
    WORLD_OBJECT_TYPES.append(clazz)
    return clazz


class Engine:

    def __init__(self):
        self.room = None
        self.player = None
        self.it = None
        self.running = True

    def show_long_description(self, description):
        print(*self.room.describe(), sep='\n')

    def parse_string(self, string):
        if string == "quit":
            self.running = False
            return
        
        tags = TextBlob(string.lower()).pos_tags
        noun = None
        verb = None

        for (word, tag) in tags:
            if tag == 'VB':
                verb = word
                break
        for (word, tag) in tags:
            if tag == 'NN':
                noun = word
                break
        print(noun, verb)
        target = self.room.search(noun)
        if target:
            target.do_action(verb, self.player, self)

    def report_error(self, error):
        print('error: {}'.format(error))

    def say(self, message):
        print(message)

    def build(self, typeinfo, *args, **kwargs):
        candidates = [world_object_type
                      for world_object_type in WORLD_OBJECT_TYPES
                      if issubclass(world_object_type, typeinfo)]
        return choice(candidates)(self, *args, **kwargs)
