from things.takable import takable


class Key(takable):
    name = "key"

    def __init__(self, engine):
        super().__init__(engine)
