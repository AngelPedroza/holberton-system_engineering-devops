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

    task_dic = {}
    task_list = []
    id_dic = {}

    for user in users:
        name_employ = user.get("username")
        for task in tasks_json:
            if task.get("userId") is user.get("id"):
                task_dic["username"] = name_employ
                task_dic["task"] = task.get("title")
                task_dic["completed"] = task.get("completed")
                task_list.append(task_dic.copy())
        id_dic[str(user.get("id"))] = task_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(id_dic, f)
