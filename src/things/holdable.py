from things import Thing


class Holdable(Thing):

    def __init__(self, engine):
        super().__init__(engine)
        self.holder = None
