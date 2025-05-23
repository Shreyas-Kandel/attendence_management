def add_student():
    print("Adding a student...")
    with open("students.txt", "a") as file:
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        age = input("Enter student age: ")
        file.write(f"Name:{name}, Roll No:{roll_no}, Age:{age}\n")
        print("Student data recorded successfully.")

def update_student():
    print("Updating a student...")
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
    updateroll = input("Enter the roll number of the student to update: ")
    with open("students.txt", "w") as file:
        updated = False
        for line in lines:
            if f"Roll No:{updateroll}," in line:
                name = input("Enter the updated student name: ")
                age = input("Enter the updated student age: ")
                file.write(f"Name:{name}, Roll No:{updateroll}, Age:{age}\n")
                updated = True
            else:
                file.write(line)
        if updated:
            print(f"Updated student with roll number {updateroll}")
        else:
            print(f"No student found with roll number {updateroll}")

def delete_student():
    print("Deleting a student...")
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
    deleteroll = input("Enter the roll number of the student to delete: ")
    with open("students.txt", "w") as file:
        for line in lines:
            if f"Roll No:{deleteroll}," not in line:
                file.write(line)
            else:
                print(f"Deleted student with roll number {deleteroll}")

def view_students():
    print("Viewing all students...")
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

def take_attendance():
    print("Taking attendance...")
    with open(".txt", "a") as file:
        roll_no = input("Enter student roll number: ")
        status = input("Enter attendance status (Present/Absent): ")
        file.write(f"Roll No:{roll_no}, Status:{status}\n")

def view_attendance():
    print("Viewing attendance...")
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())