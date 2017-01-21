from engine import register
from worldobject import WorldObject
from thing import Thing
from description import Description


@register
class Room(WorldObject):
    name = "Room"

    def __init__(self, engine):
        super().__init__(engine)
        num_things = 3
        self.things = [engine.build(Thing) for i in range(num_things)]

    def search(self, name):
        for thing in self.things:
            if thing.name == name:
                return thing
        return None

    def describe(self):
        return Description('room', children=[thing.describe()
                                             for thing in self.things])
