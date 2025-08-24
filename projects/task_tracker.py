# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

'''
# TASK PROPERTIES
id: A unique identifier for the task
description: A short description of the task
status: The status of the task (todo, in-progress, done)
createdAt: The date and time when the task was created
updatedAt: The date and time when the task was last updated
'''
import json

with open("task_tracker.json", "+r") as file:
    # loads entire task list
    task_list = json.load(file)["tasks"]

program_end = False


def add_new_task():
    print("===== ADD A NEW TASK =====")


def update_task():
    print("===== UPDATE A TASK =====")


def delete_task():
    print("===== DELETE A TASK =====")


def list_tasks():
    def list_all_tasks():
        print(task_list)
    print("===== CHOOSE FROM THE FOLLOWING =====")
    print("1. List all tasks")
    print("2. List all tasks that are done")
    print("3. List all tasks that are not done")
    print("4. List all tasks that are in progress")
    user_input = input("Option (1/2/3/4): ").strip()

    match user_input:
        case "1":
            list_all_tasks()
        case _:
            print("This is not a valid option")


def main(program_end):
    while program_end == False:
        user_input = input("task-cli (add/update/delete/list): ").strip()

        match user_input:
            case "add":
                add_new_task()
            case "update":
                update_task()
            case "delete":
                delete_task()
            case "list":
                list_tasks()
            case "exit":
                program_end = True
            case "end":
                program_end = True
            case _:
                print(f"This is not a valid input.")

        # continue


if __name__ == "__main__":
    main(program_end)
