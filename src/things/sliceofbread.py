from things.takeable import Takeable


class SliceofBread(Takeable):
    name = "slice of bread"

    def __init__(self, engine):
        super().__init__(engine)
