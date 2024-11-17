import random
import string
import requests

API_URL = "http://localhost:4567"


def random_string(length=10):
    return "".join(random.choices(string.ascii_letters, k=length))


def create_random_todo():
    title = random_string()
    description = random_string(20)
    data = {"title": title, "description": description}
    response = requests.post(API_URL + "/todos", json=data)
    assert response.status_code == 201, "Failed to create todo"
    return response.json()["id"]
