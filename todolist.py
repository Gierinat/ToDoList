from db_handler import get_tasks, Task, save_task


menu = """
1) Today's tasks
2) Add a task
0) Exit"""


def task_print():
    tasks = get_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.task}")
    else:
        print("Nothing to do!")


def add_task():
    print("\nEnter a task")
    text = input()
    task = Task(task=text)
    save_task(task)
    print('The task has been added!')


def main():
    while True:
        print(menu)
        choice = input()
        if choice == "1":
            print("\nToday:")
            task_print()
            print()
        if choice == "2":
            add_task()
        if choice == "0" or not choice:
            print("\nBye!")
            break


if __name__ == "__main__":
    main()