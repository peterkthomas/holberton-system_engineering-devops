#!/usr/bin/python3

"""
    API Stuff
"""


import requests
import json

root = 'https://jsonplaceholder.typicode.com/'


def request():
    """Performs the Request"""
    response = requests.get(root + 'users/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    users = response.json()

    response = requests.get(root + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    data = {}
    for user in users:
        user_todos = [todo for todo in todos
                      if todo.get('userId') == user.get('id')]
        user_todos = [{'username': user.get('username'),
                       'task': todo.get('title'),
                       'completed': todo.get('completed')}
                      for todo in user_todos]
        data[str(user.get('id'))] = user_todos

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    request()
