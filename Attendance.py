import os
import getpass
import time

def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

students = []

def login():
    clear()
    user = "admin"
    passwd = "foows"
    print("""
 █████╗ ████████╗████████╗███████╗███╗  ██╗██████╗  █████╗ ███╗  ██╗ █████╗ ███████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗ ██║██╔══██╗██╔══██╗████╗ ██║██╔══██╗██╔════╝
███████║   ██║      ██║   █████╗  ██╔██╗██║██║  ██║███████║██╔██╗██║██║  ╚═╝█████╗
██╔══██║   ██║      ██║   ██╔══╝  ██║╚████║██║  ██║██╔══██║██║╚████║██║  ██╗██╔══╝
██║  ██║   ██║      ██║   ███████╗██║ ╚███║██████╔╝██║  ██║██║ ╚███║╚█████╔╝███████╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝ ╚════╝ ╚══════╝
          
══════════════════════════ Attendance Monitoring System ═════════════════════════════""")
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')
    time.sleep(2)
    clear()
    loading()
    if username != user or password != passwd:
        print("Invalid credentials! Abandoning...")
        quit(1)
        time.sleep(2)
        main()

def loading():
    for i in range(6):
        print("Loading" + "." * i)
        time.sleep(0.5)
        clear()
    time.sleep(2)

def logout_loading():
    for i in range(6):
        print("Logout" + "." * i)
        time.sleep(0.5)
        clear()
    time.sleep(2)

def delete_loading():
    for i in range(6):
        print("Delete" + "." * i)
        time.sleep(0.5)
        clear()
    time.sleep(2)

def exit_loading():
    for i in range(6):
        print("Exit" + "." * i)
        time.sleep(0.5)
        clear()
    time.sleep(2)

def exit():
    clear()
    exit_loading()
    clear()
    time.sleep(1)
    print("Thanks for using Attendance Monitoring System, bye bye bye!")
    quit()


def main():
    print("""
 █████╗ ████████╗████████╗███████╗███╗  ██╗██████╗  █████╗ ███╗  ██╗ █████╗ ███████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗ ██║██╔══██╗██╔══██╗████╗ ██║██╔══██╗██╔════╝
███████║   ██║      ██║   █████╗  ██╔██╗██║██║  ██║███████║██╔██╗██║██║  ╚═╝█████╗
██╔══██║   ██║      ██║   ██╔══╝  ██║╚████║██║  ██║██╔══██║██║╚████║██║  ██╗██╔══╝
██║  ██║   ██║      ██║   ███████╗██║ ╚███║██████╔╝██║  ██║██║ ╚███║╚█████╔╝███████╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝ ╚════╝ ╚══════╝
          
══════════════════════════ Attendance Monitoring System ═════════════════════════════""")
    print("")
    print("Welcome, System Administrator")
    print("Role: \x1b[38:5:46mADMIN\x1b[38:5:7m")
    print(f""" 
╔══════════════════════════════╗
║  Attendance Monitoring Menu  ║
╠══════════════════════════════╣
║  1. Add New Student          ║
║  2. Log Out                  ║
║  0. Exit                     ║
╚══════════════════════════════╝""")
    choice = int(input("Choice: "))
    clear()

    if choice == 1:
        add_student()
    elif choice == 2:
        time.sleep(1)
        logout_loading()
        login()
    elif choice == 0:
        exit()

def main2():
    print("""
 █████╗ ████████╗████████╗███████╗███╗  ██╗██████╗  █████╗ ███╗  ██╗ █████╗ ███████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗ ██║██╔══██╗██╔══██╗████╗ ██║██╔══██╗██╔════╝
███████║   ██║      ██║   █████╗  ██╔██╗██║██║  ██║███████║██╔██╗██║██║  ╚═╝█████╗
██╔══██║   ██║      ██║   ██╔══╝  ██║╚████║██║  ██║██╔══██║██║╚████║██║  ██╗██╔══╝
██║  ██║   ██║      ██║   ███████╗██║ ╚███║██████╔╝██║  ██║██║ ╚███║╚█████╔╝███████╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝ ╚════╝ ╚══════╝
          
══════════════════════════ Attendance Monitoring System ═════════════════════════════""")
    print("")
    print("Welcome System Administrator")
    print("Role: \x1b[38:5:46mADMIN\x1b[38:5:7m")
    print(f""" 
╔══════════════════════════════╗
║  Attendance Monitoring Menu  ║
╠══════════════════════════════╣
║  1. Add New Student          ║
║  2. View Attendance          ║
║  3. Edit Attendance          ║
║  4. Delete Attedance         ║
║  5. Log Out                  ║
║  0. Exit                     ║
╚══════════════════════════════╝""")
    choice = int(input("Choice: "))
    clear()

    if choice == 1:
        add_student()
    elif choice == 2:
        view_attendance()
    elif choice == 3:
        edit_student()
    elif choice == 4:
        delete()
    elif choice == 5:
        time.sleep(1)
        logout_loading()
        login()
    elif choice == 0:
        exit()


def add_student():
    print("""
 █████╗ ████████╗████████╗███████╗███╗  ██╗██████╗  █████╗ ███╗  ██╗ █████╗ ███████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗ ██║██╔══██╗██╔══██╗████╗ ██║██╔══██╗██╔════╝
███████║   ██║      ██║   █████╗  ██╔██╗██║██║  ██║███████║██╔██╗██║██║  ╚═╝█████╗
██╔══██║   ██║      ██║   ██╔══╝  ██║╚████║██║  ██║██╔══██║██║╚████║██║  ██╗██╔══╝
██║  ██║   ██║      ██║   ███████╗██║ ╚███║██████╔╝██║  ██║██║ ╚███║╚█████╔╝███████╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝ ╚════╝ ╚══════╝
          
══════════════════════════ Attendance Monitoring System ═════════════════════════════""")
    print("")
    num_students = int(input("How many students: "))
    print("═════════")

    for i in range(num_students):
        print()
        print(f"Student {i + 1}:")
        name = input("Name: ")
        school_id = input("School ID: ")
        year = input("Year: ")
        course = input("Course: ")
        
        students.append({
            "Name": name,
            "School ID": school_id,
            "Year": year,
            "Course": course
        })
    print("═════════")
    print()
    time.sleep(2)
    text = input("Students added successfully! (Press any key to continue) ")
    time.sleep(2)
    clear()
    main2()
         

def view_attendance():
    if not students:
        print("═════════")
        print("No student data available.")
        print("═════════")
    else:
        print("════════════════════════ Student Attendance List ════════════════════════")
        for i, student in enumerate(students, 1):
            print(f"Student {i}:")
            print(f"  Name       : {student['Name']}")
            print(f"  School ID  : {student['School ID']}")
            print(f"  Year       : {student['Year']}")
            print(f"  Course     : {student['Course']}")
            print("═════════════════════════════════════════════════════════════════════════")
            print()
    text = input("Press Enter to return to the menu... ")
    clear()
    main2()

def edit_student():
    if not students:
        print("═════════")
        print("No student data available to edit.")
        print("═════════")
    else:
        print("════════════════════════ Student Attendance List ════════════════════════")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student['Name']}")
        print("═════════════════════════════════════════════════════════════════════════")
        try:
            choice = int(input("Select student number you want to edit: "))
            time.sleep(1)
            clear()
            if 1 <= choice <= len(students):
                selected_student = students[choice - 1]
                print("""
 █████╗ ████████╗████████╗███████╗███╗  ██╗██████╗  █████╗ ███╗  ██╗ █████╗ ███████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗ ██║██╔══██╗██╔══██╗████╗ ██║██╔══██╗██╔════╝
███████║   ██║      ██║   █████╗  ██╔██╗██║██║  ██║███████║██╔██╗██║██║  ╚═╝█████╗
██╔══██║   ██║      ██║   ██╔══╝  ██║╚████║██║  ██║██╔══██║██║╚████║██║  ██╗██╔══╝
██║  ██║   ██║      ██║   ███████╗██║ ╚███║██████╔╝██║  ██║██║ ╚███║╚█████╔╝███████╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝ ╚════╝ ╚══════╝
          
══════════════════════════ Attendance Monitoring System ═════════════════════════════""")
                print("Role: \x1b[38:5:46mADMIN\x1b[38:5:7m")
                print("")
                print("═════════════════")
                print("Current Details:")
                print(f"Name       : {selected_student['Name']}")
                print(f"School ID  : {selected_student['School ID']}")
                print(f"Year       : {selected_student['Year']}")
                print(f"Course     : {selected_student['Course']}")
                print("═════════════════")
                print()
                print("Enter new details")
                new_name = input(f"Name: ") or selected_student['Name']
                new_school_id = input(f"School ID: ") or selected_student['School ID']
                new_year = input(f"Year: ") or selected_student['Year']
                new_course = input(f"Course: ") or selected_student['Course']

                selected_student['Name'] = new_name
                selected_student['School ID'] = new_school_id
                selected_student['Year'] = new_year
                selected_student['Course'] = new_course
                print()
                time.sleep(2)
                print("Student details updated successfully!")
            else:
                print("Invalid selection. Returning to the menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print()
    input("Press Enter to return to the menu... ")
    time.sleep(2)
    clear()
    main2()

def delete():
    if not students:
        print("═════════")
        print("No student data available to delete.")
        print("═════════")
    else:
        print("════════════════════════ Student List ════════════════════════")
        for i, student in enumerate(students, 1):
            print(f"Student {i}:")
            print(f"  Name       : {student['Name']}")
            print(f"  School ID  : {student['School ID']}")
            print(f"  Year       : {student['Year']}")
            print(f"  Course     : {student['Course']}")
            print("═════════════════════════════════════════════════════════════════════════")
        try:
            choice = int(input("Select student number to delete or (0 to Cancel): "))
            time.sleep(2)
            delete_loading()
            if choice == 0:
                print("Deletion cancelled.")
            elif 1 <= choice <= len(students):
                removed_student = students.pop(choice - 1)
                print(f"Student {removed_student['Name']} has been successfully deleted...")
            else:
                print("Invalid choice. Please select student number.")
        except ValueError:
            print("Please select student number")
    print()
    print("═════════")
    input("Press Enter to return to the menu... ")
    loading()
    clear()
    main2()

login()
while True:
    main()