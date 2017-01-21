from worldobject import WorldObject


class Thing(WorldObject):

    def __init__(self, engine):
        super().__init__(engine)

    def describe(self):
        return self.name
        
    def desc_attrs(self):
        return ','.join([attr.describe() for attr in self.attributes.values()])
