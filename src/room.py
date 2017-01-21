from worldobject import WorldObject
from thing import Thing
from engine import Engine

class Room(WorldObject):
    
    def __init__(self):
        super().__init__()
        self.num_things = 0
        self.things = []
        #more stats
        
    def set_num_things(self, num):
        self.num_things = num
        
    def add_thing(self, thing):
        self.things.append(thing)
        
class RoomFactory():
    
    def __init__(self):
        self.room = None
        
    def generate_room(self, engine):
        self.room = Room()
        self.room.set_num_things(1) #RANDOMIZE Later
        
        for i in range(self.room.num_things):
            self.room.add_thing(engine.get_random_thing())
            
    def get_room(self):
        return self.room