# Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")


# Child class
class Dog(Animal):    # This shows that the dog has inherited the speaking trait from class animal
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print(" Cat is meowing")


# To run
a = Animal()
a.speak()