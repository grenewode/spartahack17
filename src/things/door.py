class Door():
    name = "door"

    def __init__(self, engine):
        super().__init__(engine)
        self.register_action('open', self.open)
        self.register_action('close', self.close)
        self.register_action('enter', self.enter)

    def open(self, source, engine):
        source.open(self)

    def close(self, source, engine):
        source.close(self)

    def enter(self, source, engine):
        source.enter(self)
