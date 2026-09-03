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


if __name__ == "__main__":
    main()