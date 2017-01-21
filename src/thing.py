from worldobject import WorldObject
from box import Box

class Thing(WorldObject):
    
    def __init__(self):
        super().__init__()
        
class ThingFactory():
    
    def __init__(self):
        self.box = None
        
    def generate_thing(self, engine):
        self.box = Box()
        #RANDOMIZE Later
        
    def get_thing(self):
        return self.box
        