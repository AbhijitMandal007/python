import sqlite3

con = sqlite3.connect("employee.db")
cur =con.cursor()

dept = input("Enter Department :")

cur.execute("""
SELECT dept ,SUM(salary),AVG(salary) FROM employee WHERE dept =? GROUP BY dept""",(dept,))

print(cur.fetchall())

con.close()