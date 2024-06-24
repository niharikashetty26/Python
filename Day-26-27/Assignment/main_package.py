from TaskManager import TaskManager, Task

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task_manager.add_task(name, description)
        elif choice == '2':
            name = input("Enter task name to complete: ")
            task_manager.complete_task(name)
        elif choice == '3':
            task_manager.list_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose again.")

main()