import json
import os

LOCAL_TASK_FILE = os.path.join(os.getcwd(), "tasks_tasks.json")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def show_tasks():
    return load_tasks()

def load_tasks():
    if not os.path.exists(LOCAL_TASK_FILE):
        return []
    with open(LOCAL_TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(LOCAL_TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
