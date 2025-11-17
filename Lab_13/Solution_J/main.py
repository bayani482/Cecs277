"""

Student 1: Javier Jacobo
Student 2: Bryan Bayani

Lab 13 - Iterator

Description:
An awesome task manager application.

"""

from tasklist import Tasklist
import check_input

def main_menu(tasklist):
    print("--Tasklist--")
    print(f"""
Tasks to complete: {len(tasklist)}
1. Display current task
2. Display all tasks
3. Mark current task as complete
4. Add new task
5. Search by date
6. Save and quit
""")
    user_choice = check_input.get_int_range("Enter choice (1-6): ", 1, 6)
    return user_choice

def get_date():
    print("Enter date:")
    month = check_input.get_int_range("Enter month: ", 1, 12)
    day = check_input.get_int_range("Enter day: ", 1, 31)
    year = check_input.get_int_range("Enter year: ", 2000, 2100)
    date = f"{month:02}/{day:02}/{year}"
    return date

def get_time():
    print("Enter time:")
    hour = check_input.get_int_range("Enter hour: ", 0, 23)
    minute = check_input.get_int_range("Enter minute: ", 0, 59)
    time = f"{hour:02}:{minute:02}"
    return time

def main():
    tasklist = Tasklist()
    user_choice = 0
    
    while user_choice != 6:
        user_choice = main_menu(tasklist)
        match user_choice:
            case 1:
                print(tasklist.get_current_task())
            case 2:
                for i, task in enumerate(tasklist):
                    print(f"{i + 1}.\t{task}")
            case 3:
                print("Marking current task as complete:")
                print(tasklist.get_current_task())
                tasklist.mark_complete()
                print("New current task:")
                print(tasklist.get_current_task())
            case 4:
                desc = input("Enter a task: ")
                date = get_date()
                time = get_time()
                tasklist.add_task(desc, date, time)                


if __name__ == "__main__":
    main()
