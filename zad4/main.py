import pandas
from collections import namedtuple

Path = namedtuple('Path', 'name steps profit')

data = pandas.read_csv('decisions.csv')
data.index = data['decision'].values
data.drop('decision', axis=1, inplace=True)

stages = {
    stage: data.loc[data['stage'].eq(stage)].drop('stage', axis=1)
    for stage in data['stage'].unique()
}
data = None
paths = [
    Path(name, [start, end], profit)
    for name, (start, end, profit) in stages[max(stages.keys())].iterrows()
]

print('\n'.join(map(str, ['Stage %s:\n%s\n' % item for item in stages.items()])))

for stage_number, stage_data in sorted(list(stages.items()), key=lambda item: item[0], reverse=True)[1:]:
    for name, (start, end, profit) in stage_data.iterrows():
        for path in [path for path in paths if path.steps[0] == end]:
            paths.append(
                Path(name + path.name, [start] + path.steps, profit + path.profit)
            )

most_profitable = [path for path in paths if path.profit == max([path.profit for path in paths])]

print(
    ('Paths' if len(most_profitable) > 1 else 'Path') +
    f' resulting in the highest ({most_profitable[0].profit}) profit:\n' +
    '\n'.join(
        ''.join(
            '%s' % '-'.join(map(str, steps)) for steps in [path.steps]
        ) + ' ' + path.name for path in most_profitable
    )
)
