# Taskify

# This is a minimal to-do-list app made using Python

import tabulate
import pandas as pd

def main():
    call()

def call():
    global data

    x = input("Do you wish to continue? (Y/N): \n").strip().lower()

    if x == "n":
        print("Thank you for using the app")
        return

    print("------")
    print("1 - View Tasks")
    print("2 - Update Existing Tasks")
    print("3 - Add new Task")
    print("4 - Reset to-do")
    print("5 - Mark task as completed")
    print("6 - Export the to-do to a CSV")
    print("7 - Exit")
    print("------")

    a = int(input("\nPlease enter your choice: \n"))
    if a == 1:
        view()
    elif a == 2:
        view()
        update_id = int(input("Enter the ID of the task you want to update:\n"))
        if update_id not in data[0]:
            print("ID not found!")
            call()
        else:
            task = input("Please Enter the task:\n")
        data = update(data, update_id, task)
    elif a == 3:
        task = input("Enter the task:\n")
        data = add(data, task)
        view()
    elif a == 4:
        c = input("Are you sure you want to reset?(Y/N):\n").strip().lower()
        if c == "y":
            data = [[], [], []]
            call()
        else:
            call()
    elif a == 5:
        view()
        l = int(input("Please enter the ID of completed task: "))
        data = comp(data, l)
        view()

    elif a ==6:
        export()
        print("Thank you for using the app")
        return
    elif a == 7:
        c = input("Are you sure you want to exit?(Y/N):\n").strip().lower()
        if c == "n":
            call()
        else:
            if data == [[], [], []]:
                print("Thank you for using the app!")
                return
            else:
                print("Would you like to export the your to-do as a CSV?(Y/N)")
                e = input().strip().lower()
                if e == "y":
                    export()
                else:
                    pass

                print("Thank you for using the app!")
                return

    # to-do: add logic to exit the app here
    else:
        print("Unexpected input. Please try again!")
        call()
    call()


def add(data, task, status = "In."):
    if data[0] == []:
        id = 1
    else:
        id = data[0][-1] + 1

    data[0].append(id)
    data[1].append(task)
    data[2].append(status)
    return data

def update(data, update_id, task, status = "In."):
    idx = data[0].index(update_id)
    data[1][idx] = task
    data[2][idx] = status
    return data

def comp(data, id):
    # global data
    idx = data[0].index(id)
    data[2][idx] = "C."
    return data

def print_out(data):
    data = list(zip(data[0], data[1], data[2]))
    out = tabulate.tabulate(data, headers = ["Task ID", "Task", "Status"], tablefmt = 'psql')
    print(out)

def view():
    global data
    print_out(data)

def export():
    name = input("Please enter your name: \n")
    global data
    file = pd.DataFrame({"Task ID": data[0], "Task": data[1], "Status": data[2]})
    file.to_csv(f"{name}'s to-do.csv", index = False, escapechar = '\t')
    print(f"To-do exported under the name {name}'s to-do.csv!")

if __name__ == "__main__":
    global data
    data = [[], [], []]
    main()
