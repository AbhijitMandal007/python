#using list

students =[
    {"name":"Rahul","roll":101,"mark":87},
    {"name":"john", "roll":102,"mark":47},
]    

#define display function
def display():
    for student in students:
        print(student)

#define insert function
def insert_student(name,roll,mark):
    students.append({"name":name,"roll":roll,"mark":mark})
    print("successful")

#define remove function
def remove_student(roll):
    for student in students:
        if student["roll"]== roll:
            students.remove(student)
        print("remove successful")
            return
        print("student not found")

#defne search functoin
def search_student(roll):
    for student in students:
        if student["roll"] == roll:
            print(student)

# main fnction


insert_student ("Akash",103,57)
remove_student(101)
search_student(102)
display()
print("hello")


