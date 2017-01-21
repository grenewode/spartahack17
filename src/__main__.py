from engine import Engine, register
import player
import room


from things import box, sword, picture, door, bomb, key
register(box.Box, sword.Sword, picture.Picture, room.Room, player.Player, door.Door, bomb.Bomb, key.Key)

if __name__ == "__main__":
    engine = Engine()

    engine.player = engine.build(player.Player)
    engine.room = engine.build(room.Room)

    engine.show_long_description(engine.room.describe())

    while engine.running:
        command = input(">> ")
        engine.parse_string(command)
