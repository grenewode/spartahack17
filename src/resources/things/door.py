from resources.attrs.open import Open
from thing import Thing
from resources.attrs.locked import Locked


class Door(Thing):
    name = "door"

    def __init__(self, engine):
        super().__init__(engine)
        self.set_attr(Open())
        self.set_attr(Locked())
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
        if self.get_attr(Open).open:
            engine.goto_new_room()
        elif self.get_attr(Locked).locked:
            engine.say("The door is locked.")
        else:
            engine.say("The door is closed m8.")


exports = Door
