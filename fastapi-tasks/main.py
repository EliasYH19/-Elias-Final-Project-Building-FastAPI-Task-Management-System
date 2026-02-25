from fastapi import FastAPI, HTTPException
from schema import Task, TaskCreate
import task_controller as controller

app = FastAPI()

@app.get("/tasks", response_model=list[Task])
def get_all_tasks(completed: bool | None = None):
    tasks = controller.load_tasks()
    if completed is not None:
        return [t for t in tasks if t['completed'] == completed]
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    tasks = controller.load_tasks()
    new_id = max([t['id'] for t in tasks], default=0) + 1
    new_task = {"id": new_id, **task.dict(), "completed": False}
    tasks.append(new_task)
    controller.save_tasks(tasks)
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    tasks = controller.load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskCreate):
    tasks = controller.load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t.update(task_update.dict())
            controller.save_tasks(tasks)
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = controller.load_tasks()
    new_list = [t for t in tasks if t['id'] != task_id]
    if len(tasks) == len(new_list):
        raise HTTPException(status_code=404, detail="Task not found")
    controller.save_tasks(new_list)
    return {"message": "Task deleted successfully"}

@app.get("/tasks/stats")
def get_stats():
    tasks = controller.load_tasks()
    total = len(tasks)
    done = len([t for t in tasks if t['completed']])
    return {
        "total": total,
        "completed": done,
        "pending": total - done,
        "percent": (done/total*100) if total > 0 else 0
    }