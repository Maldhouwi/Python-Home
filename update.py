import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")


conn.execute("UPDATE EMPLOYEES AGE = 67 WHERE ID = 1")
conn.commit()

# From line 10-18 it should be copied for selecting,updating and deleting info on a table
cursor = conn.execute("SELECT ID,NAME,AGE,SALARY FROM EMPLOYEES")
for row in cursor:
    print("ID", row[0])
    print("NAME", row[1])
    print("AGE", row[2])
    print("SALARY", row[3])

print("Records found")
conn.close()

