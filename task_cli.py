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

# main menu with cli (sys.argv)
def main():
    if len(sys.argv) < 2:
        print("Cara pakai: python task_cli.py [add/list] [deskripsi]")
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
    else:
        print("Unknown command!")

if __name__ == "__main__":
    main()