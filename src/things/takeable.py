from thing import Thing


class Takeable(Thing):

    def __init__(self, engine):
        super().__init__(engine)
        self.holder = None
        self.register_action('take', self.take)

    def take(self, source, engine):
        engine.say('You have a ' + self.name)
        source.add(self)
