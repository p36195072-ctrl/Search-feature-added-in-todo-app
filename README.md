Improved To-Do App

A beginner-friendly Python project that demonstrates how to build an improved To-Do application with task management features using file handling and functions.

📌 Description

This program allows the user to:

Add tasks
View all tasks
Delete a selected task
Search for tasks
Exit the application

All tasks are stored inside a file named task.txt.

🧠 Concepts Used

Functions
File Handling
with open()
Read Mode ('r')
Write Mode ('w')
Append Mode ('a')
readlines() method
Lists
pop() method
enumerate() function
for loop
while True loop
if-elif
User Input

💻 Code

def add_task():
    task = input("enter your task you wanna add?\n")

    file = open("task.txt", "a")
    file.write(task + "\n")
    file.close()

    print("task saved")

def view_task():
    file = open("task.txt", "r")

    tasks = file.readlines()

    for i, task in enumerate(tasks):
        print(i, task.strip())

    file.close()

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

def search_task():
    file = open("task.txt", "r")

    tasks = file.readlines()

    file.close()

    search = input("What you want to search: ")

    for task in tasks:
        if search in task:
            print("Founded:", task.strip())

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

▶️ Example Output

1. add task?
2. view task?
3. Delete task
4. search for tasks?
5. Exit

Enter your choice: 1
enter your task you wanna add?
Learn Python

task saved
Enter your choice: 2
0 Learn Python
Enter your choice: 4
What you want to search: Python
Founded: Learn Python
