from things import Thing
from attrs.color import Color


class Pigmented(Thing):

    def __init__(self, engine):
        super().__init__(engine)
        self.set_attr(Color())
