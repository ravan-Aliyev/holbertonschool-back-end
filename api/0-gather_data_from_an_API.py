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

    user = requests.get(f'https://jsonplaceholder.typicode.com/users/\
                        {sys.argv[1]}').json()
    userTodo = requests.get(f'https://jsonplaceholder.typicode.com/todos\
                            ?userId={sys.argv[1]}').json()

    done = sum(1 for todo in userTodo if todo['completed'])
    tasks = len(userTodo)

    print(f"Employee {user['name']} is done with tasks ({done}/{tasks}):")
    for task in userTodo:
        if task['completed']:
            print(f"\t {task['title']}")
