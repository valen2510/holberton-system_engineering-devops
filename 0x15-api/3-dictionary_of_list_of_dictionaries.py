#!/usr/bin/python3
"""Using what you did in the task #0,
    extend your Python script to export data in the JSON format.
"""

from sys import argv
import json
import requests


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/users/'
    response_users = requests.get(url)
    all_users = {}
    for user in response_users.json():
        userId = str(user['id'])
        response_tasks = requests.get(url + userId + '/todos/')
        tasks_list = []
        for tasks in response_tasks.json():
            tasks_list.append({"username": user['username'],
                               "task": tasks['title'],
                               "completed": tasks['completed']})
        all_users[userId] = tasks_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_users, json_file)
