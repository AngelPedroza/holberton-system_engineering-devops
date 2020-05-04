#!/usr/bin/python3
"""Solve an API"""
if __name__ == "__main__":
    import requests
    import sys
    import json

    user_id = int(sys.argv[1])
    user_info = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                             .format(user_id))

    try:
        user = user_info.json()
        if user_id is user[0].get("id"):
            name_employ = user[0].get("username")
    except:
        print("Not a valid JSON")

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id))

    try:
        tasks_json = tasks.json()
        complete = 0
        task_dic = {}
        task_list = []

        for task in tasks_json:
            task_dic["task"] = task.get("title")
            task_dic["completed"] = task.get("completed")
            task_dic["username"] = name_employ
            task_list.append(task_dic)
    except:
        print("Not a valid JSON")

    id_dic = {}
    id_dic[str(user_id)] = task_list

    with open(str(user_id) + ".json", "w") as f:
        json.dump(id_dic, f)
