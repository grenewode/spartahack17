from things.weapon import Weapon


class Bomb(Weapon):
    name = "bomb"

    def __init__(self, engine):
        super().__init__(engine)
        
