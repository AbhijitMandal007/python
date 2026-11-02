import sqlite3

con=sqlite3.connect("employee.db")
cur=con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS 
employee(id INTEGER PRIMARY KEY,
name TEXT,
designation TEXT,
dept TEXT,
salary REAL)""")

cur.execute("INSERT INTO employee VALUES(?,?,?,?,?)",(2,"Suroj","DATA SCIENTIST","AI",250000))
cur.execute("INSERT INTO employee VALUES(?,?,?,?,?)",(3,"Debarka","MANAGER","IT",10000000000))
cur.execute("INSERT INTO employee VALUES(?,?,?,?,?)",(4,"Binit","SDE","IT",250000))

#Read Operations 
cur.execute("SELECT * FROM employee")
print(cur.fetchall(),"\n")

#Update Operations
cur.execute("UPDATE employee SET salary=? WHERE  id=?",(60000000,1))

#Delete Operations
cur.execute("DELETE FROM employee WHERE id=?",(2,))

con.commit()
con.close()