from worldobject import WorldObject

class Room(WorldObject):
    
    def __init__(self):
        super().__init__()
        self.num_things = 0
        #more stats
        
    def set_num_things(num):
        self.num_things = num
        
class RoomFactory():
    
    def __init__(self):
        pass
        
    def generate_room():
        Room room
        room.set_num_things(1) #RANDOMIZE Later
        
        for i in range(room.num_things):
            