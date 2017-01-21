from worldobject import WorldObject
from attrs.location import Location

class Thing(WorldObject):

    def __init__(self, engine):
        super().__init__(engine)
        self.location = Location()

    def describe(self):
        return self.name
        
    def desc_attrs(self):
        return ','.join([attr.describe() for attr in self.attributes.values()])
