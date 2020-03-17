import numpy
from criterion import Criterion


class Wald(Criterion):

    def __init__(self, data):
        super().__init__(data)

    def evaluate(self):
        min_for_row = self.data.min(axis=1)
        max_for_min = min_for_row.max()
        return numpy.where(min_for_row == max_for_min)[0] + 1
