from random import choice
from attrs.attribute import Attribute

ROOM_LOCATIONS = ['left', 'right', 'front', 'back']


class Location(Attribute):

    def __init__(self):
        super().__init__()
        self.location = choice(ROOM_LOCATIONS)

    def describe(self):
        return self.location


exports = Location
