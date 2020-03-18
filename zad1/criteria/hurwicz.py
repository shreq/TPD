import numpy
from criteria.criterion import Criterion


class Hurwicz(Criterion):
    caution_factor = 0

    def __init__(self, data, caution_factor=0.5):
        super().__init__(data)
        self.caution_factor = caution_factor

    def evaluate(self):
        min_for_row = self.data.min(axis=1) * self.caution_factor
        max_for_row = self.data.max(axis=1) * (1 - self.caution_factor)
        weighed = max_for_row.add(min_for_row, fill_value=0)
        return numpy.where(
            weighed == weighed.max()
        )[0] + 1

    def modifiers(self):
        return " : " + self.caution_factor.__str__()
