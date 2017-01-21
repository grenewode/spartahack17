from things.weapon import Weapon


class Sword(Weapon):
    name = "sword"

    def __init__(self, engine):
        super().__init__(engine)
        self.register_action('take', self.take)

    def take(self, source, engine):
        source.add(self)

