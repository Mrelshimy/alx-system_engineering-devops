#!/usr/bin/python3
"""Pyhton Script to fetch data from an API"""
import requests
import sys

if __name__ == "__main__":
    """Request employee data and represent it"""

    id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    user_name = requests.get(url).json().get('name')
    user_todos = requests.get(todo_url)
    finished_tasks = []
    for task in user_todos.json():
        if task.get('completed') is True:
            finished_tasks.append(task.get('title'))
    print(f"Employee {user_name} is done with tasks\
({len(finished_tasks)}/{len(user_todos.json())}):")
    for item in finished_tasks:
        print(f'\t {item}')
