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

if __name__ == "__main__":
    main()