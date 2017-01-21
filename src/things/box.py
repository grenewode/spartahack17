from engine import register
from thing import Thing
from description import Description


@register
class Box(Thing):
    name = "box"

    def __init__(self, engine):
        super().__init__(engine)

    def describe(self):
        return Description('box')
