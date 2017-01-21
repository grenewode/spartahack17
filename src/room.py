from worldobject import WorldObject
from thing import Thing


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

    def search_and_do(self, name, action, source, engine, *args, **kwargs):
        target = self.search(name)

        if target:
            return target.do_action(action, source, engine, *args, **kwargs)
        else:
            engine.say('could not find a ' + name)
        return True

    def describe(self):
        #children=[thing.describe() for thing in self.things]
        return ["You are in a room"] + ['There is a '+child.desc_attrs()+ ' ' + child.describe() + ' in the ' + self.name #+'\n It is '+child.desc_attrs()
                                 for child in self.things]
