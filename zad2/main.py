import pandas
import pulp


def saddle_point(matrix):
    min_for_row = matrix.min(axis=1)
    max_for_col = matrix.max(axis=0)
    return min_for_row.max() == max_for_col.min()


def is_dominant(master, slave):
    if len(master) != len(slave):
        raise Exception("Arrays' lengths do not match")

    for i in range(len(master)):
        if master[i] <= slave[i]:
            return False
    return True


def reduce_dominated(matrix):
    reduced = False
    for master_label, master_content in matrix.iterrows():
        for slave_label, slave_content in matrix.iterrows():
            if master_label != slave_label and is_dominant(master_content, slave_content):
                matrix.drop(labels=slave_label, inplace=True)
                reduced = True
    for master_label, master_content in matrix.iteritems():
        for slave_label, slave_content in matrix.iteritems():
            if master_label != slave_label and is_dominant(master_content, slave_content):
                matrix.drop(columns=slave_label, inplace=True)
                reduced = True
    return reduced


rules = pandas.read_csv('rules.csv')
rules.index = rules.columns.values

print("There is " + ("" if saddle_point(rules) else "no ") + "saddle point")
print(("Reduced " if reduce_dominated(rules) else "No ") + "dominated rows/columns")
print(rules)

x = pulp.LpVariable.dicts("x", rules.index, lowBound=0)
model = pulp.LpProblem("AAAAAAAA", pulp.LpMaximize)
print(x, '\n\n', model)
