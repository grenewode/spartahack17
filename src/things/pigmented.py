from thing import Thing
from resources.attrs.color import Color


class Pigmented(Thing):

    def __init__(self, engine):
        super().__init__(engine)
        self.set_attr(Color())
