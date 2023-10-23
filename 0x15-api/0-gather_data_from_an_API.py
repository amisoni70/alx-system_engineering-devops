#!/usr/bin/python3
"""A script that returns the to-do list progress for
a given employees's ID
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    tasks_done = [t for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), len(tasks_done), len(todos)))
    [print("\t {}".format(c.get("title"))) for c in tasks_done]
