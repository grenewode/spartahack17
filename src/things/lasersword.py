from things.weapon import Weapon


class Lasersword(Weapon):
    name = "Lasersword"

    def __init__(self, engine):
        super().__init__(engine)
        
