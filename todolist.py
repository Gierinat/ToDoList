tasks = ["Do yoga", "Make a breakfast", "Learn the basics of SQL", "Learn about ORM"]


def task_print(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}) {task}")


def main():
    print("Today:")
    task_print(tasks)


if __name__ == "__main__":
    main()