from attrs.attribute import Attribute


class Open(Attribute):

    def __init__(self):
        super().__init__()
        self.open = False

    def describe(self):
        if self.open:
            return "Open"
        else:
            return "Closed"
