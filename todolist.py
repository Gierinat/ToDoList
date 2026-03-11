from db_handler import get_tasks


menu = """1) Today's tasks
2) Add a task
0) Exit"""


def task_print():
    tasks = get_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Nothing to do!")




def main():
    while True:
        print(menu)
        choice = input()
        if choice == "1":
            print("Today:")
            task_print()
            print()
        if choice == "2":
            pass
        if choice == "0":
            print("Bye!")
            break


if __name__ == "__main__":
    main()