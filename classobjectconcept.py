# Class is a blueprint of an object
# An object is an instance of a class
class Person:
    # Properties/Attributes/Characteristics

    name = "Bob"
    age = 23
    location = "New York"


    def speak(self):
        print("Hello person is speaking")


accountant = Person      # Instantiating/creating an object

accountant.speak()      # Calling the function but we have to mention the object which in this case is accountant
