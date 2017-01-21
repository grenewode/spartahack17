class Description:

    def __init__(self, name, adjectives=None, children=None):
        self.name = name
        self.adjectives = adjectives if adjectives is not None else {}
        self.children = children if children is not None else []

    def short(self):
        adjectives = ', '.join(self.adjectives)
        return "There is a {adjectives} {name}".format(name=self.name,
                                                       adjectives=adjectives)

    def long(self):
        return [self.short()] + [desc + ' in the ' + self.name
                                 for child in self.children
                                 for desc in child.long()]
