from worldobject import WorldObject


class Player(WorldObject):

    def __init__(self, engine):
        super().__init__(engine)
        self.inventory = []

        self.register_action('inventory', self.show_inventory)
        self.register_action('look', self.look)

    def show_inventory(self, source, engine):
        engine.say("You have " + ",\n".join([thing.describe()
                                             for thing in self.inventory]))
        
    def look(self, source, engine):
        engine.show_long_description(engine.room.describe())

    def add(self, thing):
        self.inventory.append(thing)
