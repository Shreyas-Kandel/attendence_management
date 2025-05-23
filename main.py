from student_management import (
add_student,
update_student,
delete_student, 
view_students, 
take_attendance, 
view_attendance,
)

def menu():
    print("Welcome to the Student Attendance System \n")
    print("Enter 1 to add a student \n")
    print("Enter 2 to update a student \n")
    print("Enter 3 to delete a student \n")
    print("Enter 4 to view all students \n")
    print("Enter 5 to Take attendance \n")
    print("Enter 6 to view attendance \n")
    print("Enter 7 to exit \n")

while True:
    menu()
    option = input("Enter your choice: ")
    if option == "1":
        add_student()
    elif option == "2":
        update_student()
    elif option == "3":
        delete_student()
    elif option == "4":
        view_students()
        break
    elif option == "5":
        take_attendance()
    elif option == "6":
        view_attendance()
    elif option == "7":
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")

