from engine import register
from things.weapon import Weapon
from description import Description


@register
class Sword(Weapon):
    name = "sword"

    def __init__(self, engine):
        super().__init__(engine)

    def describe(self):
        return Description('sword')
