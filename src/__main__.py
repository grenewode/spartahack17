import things
import attrs

from engine import Engine, WORLD_OBJECT_TYPES
from player import Player
from room import Room

if __name__ == "__main__":
    print(WORLD_OBJECT_TYPES)
    engine = Engine()

    engine.player = engine.build(Player)
    engine.room = engine.build(Room)
    
    engine.show_long_description(engine.room.describe())

    while engine.running:
        command = input(">> ")
        engine.parse_string(command)
        
