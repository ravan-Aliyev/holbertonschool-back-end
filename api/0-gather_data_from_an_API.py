#!/usr/bin/python3
"""
Requesting data from rest api
"""
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

    done = sum(1 for todo in userTodo if todo['completed'])
    tasks = len(userTodo)

    print("Employee {0} is done with tasks ({1}/{2}):"
          .format(user['name'], done, tasks))

    for task in userTodo:
        if task['completed']:
            print(" \t{0}".format(task['title']))
