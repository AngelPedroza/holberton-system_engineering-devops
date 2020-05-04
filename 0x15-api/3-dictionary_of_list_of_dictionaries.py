#!/usr/bin/python3
"""Solve an API"""
if __name__ == "__main__":
    import requests
    import sys
    import json

    user_info = requests.get('https://jsonplaceholder.typicode.com/users')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')

    try:
        tasks_json = tasks.json()
        users = user_info.json()
    except:
        print("Not a valid JSON")

    final = {}
    user_names = {}

    for user in users:
        name = user.get("username")
        user_id = user.get("id")
        final[user_id] = []
        user_names[user_id] = name 

    for task in tasks_json:
        user_id = task.get("userId")
        status = task.get("completed")
        title = task.get("title")
        task_dic = {
            "username": user_names.get(user_id).
            "task": title,
            "completed": status
        }

        if final.get(user_id) is not None:
            final.get(user_id).append(task_dic.copy())

    with open("todo_all_employees.json", "w", newline="") as f:
        json.dump(final, f)
