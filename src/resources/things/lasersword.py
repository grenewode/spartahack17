from things.weapon import Weapon


class Lasersword(Weapon):
    name = "lasersword"

    def __init__(self, engine):
        super().__init__(engine)


exports = Lasersword
