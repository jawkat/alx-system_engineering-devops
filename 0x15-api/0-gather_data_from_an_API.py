#!/usr/bin/python3
""" task 0 """
import requests
import sys


def get_employee(employee_id):
    """ comments """
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Emplyee ID must be an integer")
        return

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"

    user_response = requests.get(user_url, timeout=2)
    if user_response.status_code != 200:
        print(f"User ID {employee_id} not found")
        return
    user = user_response.json()
    employee_name = user.get('name')

    todos_url = f"{base_url}/todos?userId={employee_id}"

    todos_response = requests.get(todos_url, timeout=2)
    if todos_response.status_code != 200:
        print("error request")
        return

    todos = todos_response.json()
    total_task = len(todos)

    task_done = [todo for todo in todos if todo.get('completed')]

    nb_task_done = len(task_done)

    print(f"Employee {employee_name} is done withtasks\
        ({nb_task_done}/{total_task}):")
    for task in task_done:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        get_employee(sys.argv[1])
