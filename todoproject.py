# This is my beginner friendly mini project created by using lists,loops,conditional statments
'''
tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = int(input("Enter task number to remove: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f'"{removed}" removed successfully!')
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

        '''
        
import random
import string

length = int(input("Password length: "))
use_symbols = input("Include symbols? y/n: ").lower() == "y"

chars = string.ascii_letters + string.digits
if use_symbols:
    chars += string.punctuation

password = ''.join(random.choice(chars) for _ in range(length))
print(f"Your password: {password}")

marks = int(input("Enter your marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter 0 to 100 only")
else:
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 33:
        grade = "E - Pass"
    else:
        grade = "F - Fail"
    
    print(f"Your grade is: {grade}")