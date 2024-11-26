import random
import string
import requests

API_URL = "http://localhost:4567"

# Helper to generate random strings
def random_string(length=10):
    return "".join(random.choices(string.ascii_letters, k=length))

# Create a random todo
def create_random_todo():
    title = random_string()
    description = random_string(20)
    data = {"title": title, "description": description}
    response = requests.post(API_URL + "/todos", json=data)
    assert response.status_code == 201, f"Failed to create todo: {response.text}"
    return response.json()["id"]

# Create a random project
def create_random_project():
    title = random_string()
    description = random_string(20)
    data = {"title": title, "description": description}
    response = requests.post(API_URL + "/projects", json=data)
    assert response.status_code == 201, f"Failed to create project: {response.text}"
    return response.json()["id"]

# Update a todo
def update_todo(todo_id):
    update_data = {"title": "Updated Todo Title", "description": "Updated Todo Description"}
    response = requests.put(f"{API_URL}/todos/{todo_id}", json=update_data)
    assert response.status_code in [200, 204], f"Failed to update todo {todo_id}: {response.text}"

# Update a project
def update_project(project_id):
    update_data = {"title": "Updated Project Title", "description": "Updated Project Description"}
    response = requests.put(f"{API_URL}/projects/{project_id}", json=update_data)
    assert response.status_code in [200, 204], f"Failed to update project {project_id}: {response.text}"

# Delete a todo
def delete_todo(todo_id):
    response = requests.delete(f"{API_URL}/todos/{todo_id}")
    assert response.status_code in [200, 204], f"Failed to delete todo {todo_id}: {response.text}"

# Delete a project
def delete_project(project_id):
    response = requests.delete(f"{API_URL}/projects/{project_id}")
    assert response.status_code in [200, 204], f"Failed to delete project {project_id}: {response.text}"
