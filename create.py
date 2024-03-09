import sqlite3    # To open the database

conn = sqlite3.connect('test.db')     # To connect to the database
print("Opened database successfully")

# Execute function is used to do things in the database
# Not null is used to ensure that the value is not left blank
# The primary key is used to show tha the id can not be repeated once used
conn.execute('''CREATE TABLE EMPLOYEES(
ID INT PRIMARY KEY NOT NULL,     
NAME TEXT NOT NULL,
AGE INT NOT NULL,
SALARY REAL NOT NULL);''')

# Don't forget the commas after every entry and the semicolon after finishing the last entry and the triple quotes



print("Table created successfully")
conn.close()


# Single quotes are used when you want to write a string in another string