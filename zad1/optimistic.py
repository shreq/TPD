import numpy
from criterion import Criterion


class Optimistic(Criterion):

    def __init__(self, data):
        super().__init__(data)

    def evaluate(self):
        max_for_row = self.data.max(axis=1)
        max_for_max = max_for_row.max()
        return numpy.where(max_for_row == max_for_max)[0] + 1
