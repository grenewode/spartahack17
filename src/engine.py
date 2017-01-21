from random import choice

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
        print(*self.room.describe().long(), sep='\n')

    def parse_string(self, string):
        words = string.split(" ")
        if words == ['look']:
            self.show_long_description(self.room.describe())
            return
        if words == ['quit']:
            self.running = False
            return

        if len(words) > 2 and words[:2] == ['look', 'at']:
            spec = words[2:]
            if spec[0] == 'the':
                del spec[0]
            thing = self.room.search(spec[-1])
            if thing is None:
                self.say('there is no ' + ' '.join(spec))
            else:
                self.it = thing
                print('You look at the ' + self.it.name)
        else:
            self.player.do_action(words[0], None, self)
            

    def report_error(self, error):
        print('error: {}'.format(error))

    def say(self, message):
        print(message)

    def build(self, typeinfo, *args, **kwargs):
        candidates = [world_object_type
                      for world_object_type in WORLD_OBJECT_TYPES
                      if issubclass(world_object_type, typeinfo)]
        return choice(candidates)(self, *args, **kwargs)
