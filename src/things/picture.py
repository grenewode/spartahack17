from engine import register
from thing import Thing
from attrs.color import Color
from description import Description


@register
class Picture(Thing):
    name = 'picture'

    def __init__(self, engine):
        super().__init__(engine)
        self.color = engine.build(Color)

    def describe(self):
        return Description('picture', adjectives=[self.color.describe()])
