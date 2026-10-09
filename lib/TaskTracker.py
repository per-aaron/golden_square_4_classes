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
        if task_number > len(self.tasks):
            raise Exception(f"Invalid task number provided, pick a task in this range 1:{len(self.tasks)}.")
        self.tasks.pop(task_number-1)