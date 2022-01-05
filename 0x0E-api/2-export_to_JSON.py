#!/usr/bin/python3

"""
    API Stuff
"""


import requests
import sys
import json

root = 'https://jsonplaceholder.typicode.com/'


def request():
    """Performs the Request"""
    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    empid = sys.argv[1]
    try:
        _empid = int(sys.argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    response = requests.get(root + 'users/' + empid)
    if response.status_code == 404:
        return print('User id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user = response.json()

    response = requests.get(root + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    user_todos = [todo for todo in todos
                  if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]

    user_todos = [{'task': todo.get('title'),
                   'completed': todo.get('completed'),
                   'username': user.get('username')}
                  for todo in user_todos]
    data = {empid: user_todos}
    with open(empid + '.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    request()
