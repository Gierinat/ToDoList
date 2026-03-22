from datetime import datetime, date, timedelta

from db_handler import get_tasks, Task, save_task


menu = """
1) Today's tasks
2) Week's tasks
3) All tasks
4) Add a task
0) Exit
"""


def task_print(mode='all'):
    tasks = get_tasks(mode)

    if tasks and mode == 'all':
        for i, task in enumerate(tasks, 1):
            day = task.deadline.strftime('%d')
            month = task.deadline.strftime('%b')
            print(f"{i}. {task.task}. {day} {month}")

    elif mode == 'week':
        week_dict = {date.today() + timedelta(days=i) : [] for i in range(7)}
        for task in tasks:
            week_dict[task.deadline].append(task.task)

        for task_date, tasks in week_dict.items():
            day_name = task_date.strftime("%A")
            day = task_date.strftime('%d')
            month = task_date.strftime('%b')

            print(f"{day_name} {day} {month}:")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("Nothing to do!")
            print()

    elif tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.task}")

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
            print()

        if choice == "2":
            task_print('week')
            print()

        if choice == "3":
            print("All tasks:")
            task_print()
            print()

        if choice == "4":
            add_task()
            print()

        if choice == "0" or not choice:
            print("\nBye!")
            break


if __name__ == "__main__":
    main()