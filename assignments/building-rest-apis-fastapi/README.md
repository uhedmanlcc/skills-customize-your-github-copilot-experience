# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining routes, modeling request data, and returning appropriate HTTP responses. You will create an in-memory task service that clients can use to list, create, update, and delete tasks.

## 📝 Tasks

### 🛠️ Create API Routes and Task Models

#### Description
Set up the FastAPI application and define the data models needed for a task list. Add routes that allow clients to view all tasks and create a new task.

#### Requirements
Completed program should:

- Create a FastAPI application in `starter-code.py`
- Define a Pydantic model with a required task `title` and an optional `completed` value that defaults to `False`
- Implement `GET /tasks` to return all tasks
- Implement `POST /tasks` to add a task and return the created task with a unique integer ID
- Return a `201 Created` response when a task is added


### 🛠️ Implement CRUD Behavior and Error Handling

#### Description
Complete the remaining task routes and make the API respond clearly when a requested task does not exist.

#### Requirements
Completed program should:

- Implement `GET /tasks/{task_id}` to return one task
- Implement `PUT /tasks/{task_id}` to replace a task's title and completion status
- Implement `DELETE /tasks/{task_id}` and return a successful response when deletion occurs
- Return a `404 Not Found` response for an unknown task ID
- Validate request bodies using Pydantic models instead of reading raw JSON
- Run the API with Uvicorn and verify the endpoints using the automatically generated documentation at `/docs`
