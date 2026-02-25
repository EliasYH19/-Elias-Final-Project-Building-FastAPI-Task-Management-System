import json
import os

FILE_NAME = "tasks.txt"

def load_tasks():
    # Reads tasks.txt and returns them as a list of dictionaries
        return []
    tasks = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                tasks.append(json.loads(line))
    return tasks

def save_tasks(tasks):
    # Writes the list of tasks to the file, one JSON object per line
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")