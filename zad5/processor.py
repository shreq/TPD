import heapq as hq


class Processor:

    def __init__(self, max_priority):
        self.queue = []
        self.elapsed_time = 0
        self.current_task = None
        self.max_priority = max_priority

    def process(self, time):
        if self.current_task is not None:
            time_left = self.current_task.process(time)
            if time_left >= 0:
                self.elapsed_time += time - time_left
                self.current_task = self.dequeue()
                self.process(time_left)
            else:
                self.elapsed_time += time
        else:
            self.finish()

    def dequeue(self):
        if len(self.queue) > 0:
            return hq.heappop(self.queue)[1]
        else:
            return None

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
