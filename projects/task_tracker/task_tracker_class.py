import json
from colorist import Color, BgColor
from tasks_class import Task
'''
# TASK PROPERTIES
id: A unique identifier for the task
description: A short description of the task
status: The status of the task (todo, in-progress, done)
createdAt: The date and time when the task was created
updatedAt: The date and time when the task was last updated
'''


class TaskTracker:
    cool = 2

    def __init__(self, file_path="task_tracker.json"):
        self.file_path = file_path
        self.task_list = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, "+r") as file:
                # loads entire task list
                return json.load(file)["tasks"]
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "Error loading Tasks": [FileNotFoundError, json.JSONDecodeError]
            }

    def write_task_file(self):
        print()

    def add_new_task(self):
        print("===== ADD A NEW TASK =====")

    def update_task(self):
        print("===== UPDATE A TASK =====")

    def delete_task(self):
        print("===== DELETE A TASK =====")

    def list_tasks(self):
        back = False
        while back == False:
            def list_all_tasks():
                for task in self.task_list:
                    print(f"{BgColor.BLACK}Task {task['id']}: ")
                    print(f"\t '{task['description']}' ")
                    match task['status']:
                        case "done":
                            print(
                                f"\t Status: {Color.GREEN}{task['status']}{Color.OFF}{BgColor.BLACK}")
                        case "todo":
                            print(
                                f"\t Status: {Color.RED}{task['status']}{Color.OFF}{BgColor.BLACK}")
                        case "in-progress":
                            print(
                                f"\t Status: {Color.YELLOW}{task['status']}{Color.OFF}{BgColor.BLACK}")
                    print(f"\t Created At: {task['createdAt']} {BgColor.OFF}")

            def list_done_tasks():
                for task in self.task_list:
                    if (task["status"] == "done"):
                        print(f"{BgColor.BLACK}Task {task['id']}: ")
                        print(f"\t '{task['description']}' ")
                        print(
                            f"\t Status: {Color.GREEN}{task['status']}{Color.OFF}{BgColor.BLACK}")
                        print(f"\t Created At: {task['createdAt']} {BgColor.OFF}")
                    else:
                        continue

            def list_incomplete_tasks():
                for task in self.task_list:
                    if (task["status"] == "todo"):
                        print(f"{BgColor.BLACK}Task {task['id']}: ")
                        print(f"\t '{task['description']}' ")
                        print(
                            f"\t Status: {Color.RED}{task['status']}{Color.OFF}{BgColor.BLACK}")
                        print(f"\t Created At: {task['createdAt']} {BgColor.OFF}")
                    else:
                        continue

            def list_in_progress_tasks():
                for task in self.task_list:
                    if (task["status"] == "todo"):
                        print(f"{BgColor.BLACK}Task {task['id']}: ")
                        print(f"\t '{task['description']}' ")
                        print(
                            f"\t Status: {Color.YELLOW}{task['status']}{Color.OFF}{BgColor.BLACK}")
                        print(f"\t Created At: {task['createdAt']} {BgColor.OFF}")
                    else:
                        continue

            print("===== CHOOSE FROM THE FOLLOWING =====")
            print("1. List all tasks")
            print("2. List all tasks that are done")
            print("3. List all tasks that are not done")
            print("4. List all tasks that are in progress")
            print("<== back")
            user_input = input("Option (1/2/3/4/back): ").strip()
            print("======================================")

            match user_input:
                case "1":
                    list_all_tasks()
                case "2":
                    list_done_tasks()
                case "3":
                    list_incomplete_tasks()
                case "4":
                    list_in_progress_tasks()
                case "5":
                    back = True
                case "back":
                    back = True
                case _:
                    print("This is not a valid option")
