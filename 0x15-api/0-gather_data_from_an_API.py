#!/usr/bin/python3
"""Solve an API"""
if __name__ == "__main__":
    import requests
    import sys

    user_id = int(sys.argv[1])
    user_info = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                             .format(user_id))

    try:
        user = user_info.json()
        if user_id is user[0].get("id"):
            name_employ = user[0].get("name")
    except:
        print("Not a valid JSON")

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id))

    try:
        tasks_json = tasks.json()
        complete = 0
        task_title = []

        for task in tasks_json:
            if task.get("completed") is True:
                complete += 1
                task_title.append(task.get("title"))
    except:
        print("Not a valid JSON")

    print("Employee {} is done with tasks({}/{}):"
          .format(name_employ, complete, len(tasks_json)))
    for title in task_title:
        print("\t {}".format(title))
