#Only lists concept used
students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grades = [int(x) for x in input("Enter grades (comma-separated): ").split(',')]
        students.append([name, age, grades])
        print(f"\nStudent '{name}' has been added to the system.")
    elif choice == '2':
        print("\n===== Students =====")
        if not students:
            print("No students in the system yet.")
        else:
            for student in students:
                print(f"Name: {student[0]}\nAge: {student[1]}\nGrades: {student[2]}")
                print("====================")
    elif choice == '3':
        search_name = input("Enter student name to search: ")
        found = False
        for student in students:
            if student[0] == search_name:
                print("\n===== Student Found =====")
                print(f"Name: {student[0]}\nAge: {student[1]}\nGrades: {student[2]}")
                found = True
                break
        if not found:
            print(f"No student with the name '{search_name}' found.")
    elif choice == '4':
        remove_name = input("Enter student name to remove: ")
        removed = False
        for student in students:
            if student[0] == remove_name:
                students.remove(student)
                print(f"\nStudent '{remove_name}' has been removed from the system.")
                removed = True
                break
        if not removed:
            print(f"No student with the name '{remove_name}' found.")
    elif choice == '5':
        break
    else:
        print("\nInvalid choice. Please try again.")
