from things.takeable import Takeable


class Key(Takeable):
    name = "key"

    def __init__(self, engine):
        super().__init__(engine)
