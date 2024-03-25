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
    user_name = requests.get(url).json().get('name')
    user_id = requests.get(url).json().get('id')
    user_todos = requests.get(todo_url)
    with open(f'new.csv', 'w') as file:
        for task in user_todos.json():
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, user_name, task.get('completed'),
                               task.get('title')))
