from random import choice
from attrs.attribute import Attribute

COLORS = ['red', 'green', 'blue']


class Color(Attribute):

    def __init__(self):
        super().__init__()
        self.color = choice(COLORS)

    def describe(self):
        return self.color

exports = Color
