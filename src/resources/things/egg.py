from things.takeable import Takeable


class Egg(Takeable):
    name = "egg"

    def __init__(self, engine):
        super().__init__(engine)

exports = Egg
