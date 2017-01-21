from things.weapon import Weapon


class Sword(Weapon):
    name = "sword"

    def __init__(self, engine):
        super().__init__(engine)


exports = Sword
