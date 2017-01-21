from random import choice

COLORS = ['red', 'green', 'blue']


class Color:

    def __init__(self):
        # super().__init__(self, engine)
        self.color = choice(COLORS)

    def describe(self):
        return self.color
