from thing import Thing


class Takeable(Thing):

    def __init__(self, engine):
        super().__init__(engine)
        self.holder = None
