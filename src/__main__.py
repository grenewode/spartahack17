from engine import Engine
import player
import room
import glob
import importlib
import os.path


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
    engine = Engine(load("src/resources/things/") +
                    load("src/resources/things/") +
                    [player.Player, room.Room])

    engine.player = engine.build(player.Player)
    engine.room = engine.build(room.Room)

    engine.show_long_description(engine.room.describe())

    while engine.running:
        command = input(">> ")
        engine.parse_string(command)
