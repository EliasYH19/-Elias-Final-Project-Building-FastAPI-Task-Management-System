import json
import os

FILE_NAME = "tasks.txt"

def load_tasks():
    # 1. Check if file exists. If not, return empty list immediately.
    if not os.path.exists(FILE_NAME):
        return []

    # 2. Everything below this is lined up at the same level
    tasks = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                tasks.append(json.loads(line))
    
    # 3. Final return happens only after the file is fully read
    return tasks

def save_tasks(tasks):
    # Writes the list of tasks to the file, one JSON object per line
    with open(FILE_NAME, "w") as file:
        for task in tasks:

            file.write(json.dumps(task) + "\n")
