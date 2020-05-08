import pandas


def get_cheapest_connection(node, df):
    nodes = df.iloc[node - 1, :]
    return nodes.loc[nodes.eq(nodes.min())]


data = pandas.read_csv('graph.csv').dropna(axis=1, how='all').dropna(how='all')
data.index += 1

print(data.to_string())

result = pandas.DataFrame()
for i in range(1, data.index.size + 1):
    edges = get_cheapest_connection(i, data)
    for j in range(edges.index.size):
        result[str(i) + '-' + edges.index[j]] = [edges[j]]

print('\nEdges:\n' +
      result.T.to_string(header=False) +
      '\nMinimal spanning tree:\t' + str(float(result.T.sum().values)))
