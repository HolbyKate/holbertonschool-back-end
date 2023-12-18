#!/usr/bin/python3
"""Gather data from an API"""


import requests
import sys

if len(sys.argv) == 2:
    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()
    done_tasks = []
    for task in todo:
        if task.get('completed') is True:
            done_tasks.append(task)
    print('Employee {} is done with tasks({}/{}):'
            .format(user.get('name'), len(done_tasks), len(todo)))
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
