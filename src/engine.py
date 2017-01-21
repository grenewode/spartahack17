class Engine:

    def __init__(self):
        self.things = {}
        self.rooms = {}
        self.attributes = {}

        self.room = None
        self.player = None

    def parse_string(self, string):
        words = string.split(" ")
        if words == ['look']:
            print(*self.room.describe(), sep='\n')

    def report_error(self, error):
        print('error: {}'.format(error))

    def say(self, message):
        print(message)

    def get_random_thing(self, name, tags=None):
        pass

    def get_random_room(self, name, tags=None):
        pass

    def get_random_attribute(self, name, tags=None):
        pass
