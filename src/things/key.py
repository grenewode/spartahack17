from things.takeable import Takable


class Key(Takable):
    name = "key"

    def __init__(self, engine):
        super().__init__(engine)
