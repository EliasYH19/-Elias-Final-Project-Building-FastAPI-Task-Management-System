from pydantic import BaseModel

# What a task looks like when saved/retrieved
class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False

# What is required when a user creates a new task
class TaskCreate(BaseModel):
    title: str
    description: str | None = None