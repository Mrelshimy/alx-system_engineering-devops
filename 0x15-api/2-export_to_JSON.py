#!/usr/bin/python3
"""Pyhton Script to fetch data from an API"""
import json
import requests
import sys

if __name__ == "__main__":
    """Request employee data and represent it"""

    id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    user_name = requests.get(url).json().get('username')
    user_id = requests.get(url).json().get('id')
    user_todos = requests.get(todo_url)
    task_list = []
    for task in user_todos.json():
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'), "username": user_name}
        task_list.append(task_dict)
    user_dict = {user_id: task_list}
    with open(f'{user_id}.json', 'w') as file:
        json.dump(user_dict, file)
