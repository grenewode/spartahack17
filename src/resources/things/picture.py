from things.pigmented import Pigmented


class Picture(Pigmented):
    name = 'picture'

    def __init__(self, engine):
        super().__init__(engine)
exports = Picture
