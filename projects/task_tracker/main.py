from task_tracker_class import TaskTracker
import time
program_end = False


def main(program_end, test):
    tk = TaskTracker()
    
    while program_end == False:
        if test:
            user_input = test.strip()
            print(f"task-cli (add/update/delete/list/end): {user_input}")
            time.sleep(0.5)
        else:
            user_input = input("task-cli (add/update/delete/list/end): ").strip()
        match user_input:
            case "add":
                tk.add_new_task()
            case "update":
                tk.update_task()
            case "delete":
                tk.delete_task()
            case "list":
                tk.list_tasks()
            case "exit":
                program_end = True
            case "end":
                program_end = True
            case _:
                print(f"This is not a valid input.")


if __name__ == "__main__":
    main(program_end, "list")
