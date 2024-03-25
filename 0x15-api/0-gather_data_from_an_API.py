#!/usr/bin/python3
"""Pyhton Script to fetch data from an API"""
import requests
import sys

if __name__ == "__main__":
    """Request employee data and represent it"""

    user_name = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}").json().get('name')
    user_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos")
    finished_tasks=[]
    for task in user_todos.json():
        if task.get('completed') == True :
            finished_tasks.append(task.get('title'))
    print(f"Employee {user_name} is done with tasks({len(finished_tasks)}/{len(user_todos.json())}):")
    for item in finished_tasks:
        print(f'\t{item}')
    