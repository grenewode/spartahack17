from engine import register
from things.weapon import Weapon
from description import Description


@register
class Sword(Weapon):
    name = "sword"

    def __init__(self, engine):
        super().__init__(engine)
        self.register_action('take', self.take)

    def take(self, source, engine):
        source.add(self)

    def describe(self):
        return Description('sword')
