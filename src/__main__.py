from engine import Engine
from player import Player


if __name__ == "__main__":
    engine = Engine()
    engine.player = Player()

    while True:
        command = input(">> ")
        engine.parse_string(command)
