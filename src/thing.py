from worldobject import WorldObject


class Thing(WorldObject):

    def __init__(self, engine):
        super().__init__(engine)

    def describe(self):
        return self.namem
