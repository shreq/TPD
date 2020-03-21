import numpy
from criteria.criterion import Criterion


class BayesLaplace(Criterion):
    probability = []

    def __init__(self, data, probability=None):
        super().__init__(data)
        if probability is None:
            probability = [round(1 / len(data.columns), 3) for _ in data.columns]
        self.probability = probability

    def evaluate(self):
        weighed = self.data * self.probability
        summed = weighed.sum(axis=1)
        return numpy.where(
            summed == summed.max()
        )[0]

    def modifiers(self):
        return " : " + self.probability.__str__()
