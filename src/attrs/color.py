from engine import register
from random import choice

COLORS = ['red', 'green', 'blue']


@register
class Color:

    def __init__(self, engine):
        # super().__init__(self, engine)
        self.color = choice(COLORS)

    def describe(self):
        return self.color
