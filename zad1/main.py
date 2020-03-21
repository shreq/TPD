from os import system, name
import pandas

from criteria.bayes_laplace import BayesLaplace
from criteria.hurwicz import Hurwicz
from criteria.optimistic import Optimistic
from criteria.savage import Savage
from criteria.wald import Wald


def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")


def array_to_string(criterion):
    result = criterion.evaluate()
    string = ", ".join(map(str, result+1))
    return string


data = pandas.read_csv("data.csv")
variants = data[:-2]
probabilities = data.iloc[-2].values.tolist()
gamma = data.iat[-1, 0]

criteria = [
    Wald(variants),
    Optimistic(variants),
    Hurwicz(variants, gamma),
    BayesLaplace(variants),
    BayesLaplace(variants, probabilities),
    Savage(variants)
]

print(variants, end="\n\n")

results = pandas.DataFrame(columns=['Selected variants']).rename_axis("Criterion", axis=1)
for criterion in criteria:
    results.at[
        criterion.__class__.__name__ + criterion.modifiers()
        ] = [array_to_string(criterion)]
print(results)
