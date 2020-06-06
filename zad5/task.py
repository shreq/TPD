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
