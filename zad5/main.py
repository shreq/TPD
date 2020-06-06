import heapq as hq


class Task:
    ID = 1

    def __init__(self, priority, start_time, time_to_finish):
        self.priority = priority
        self.id = Task.ID
        Task.ID += 1
        self.start_time = start_time
        self.time_to_finish = time_to_finish

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return 'Task_' + str(self.id)

    def process(self, time):
        if self.time_to_finish > time:
            self.time_to_finish -= time
            return -1
        else:
            self.finish()
            return time - self.time_to_finish

    def finish(self):
        print(str(self) + ' finished')

    def switch(self, other):
        print(str(self) + ' switched to ' + str(other))


class Processor:

    def __init__(self, max_priority):
        self.queue = []
        self.elapsed_time = 0
        self.current_task = None
        self.max_priority = max_priority

    def process(self, time):
        if self.current_task is not None:
            time_left = self.current_task.process(time)
            if time_left > 0:
                self.elapsed_time += (time - time_left)
                if len(self.queue) > 0:
                    self.current_task = self.dequeue()
                    self.process(time_left)
                else:
                    self.current_task = None
                    self.finish()
            elif time_left == 0:
                self.elapsed_time += time
                if len(self.queue) > 0:
                    self.current_task = self.dequeue()
                else:
                    self.current_task = None
                    self.finish()
            else:
                self.elapsed_time += time

    def dequeue(self):
        return hq.heappop(self.queue)[1]

    def enqueue(self, task):
        if self.current_task is not None:
            if self.current_task.priority < task.priority:
                self.current_task.switch(task)
                hq.heappush(self.queue, (self.max_priority - self.current_task.priority, self.current_task))
                self.current_task = task
            else:
                hq.heappush(self.queue, (self.max_priority - task.priority, task))
        else:
            self.current_task = task

    def finish(self):
        print("Processing finished after " + str(self.elapsed_time) + " seconds")
        self.elapsed_time = 0


t1 = Task(1, 2, 4)
t2 = Task(2, 2, 4)
t3 = Task(3, 4, 4)
t4 = Task(4, 2, 4)
t5 = Task(5, 2, 4)
list = [t1, t2, t3, t4, t5]

p = Processor(10)

task = list.pop(0)
p.enqueue(task)
while len(list) > 0:
    task = list.pop(0)
    p.process(task.start_time)
    p.enqueue(task)

p.process(100)



