"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    """A task stored by the API."""

    title: str
    completed: bool = False


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a short message describing the API."""
    return {"message": "Task API is running"}


# TODO: Add GET /tasks to return all tasks.


# TODO: Add POST /tasks to create a task.
# The route should assign the next available integer ID and return the new task.


# TODO: Add GET /tasks/{task_id} to return one task or a 404 response.


# TODO: Add PUT /tasks/{task_id} to replace an existing task or return a 404 response.


# TODO: Add DELETE /tasks/{task_id} to remove an existing task or return a 404 response.
