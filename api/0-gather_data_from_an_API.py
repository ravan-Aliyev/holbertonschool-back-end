#!/usr/bin/python3
"""
Requesting data from rest api
"""
import requests
import sys

if (len(sys.argv) < 2):
    print("Please enter user id")
    sys.exit()

dataUser = requests.get('https://jsonplaceholder.typicode.com/users').json()
dataToDo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

user = next((u for u in dataUser if u['id'] == int(sys.argv[1])), None)

if user is None:
    print("User not found")
    sys.exit(1)

usersTodos = [todo for todo in dataToDo if todo['userId'] == user['id']]

done = sum(1 for todo in usersTodos if todo['completed'])
tasks = len(usersTodos)

print(f"Employee {user['name']} is done with tasks ({done}/{tasks}):")
for task in usersTodos:
    if task['completed']:
        print(f"\t {task['title']}")
