from resources.attrs.open import Open
from things.openable import Openable
from resources.attrs.locked import Locked


class Door(Openable):
    name = "door"

    def __init__(self, engine):
        super().__init__(engine)
        self.set_attr(Locked())
        self.register_action('enter', self.enter)

    def enter(self, source, engine):
        if self.get_attr(Open).open:
            engine.goto_new_room()
        elif self.get_attr(Locked).locked:
            engine.say("door.is_locked")
        else:
            engine.say("door.is_unlocked")


exports = Door
