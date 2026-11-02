import xml.etree.ElementTree as ET

file = "student.xml"


def add_student():
    tree = ET.parse(file)
    root = tree.getroot()

    student = ET.SubElement(root, "student")
    student.set("id", input("Enter ID: "))

    ET.SubElement(student, "name").text = input("Enter Name: ")
    ET.SubElement(student, "department").text = input("Enter Department: ")
    ET.SubElement(student, "year").text = input("Enter Year: ")
    ET.SubElement(student, "email").text = input("Enter Email: ")
    ET.SubElement(student, "cgpa").text = input("Enter CGPA: ")

    tree.write(file)
    print("Student added successfully!")


def display_students():
    tree = ET.parse(file)
    root = tree.getroot()

    for student in root.findall("student"):
        print("\nID:", student.get("id"))
        print("Name:", student.find("name").text)
        print("Department:", student.find("department").text)
        print("Year:", student.find("year").text)
        print("Email:", student.find("email").text)
        print("CGPA:", student.find("cgpa").text)


def delete_student():
    tree = ET.parse(file)
    root = tree.getroot()

    id = input("Enter ID to delete: ")

    for student in root.findall("student"):
        if student.get("id") == id:
            root.remove(student)
            tree.write(file)
            print("Student deleted!")
            return

    print("Student not found!")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
