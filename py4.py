students = []

while True:
    print("\n1.Create")
    print("2.Read")
    print("3.Update")
    print("4.Delete")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)

    elif choice == "2":
        print(students)

    elif choice == "3":
        old = input("Enter old name: ")
        new = input("Enter new name: ")

        if old in students:
            index = students.index(old)
            students[index] = new

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in students:
            students.remove(name)

    elif choice == "5":
        break