tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully.")


def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task has been removed.")
    else:
        print("Task not found.")

def view_tasks():
    print("Tasks:")
    if len(tasks) == 0:
        print("No tasks found")
    else:
        for task in tasks:
            print(task)

def menu():
    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter 1-4: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            
menu()         