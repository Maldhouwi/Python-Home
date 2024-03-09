# Basiclly shows that one function can be used for various operations
class Shape:
    def draw(self):
        print("Drawing Shape")


class Square:
    def draw(self):
        print("Drawing Square")


class Rectangle:
    def draw(self):
        print("Drawing Rectangle")


# to run
a = Shape()
a.draw()