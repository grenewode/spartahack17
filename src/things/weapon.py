from things.takeable import Takeable


class Weapon(Takeable):

    def __init__(self, engine):
        super().__init__(engine)
