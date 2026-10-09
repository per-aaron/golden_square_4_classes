class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def show(self):
        if not bool(self.tasks):
            raise Exception("No task set.")
        return list(enumerate(self.tasks, start=1))

    def complete(self, task_number):
        self.tasks.pop(task_number-1)