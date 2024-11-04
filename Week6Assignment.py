import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

# Load tasks from the JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    status = "pending"
    tasks.append({"description": description, "status": status})
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['description']} - {task['status']}")
    print()

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to update: ")) - 1
        if task_id < 0 or task_id >= len(tasks):
            raise IndexError
        new_description = input("Enter new task description (leave blank to keep current): ")
        new_status = input("Enter new task status (pending/completed, leave blank to keep current): ")
        if new_description:
            tasks[task_id]['description'] = new_description
        if new_status in ["pending", "completed"]:
            tasks[task_id]['status'] = new_status
        save_tasks(tasks)
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid task ID. Please try again.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: ")) - 1
        if task_id < 0 or task_id >= len(tasks):
            raise IndexError
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task ID. Please try again.")

# Main program loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
