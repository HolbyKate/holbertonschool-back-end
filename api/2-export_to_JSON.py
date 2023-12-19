#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and store TODO list progress in a JSON file"""

import json
import requests
import sys


def get_employee_progress_json(employee_ID):
    """
    Retrieve employee information and TODO list progress based on the
    employee ID.
    The data will be save to a file named in format:
        <employee_ID>.json
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_ID}"
    todos_url = f"{url}/todos?userId={employee_ID}"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if employee_response.status_code == 200:
        employee_username = employee_data.get("username")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create base dictionary and list to contain tasks
    tasks_dict = {}
    tasks_list = []

    # Fill list with dictionaries in requested format for JSON
    for task in todos_data:
        tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_username
            })

    # Add list to the dictionary
    tasks_dict[str(employee_ID)] = tasks_list

    # Generate filename and dump dictionary into JSON file
    json_filename = f"{employee_ID}.json"
    with open(json_filename, mode="w") as json_file:
        json.dump(tasks_dict, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_progress_json(employee_id)
