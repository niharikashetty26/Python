from .task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)
        print(f"Task '{name}' added.")

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_as_completed()
                print(f"Task '{name}' marked as completed.")
                return
        print(f"Task '{name}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(f"Task List: {task}")