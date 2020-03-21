import numpy

from criteria.criterion import Criterion


class Savage(Criterion):

    def __init__(self, data):
        super().__init__(data)

    def evaluate(self):
        max_for_column = self.data.max()
        subtracted = self.data - max_for_column
        max_for_row = subtracted.max()
        return numpy.where(
            max_for_row == max_for_row.max()
        )[0]
