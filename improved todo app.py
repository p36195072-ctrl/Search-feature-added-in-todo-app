def add_task():
    task = input("enter your task you wanna add?"+ "\n")

    file = open("task.txt" , "a")
    file.write (task + "\n")
    file.close()

    print("task saved")

def view_task():
    file = open("task.txt" , "r")

    task = file.readlines()

    

    for i, task in enumerate(task):
        print(i , task)

def delete_task():
    with open("task.txt", "r") as file:
        tasks = file.readlines()

    if len(tasks) == 0:
        print("No tasks to delete")
        return

    for i, task in enumerate(tasks):
        print(i, task.strip())

    delete_index = int(input("Enter the task number: "))

    if delete_index < 0 or delete_index >= len(tasks):
        print("Invalid task number")
        return

    tasks.pop(delete_index)

    with open("task.txt", "w") as file:
        for task in tasks:
            file.write(task)

    print("Task deleted")

    print("There is some error")

def search_task():
    file = open("task.txt" , "r")

    tasks = file.readlines()

    file.close()

    search = input("What you want you search:")
    for task in tasks:
        if search in task:
            print ("Founded:" , task.strip())


while True:
    
    print("1. add task?")
    print("2. view task?")
    print("3. Delete task")
    print("4. search for tasks?")
    
    print("5. Exit")

     
    
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()

    elif choice == 2:
        view_task()

    elif choice == 3:
        delete_task()

    elif choice == 4:
        search_task()

    elif choice == 5:
        break
    