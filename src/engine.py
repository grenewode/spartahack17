from room import RoomFactory
from thing import ThingFactory

class Engine:

    def __init__(self):
        self.things = {}
        self.rooms = {}
        self.attributes = {}

    def parse_string(self, string):
        pass

    def report_error(self, error):
        print('error: {}'.format(error))

    def say(self, message):
        print(message)

    def get_random_thing(self, name, tags=None):
        t_fac = ThingFactory()
        t_fac.generate_thing()
        return t_fac.get_thing()

    def get_random_room(self, name, tags=None):
        r_fac = RoomFactory()
        r_fac.generate_room()
        return r_fac.get_room()

    def get_random_attribute(self, name, tags=None):
        pass
