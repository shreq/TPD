from os import system, name
import pandas
import numpy

from optimistic import Optimistic
from wald import Wald


def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")


def array_to_string(criterion):
    result = criterion.evaluate()
    string = ", ".join(map(str, result))
    return string


setup = {}
data = pandas.DataFrame(
    data=[[20, 50, 70, 10, 10],
          [10, 25, 50, 70, 60],
          [30, 50, 40, 20, 50],
          [20, 40, 40, 10, 70],
          [40, 30, 65, 70, 70],
          [30, 30, 60, 50, 40]],
    index=[1, 2, 3, 4, 5, 6],
    columns=['I', 'II', 'III', 'IV', 'V']
)
criteria = [
    Wald(data),
    Optimistic(data)
]

print(data, end="\n\n")
results = pandas.DataFrame(columns=['Selected variants']).rename_axis("Criterion", axis=1)
for criterion in criteria:
    results.at[criterion.__class__.__name__] = [array_to_string(criterion)]
print(results)
