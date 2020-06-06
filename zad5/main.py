from random import randint

import pandas

from processor import Processor
from task import Task

processor = Processor(10)
tasks = [Task(randint(1, 10), randint(1, 10), randint(1, 10)) for i in range(10)]

print(
    "Tasks:\n" + pandas.DataFrame(
        [[task.priority, task.start_time, task.time_to_finish] for task in tasks],
        columns=['priority', 'start_time', 'time_to_finish'],
        index=[task.id for task in tasks]
    ).to_string()
)
print("\nProcessing:")

task = tasks.pop(0)
processor.enqueue(task)
while len(tasks) > 0:
    task = tasks.pop(0)
    processor.process(task.start_time)
    processor.enqueue(task)

processor.process(100)
