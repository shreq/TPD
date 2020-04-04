import pandas
import pulp


def saddle_point(matrix):
    min_for_row = matrix.min(axis=1)
    max_for_col = matrix.max(axis=0)
    if min_for_row.max() == max_for_col.min():
        return True, min_for_row.max()
    else:
        return False


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


data = pandas.read_csv('rules.csv')

discardA = data.iloc[-2][0]
discardB = data.iloc[-1][0]

rules = data[:-2].astype("float64")
rules.index = rules.columns.values

rules.drop(labels=discardA, inplace=True)
rules.drop(columns=discardB, inplace=True)

saddle_point_exist = saddle_point(rules)
if saddle_point_exist:
    print("There is saddle point that amounts: " + str(saddle_point_exist[1]))
    exit(0)
else:
    print("There is no saddle point")

if reduce_dominated(rules):
    print("Reduced dominated rows/columns\n"
          "New matrix:\n" +
          str(rules))
else:
    print("No dominated rows/columns")

minValue = rules.values.min()

if minValue < 0:
    rules += -minValue

x = pulp.LpVariable.dicts("x", rules.columns, lowBound=0)
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

print("\nPlayer A strategy:")
for var in modelA.variables():
    print(var.name + ": " + str(var.varValue * gameValue))

print("\nPlayer B strategy:")
for var in modelB.variables():
    print(var.name + ": " + str(var.varValue * gameValue))

if minValue < 0:
    gameValue -= -minValue

print("\nGame value: ", gameValue)