import pandas

data = pandas.read_csv('graph.csv')
data.index += 1

print(data.to_string())
rows = data.index.values
columns = data.columns.values
columns = columns[columns != str(rows[0])]
vertices = [rows[0]]


result = pandas.DataFrame()
while len(columns) > 0:
    nodes = data.loc[vertices, columns]
    min_value = nodes.min().min()

    vertex = nodes[nodes.eq(min_value).any(1)].index.values[0]
    nearest_vertex = nodes.min().idxmin()

    connection = str(vertex) + "-" + str(nearest_vertex)
    result[connection] = [min_value]

    vertices.append(int(nearest_vertex))
    columns = columns[columns != nearest_vertex]

print('\nEdges:\n' +
      result.T.to_string(header=False) +
      '\nMinimal spanning tree:\t' + str(float(result.T.sum().values)))
