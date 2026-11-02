# tupple
student1 =(101,"harry")
student2 =(102,"jhon")
student3 =(103,"bob")
student4 =(104,"jack")

#set
python_student ={"harry","jhon","jack"}
java_student ={"jhon","bob"}

#studnt take at least one course
def student_course():
    student = python_student.union(java_student)
    print(student)

#student who take both the courses
def common_student():
    student = python_student.intersection(java_student)
    print(student)

#student take only python course
def student_python():
    student = python_student.difference(java_student)
    print(student)    

# student take only java course
def student_java():
    student = java_student.difference(python_student)
    print(student)

#main function
print("studnt take at least one course")
student_course()
print("student who take both the courses")
common_student()
print("student take only python course")
student_python()
print("student take only java course")
student_java()
