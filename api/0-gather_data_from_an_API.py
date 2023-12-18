#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and display TODO list progress."""
import requests
import sys


def to_do(employee_ID):
    """
    Retrieve employee information and TODO
    list progress based on the employee ID.

    Args:
        employee_ID (int): The ID of the employee.

    Returns:
        None

    Prints:
        Displays the employee's TODO list progress.
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_id}"
    todos_url = f"{url}/todos?userId={employee_id}"

    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Error fetching employee data. Status code:
              {employee_response.status_code}")
        sys.exit(1)

    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error fetching TODO list data. Status code:
              {todos_response.status_code}")
        sys.exit(1)

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    print(f"Employee {employee_name} is done with tasks
          ({completed_tasks}/{total_tasks}): ")

    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    to_do(employee_id)
