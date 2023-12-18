#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and store TODO list progress in a CSV file"""

import csv
import requests
import sys


def get_employee_progress_csv(employee_ID):
    """
    Retrieve employee information and TODO list progress based on the
    employee ID.
    The data will be save to a file named in format:
        <employee_ID>.csv
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_ID}"
    todos_url = f"{url}/todos?userId={employee_ID}"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if employee_response.status_code == 200:
        employee_name = employee_data.get("username")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write task data to CSV
        for task in todos_data:
            task_status = str(task.get("completed"))
            task_title = task.get("title")
            csv_writer.writerow([employee_id,
                                employee_name,
                                task_status,
                                task_title])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_progress_csv(employee_id)