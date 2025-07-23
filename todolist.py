todo_list = {}

while True:
    print("")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        date = input("Enter date (month-date): ")
        task = input("Enter the task: ")
        if date in todo_list:
            todo_list[date].append(task)
        else:
            todo_list[date] = [task]
        print("Task added")

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks in the list")
        else:
            for date in todo_list:
                print("")
                print("Date: " + date)
                tasks = todo_list[date]
                for i in range(len(tasks)):
                    print(str(i + 1) + ". " + tasks[i])

    elif choice == "3":
        date = input("Enter the date (month-date): ")
        if date in todo_list:
            tasks = todo_list[date]
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])
            num = input("Enter task number to remove: ")

            num = int(num)

            task_index = num - 1

            task_to_remove = tasks[task_index]
            print("Removed: " + task_to_remove)
            del tasks[task_index]
            if len(tasks) == 0:
                del todo_list[date]
        else:
            print("No tasks on that date.")

    elif choice == "4":
        print("Bye")
        break

    else:
        print("Please choose a number from the menu.")
