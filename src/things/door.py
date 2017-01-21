from attrs.open import Open
from thing import Thing
#from room import Room

class Door(Thing):
    name = "door"

    def __init__(self, engine):
        super().__init__(engine)
        self.set_attr(Open())
        self.register_action('open', self.open)
        self.register_action('close', self.close)
        self.register_action('enter', self.enter)

    def open(self, source, engine):
        self.get_attr(Open).open = True
        engine.say("The door is opened.")

    def close(self, source, engine):
        self.get_attr(Open).open = False
        engine.say("The door is closed.")

    def enter(self, source, engine):
        engine.room = engine.build(Room)
        engine.show_long_description(engine.room.describe())
