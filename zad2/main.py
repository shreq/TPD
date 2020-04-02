import pandas
import scipy


def saddle_point(matrix):
    min_for_row = matrix.min(axis=1)
    max_for_col = matrix.max(axis=0)
    return min_for_row.max() == max_for_col.min()


rules = pandas.read_csv('rules.csv')
rules.index = rules.columns.values

print(rules)
