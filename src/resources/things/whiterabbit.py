from things.takeable import Takeable


class Snowbunny(Takeable):
    name = "white rabbit"

    def __init__(self, engine):
        super().__init__(engine)
exports = Snowbunny
