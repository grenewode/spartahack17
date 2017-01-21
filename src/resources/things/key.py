from things.takeable import Takeable

class Key(Takeable):
    name = "key"

    def __init__(self, engine):
        super().__init__(engine)
        self.register_action('unlock',self.unlock)

    def unlock(self, source, engine):
        engine.say("It's unlocked.")
exports = Key
