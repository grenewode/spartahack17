from engine import Engine
import player
import room
import glob
import importlib
import os.path

# from things import box, sword, picture, door, bomb, key, egg, lasersword, sliceofbread, whiterabbit, doombringer
# register(box.Box, sword.Sword, picture.Picture, room.Room, player.Player, door.Door,
#          bomb.Bomb, key.Key, egg.Egg, lasersword.Lasersword, sliceofbread.SliceofBread, whiterabbit.Snowbunny, doombringer.DoomBringer
#          )


def load(directory):
    types = []
    for mod in glob.glob(directory + "/*.py"):
        try:
            mod = os.path.basename(mod)[:-3]
            module = importlib.import_module('resources.things.' + mod)
            types.append(module.exports)
        except AttributeError:
            pass
    return types


if __name__ == "__main__":
    engine = Engine(load("./src/resources/things/") +
                    load("./src/resources/things/") +
                    [player.Player, room.Room])

    engine.player = engine.build(player.Player)
    engine.room = engine.build(room.Room)

    engine.show_long_description(engine.room.describe())

    while engine.running:
        command = input(">> ")
        engine.parse_string(command)
