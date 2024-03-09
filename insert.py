# The first three lines are always used to connect to the database
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# The word faith uses single quotes because it is a string inside another string
conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH',54,25248.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'MARK',44,23700.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'JANE',34,23700.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'ALLAN',37,25244.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'IAN',29,25200.00)")


conn.commit()  # To commit the work
print("Records successfully inserted")
conn.close()
