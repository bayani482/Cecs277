"""
Lab 13 - iterator

Student 1: Brian Bayani
Student 2: Javier Jacobo
Date: November 18th, 2025

This program manages a task list using an iterator.
"""

import check_input
from tasklist import TaskList


def main_menu():
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")
    choice = check_input.get_int_range("Enter a choice: ", 1, 6)
    return choice


def get_date():
    print("Enter due date:")
    month = check_input.get_int_range("Enter month: ", 1, 12)
    day = check_input.get_int_range("Enter day: ", 1, 31)
    year = check_input.get_int_range("Enter year: ", 2000, 2100)
    month_str = f"{month:02d}"
    day_str = f"{day:02d}"
    date_str = f"{month_str}/{day_str}/{year}"
    return date_str


def get_time():
    print("Enter time:")
    hour = check_input.get_int_range("Enter hour: ", 0, 23)
    minute = check_input.get_int_range("Enter minute: ", 0, 59)

    time_str = f"{hour:02d}:{minute:02d}"
    return time_str


def main():
    task_list = TaskList()

    while True:
        print("\n-Tasklist-")
        print(f"Tasks to complete: {len(task_list)}")
        choice = main_menu()

        match choice:
            case 1:
                print("Current Task is")
                t = task_list.get_current_task()
                if t is None:
                    print("no tasks")
                else:
                    print(t)

            case 2:
                print("Tasks")
                if len(task_list) == 0:
                    print("No tasks in the list.")
                else:
                    for i, t in enumerate(task_list, start=1):
                        print(f"{i}. {t}")

            case 3:
                t = task_list.get_current_task()
                if t is None:
                    print("No tasks to complete.")
                else:
                    print("Marking current task as complete:")
                    print(t)
                    task_list.mark_complete()

                    new = task_list.get_current_task()
                    if new is None:
                        print("All tasks are now complete.")
                    else:
                        print("New current task is:")
                        print(new)

            case 4:
                desc = input("Enter a task: ")
                date = get_date()
                time = get_time()
                task_list.add_task(desc, date, time)

            case 5:
                print("\Search by Date")
                date = get_date()
                matches = []

                for t in task_list:
                    if t.date == date:
                        matches.append(t)

                if not matches:
                    print("No tasks due on that date.")
                else:
                    print(f"Tasks due on {date}:")
                    for i, t in enumerate(matches, start=1):
                        print(f"{i}. {t}")

            case 6:
                print("\nSaving list...")
                task_list.save_file()
                break

if __name__ == "__main__":
    main()
