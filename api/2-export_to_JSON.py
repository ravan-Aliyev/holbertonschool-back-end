#!/usr/bin/python3
"""
Requesting data from rest api
"""
import json
import requests
import sys

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please enter user id")
        sys.exit()

    link = 'https://jsonplaceholder.typicode.com'

    user = requests.get('{0}/users/{1}'
                        .format(link, sys.argv[1])).json()
    userTodo = requests.get('{0}/todos?{1}={2}'
                            .format(link, "userId", sys.argv[1])).json()

    tasksArr = []

    for data in userTodo:
        obj = {"task": data['title'], "completed": data['completed'],
               "username": user['username']}
        tasksArr.append(obj)

    filename = f"{user['id']}.json"

    with open(filename, 'w', encoding="utf-8") as file:
        serialized = {user['id']: tasksArr}
        json.dump(serialized, file)
