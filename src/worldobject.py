class WorldObject:
    """
    Describes anything that can be in the game.
    WorldObjects can have actions

    # Actions
    Actions are mappings from name -> behavior, which are how the state of the
    world is changed.

    Also, every WorldObject should set name to some english value, which is
    used to reference the object in the real world
    """
    name = None

    def __init__(self, engine):
        self.actions = {}
        self.attributes = {}

    def set_attr(self, value):
        self.attributes[type(value)] = value

    def get_attr(self, typeinfo):
        return self.attributes[typeinfo]

    def has_attr(self, typeinfo):
        return typeinfo in self.attributes

    def register_action(self, action_name, callback):
        """
        Call this function to register an action for this object.
        """
        self.actions[action_name] = callback

    def has_action(self, action, engine):
        """
        Allows the game to ast of a world object can do a particular action
        """
        engine.say("yes" if action in self.actions else "no")

    def do_action(self, action, source, engine):
        """
        Does an action
        """
        if action in self.actions:
            self.actions[action](source, engine)
            return True
        return False
