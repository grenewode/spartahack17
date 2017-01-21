from things.holdable import Holdable


class Weapon(Holdable):

    def __init__(self, engine):
        super().__init__(engine)
