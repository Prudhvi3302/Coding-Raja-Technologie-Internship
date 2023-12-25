import json

class Task:
    def __init__(self, description, priority, due_date, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

# Functions for task management
def add_task_manually(tasks):
    description = input("Enter task description: ")
    priority = input("Enter task priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    task = Task(description, priority, due_date)
    add_task(tasks, task)

# ... (rest of the functions remain the same)

# Example usage
tasks_file = 'tasks.json'
tasks = load_task(tasks_file)

# Manually add tasks
num_tasks = int(input("Enter the number of tasks to add: "))
for _ in range(num_tasks):
    add_task_manually(tasks)

# Display tasks
display_tasks(tasks)

# Mark a task as completed
index_to_complete = int(input("Enter the index of the task to mark as completed: "))
mark_as_completed(tasks, index_to_complete - 1)  # Adjusting for 0-based indexing

# Remove a task
index_to_remove = int(input("Enter the index of the task to remove: "))
remove_task(tasks, index_to_remove - 1)  # Adjusting for 0-based indexing

# Save tasks
save_tasks(tasks_file, tasks)
