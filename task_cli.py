import sys
import json
from datetime import datetime
import os

FILE_NAME = 'tasks.json'

# db code
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        return json.dump(tasks, file, indent=4)

# feature
def add_task(description):
    tasks = load_tasks()
    new_id = 1 if len(tasks) == 0 else tasks[-1]['id'] + 1
    now = datetime.now().isoformat()

    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createAt': now,
        'updateAt': now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("There are no tasks yet. Please add a new task!")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - Status: {task['status']}")

def update_task(task_id, new_description):
    tasks = load_tasks()
    isFound = False

    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updateAt'] = datetime.now().isoformat()
            isFound = True
            break

    if isFound:
        save_tasks(tasks)
        print(f"Task (ID: {task_id}) updated successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found!")

# main menu with cli (sys.argv)
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py [add/list] [description, use a string!]")
        return
    command = sys.argv[1]
    if command == 'add':
        if len(sys.argv) < 3:
            print("Error: Enter the task description!")
            return
        description = sys.argv[2]
        add_task(description)
    elif command == 'list':
        list_tasks()
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: python task_cli.py update [id] [new_description, use a string!]")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be a number!")
            return
        new_description = sys.argv[3]
        update_task(task_id, new_description)
    else:
        print("Unknown command!")

if __name__ == "__main__":
    main()

#  JANGAN LUPA RETURN!