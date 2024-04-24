#!/usr/bin/python3
"""
Requesting data from rest api
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users').json()

    username = {}

    for user in users:
        username[user['id']] = user['username']

    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos').json()

    with open("todo_all_employees.json", 'w') as file:
        tasks_by_user = {}

        for new_task in todos:
            user_id = new_task['userId']

            if user_id not in tasks_by_user:
                tasks_by_user[user_id] = []

            new_task_title = new_task['title']
            new_task_status = new_task['completed']
            user_id = new_task['userId']
            task_data = {
                "username": username[user_id],
                "task": new_task_title,
                "completed": new_task_status
                }
            tasks_by_user[user_id].append(task_data)
        json.dump(tasks_by_user, file)
