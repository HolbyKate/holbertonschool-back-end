#!/usr/bin/python3
"""Gather data from an API"""


import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(api_url)
    todos = response.json()
    employee_name = todos[0].get('name')
    tasks = []
    for todo in todos:
        if todo.get('completed'):
            tasks.append(todo.get('title'))
    print(f'Employee {employee_name} is done with tasks({len(tasks)}/{len(todos)}):')
    for task in tasks:
        print('\t {}'.format(task))


if __name__ == '__main__':
    get_employee_todo_progress(argv[1])
