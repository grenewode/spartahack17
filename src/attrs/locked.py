from attrs.attribute import Attribute

class Locked(Attribute):

    def __init__(self):
        super().__init__()
        self.Locked = False

    def describe(self):
        if self.Locked:
            return "The door is locked."
        else:
            return "The door is unlocked,"
