#!/usr/bin/python3
"""Solve an API"""
if __name__ == "__main__":
    import requests
    import sys
    import csv

    user_id = int(sys.argv[1])
    user_info = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                             .format(user_id))

    try:
        user = user_info.json()
        if user_id is user[0].get("id"):
            user_name = user[0].get("name")
    except:
        print("Not a valid JSON")

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id))

    tasks_json = tasks.json()

    with open(str(user_id) + ".csv", "w") as data_file:
        csv_writer = csv.writer(data_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks_json:
            id = str(task.get("id"))
            task_status = str(task.get("completed"))
            task_title = str(task.get("title"))
            csv_writer.writerow([id, user_name, task_status, task_title])
