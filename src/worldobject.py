class WorldObject:
    name = None

    def __init__(self):
        self.actions = {}
        self.descriptions = {}
        self.attributes = {}

    def register_action(self, action_name, callback):
        self.actions[action_name] = callback

    def has_action(self, action, engine):
        engine.say("yes" if action in self.actions else "no")

    def do_action(self, action, source, engine):
        if action not in self.actions:
            engine.report_error("action not found")
        else:
            self.actions[action](self, source, engine)

    def what_is(self, attribute, engine):
        if attribute not in self.attributes:
            engine.report_error("It does not have {} ".format(attribute))
        else:
            engine.say(self.attributes[attribute])

    def describe(self):
        return ['this is a ' + self.name]
