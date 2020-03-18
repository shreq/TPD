import numpy
from criteria.criterion import Criterion


class Optimistic(Criterion):

    def __init__(self, data):
        super().__init__(data)

    def evaluate(self):
        max_for_row = self.data.max(axis=1)
        return numpy.where(
            max_for_row == max_for_row.max()
        )[0] + 1
