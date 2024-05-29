class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = 'completed' if self.completed else 'not completed'
        return f"Task(name={self.name}, description={self.description}, status={status})"