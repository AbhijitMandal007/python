import sqlite3

# Connect to SQlite database
con  = sqlite3.connect("student1.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
roll_no INTEGER PRIMARY KEY,
name TEXT,
department TEXT,
cgpa REAL
)
""")


roll = int(input("Enter Roll Number :"))
name =  input("Enter Name :")
department = input("Enter Department :")
cgpa = float(input("Enter CGPA :"))

cursor.execute("INSERT INTO Student VALUES(?,?,?,?)",
               (roll,name,department,cgpa))

con.commit()

# Display
print("\nStudents Detail:")
cursor.execute("SELECT*FROM Student")

for row in cursor.fetchall():
    print("Roll No:" ,row[0])
    print("Name:",row[1])
    print("Department:",row[2])
    print("CGPA:",row[3])
    print()

con.close()    