#!/usr/bin/python3
"""Pyhton Script to fetch data from an API"""
import json
import requests

if __name__ == "__main__":
    """Request employee data and represent it"""

    all_url = f"https://jsonplaceholder.typicode.com/users"
    users = requests.get(all_url).json()
    users_id_list = []
    for user in users:
        users_id_list.append(user.get('id'))

    all_dict = {}
    for id in users_id_list:
        url = f"https://jsonplaceholder.typicode.com/users/{id}"
        todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
        user_name = requests.get(url).json().get('username')
        user_id = requests.get(url).json().get('id')
        user_todos = requests.get(todo_url)
        task_list = []
        for task in user_todos.json():
            task_dict = {"username": user_name,
                         "completed": task.get('completed'),
                         "task": task.get('title')}
            task_list.append(task_dict)
        all_dict[user_id] = task_list
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_dict, file)
