class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}, Description: {self.description}, Status: {status}"

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def mark_task_as_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_as_completed()
            print(f"Task {task_number} marked as completed.")
        else:
            print(f"Invalid task number: {task_number}")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.title}' deleted.")
        else:
            print(f"Invalid task number: {task_number}")

    def edit_task(self, task_number, new_title, new_description):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.title = new_title
            task.description = new_description
            print(f"Task {task_number} updated to Title: {new_title}, Description: {new_description}.")
        else:
            print(f"Invalid task number: {task_number}")

# main() y la función de entrada de datos se mantienen sin cambios.



def main():
    manager = ToDoListManager()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Delete a task")
        print("6. Edit a task")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            manager.mark_task_as_completed(task_number)
        elif choice == "4":
            manager.clear_tasks()
        elif choice == "5":
            manager.list_tasks()
            task_number = int(input("Enter the task number to delete: "))
            manager.delete_task(task_number)
        elif choice == "6":
            manager.list_tasks()
            task_number = int(input("Enter the task number to edit: "))
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            manager.edit_task(task_number, new_title, new_description)
        elif choice == "7":
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
