# InBuilt Functions
# To show the largest number in a group
y = max(56, 67, 84, 95, 12)
print(y)

# To show the smallest number in a group
x= min(56, 67, 84, 95, 12)
print(x)

# Two raised to power three

z =pow(2,3)
print(z)

# User defined Functions
def details():
    print("Hello World")

details()  # calling the functions

#Parameters and arguments
def students(name,course,age):
    print(name,course,age)

students("Ashley","MIT",17)
students("Precious","Cybersecurity",27)


def employees(fullname, identificationnumber, salary, position, age):
    print(fullname, identificationnumber, salary, position, age)

employees("Ashley Njeri",20965993,120000,"Operations Manager",37)
employees("Justina Syokau",20963654,100000,"General Manager",45)
employees("Jeniffer Njoki",23453948,90000,"Human Resource Manager",30)
employees("Carlos Gambino",2327937,60000,"Senior Developer",21)
employees("Jason Wafula",2362927,50000,"Junior Developer",23)


