import numpy
from criteria.criterion import Criterion


class BayesLaplace(Criterion):
    probability = []

    def __init__(self, data, probability=None):
        super().__init__(data)
        self.probability = probability if probability is not None \
            else [0.2, 0.2, 0.2, 0.2, 0.2]

    def evaluate(self):
        weighed = self.data * self.probability
        summed = weighed.sum(axis=1)
        return numpy.where(
            summed == summed.max()
        )[0] + 1

    def modifiers(self):
        return " : " + self.probability.__str__()
