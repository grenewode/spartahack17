from engine import Engine
import player
import room
import glob
import importlib
import os.path


def load(rdirectory):
    types = []
    main_path = os.path.dirname(__file__)
    path = os.path.join(main_path, rdirectory, "*.py")
    for mod in glob.glob(path):
        try:
            mod = os.path.basename(mod)[:-3]
            module = importlib.import_module('resources.things.' + mod)
            types.append(module.exports)
        except AttributeError:
            pass
    return types


if __name__ == "__main__":
    engine = Engine(load("resources/things/") +
                    load("resources/things/") +
                    [player.Player, room.Room])

    engine.player = engine.build(player.Player)
    engine.room = engine.build(room.Room)

    engine.show_long_description(engine.room.describe())

    while engine.running:
        command = input(">> ")
        engine.parse_string(command)
