from attrs.attribute import Attribute

class Locked(Attribute):

    def __init__(self):
        super().__init__()
        self.locked = False

    def describe(self):
        if self.locked:
            return "The door is locked."
        else:
            return "The door is unlocked."
