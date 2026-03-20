from datetime import datetime

from db_handler import get_tasks, Task, save_task


menu = """
1) Today's tasks
2) Week's tasks
3) All tasks
4) Add a task 
0) Exit"""


def task_print(mode='all'):
    tasks = get_tasks()

    if tasks and mode == 'all':
        for i, task in enumerate(tasks, 1):
            day = task.deadline.strftime('%d')
            month = task.deadline.strftime('%b')
            print(f"{i}. {task.task}. {day} {month}")
    else:
        print("Nothing to do!")


def add_task():
    print("\nEnter a task")
    text = input()

    print("Enter a deadline")
    deadline = input()
    deadline_date = datetime.strptime(deadline, "%Y-%m-%d")

    task = Task(task=text, deadline=deadline_date)
    save_task(task)
    print('The task has been added!')


def main():
    today = datetime.today()
    while True:
        print(menu)
        choice = input()

        if choice == "1":
            print(f"\nToday {today.strftime('%d')} {today.strftime('%b')}:")
            task_print('today')

        if choice == "3":
            print("All tasks:")
            task_print()

        if choice == "4":
            add_task()

        if choice == "0" or not choice:
            print("\nBye!")
            break


if __name__ == "__main__":
    main()