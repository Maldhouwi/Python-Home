class Person:
    def __init__(self, firstname, age, gender):
        self.firstname=firstname     # Line 3,4,5 initialising variable
        self.age = age
        self.gender=gender


def details(self):
    print(self.firstname, "is studying")

# Passing the parameters
teacher = Person("Joe",18,"male")
accountant = Person("Jennifer",38,"female")
doctor = Person("George",28,"male")

# To print out the details you will say
print(teacher.firstname,accountant.age,accountant.gender)