import numpy

from criteria.criterion import Criterion


class Savage(Criterion):

    def __init__(self, data):
        super().__init__(data)

    def evaluate(self):
        max_for_column = self.data.max()
        subtracted = max_for_column - self.data
        max_for_row = subtracted.max(axis=1)
        return numpy.where(
            max_for_row == max_for_row.min()
        )[0]
