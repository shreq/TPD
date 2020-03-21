import numpy
from criteria.criterion import Criterion


class Wald(Criterion):

    def __init__(self, data):
        super().__init__(data)

    def evaluate(self):
        min_for_row = self.data.min(axis=1)
        return numpy.where(
            min_for_row == min_for_row.max()
        )[0]
