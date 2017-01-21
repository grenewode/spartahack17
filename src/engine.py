from random import choice
from textblob import TextBlob

WORLD_OBJECT_TYPES = []


def register(*classes):
    # global WORLD_OBJECT_TYPES
    for clazz in classes:
        WORLD_OBJECT_TYPES.append(clazz)


def extract_tags(tag_list):
    return [tag[1] for tag in tag_list]


def extract_words(tag_list):
    return [tag[0] for tag in tag_list]


def extract(tag_list):
    return (extract_words(tag_list), extract_tags(tag_list))


def target_command(tags, callback):
    words, tags = extract(tags)
    if len(tags) == 3 and tags == ('VB', 'NN'):
        callback(*words)

    if len(tags) == 2 and tags == ('VB', 'DT', 'NN'):
        callback(words[0], words[2])


def target_player(tags, callback):
    words, tags = extract(tags)
    if len(tags) == 1 and tags == ('VB'):
        return callback(words[0])


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
        if target_command(tags,
                          lambda verb, noun:
                          self.room.search_and_do(noun, verb,
                                                  self.player, self)):
            return




    def report_error(self, error):
        print('error: {}'.format(error))

    def say(self, message):
        print(message)

    def build(self, typeinfo, *args, **kwargs):
        candidates = [world_object_type
                      for world_object_type in WORLD_OBJECT_TYPES
                      if issubclass(world_object_type, typeinfo)]
        return choice(candidates)(self, *args, **kwargs)
