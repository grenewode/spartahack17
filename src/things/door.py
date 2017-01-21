from attrs.open import Open
class Door(Thing):
    name = "door"

    def __init__(self, engine):
        super().__init__(engine)
        self.register_action('open', self.open)
        self.register_action('close', self.close)
        self.register_action('enter', self.enter) #work on this later, should trigger room generation

    def open(self, source, engine):
        self.get_attr(Open).open = True
        engine.say("The door is opened.")

    def close(self, source, engine):
        self.get_attr(Open).open = False
        engine.say("The door is closed.")
