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

print(rules)
print()
print("There is " + ("" if saddle_point(rules) else "no ") + "saddle point")
print(("Reduced " if reduce_dominated(rules) else "No ") + "dominated rows/columns")

minValue = rules.values.min()

if minValue < 0:
    rules += -minValue

x = pulp.LpVariable.dicts("x", rules.index, lowBound=0)
modelA = pulp.LpProblem("A", pulp.LpMinimize)
modelA += pulp.lpSum(x)
for _, rowValue in rules.iterrows():
    modelA += pulp.lpSum([x[label] * rowValue[label] for label in rowValue.index]) >= 1
modelA.solve()

y = pulp.LpVariable.dicts("y", rules.index, lowBound=0)
modelB = pulp.LpProblem("B", pulp.LpMaximize)
modelB += pulp.lpSum(y)
for _, colValue in rules.iteritems():
    modelB += pulp.lpSum([y[label] * colValue[label] for label in colValue.index]) <= 1
modelB.solve()

gameValue = 1 / sum([x.varValue for x in modelA.variables()])

print("\nPlayer A stategy:")
for var in modelA.variables():
    print(var.name + ": " + str(var.varValue * gameValue))

print("\nPlayer B stategy:")
for var in modelB.variables():
    print(var.name + ": " + str(var.varValue * gameValue))

if minValue < 0:
    gameValue -= -minValue

print("\nGame value: ", gameValue)