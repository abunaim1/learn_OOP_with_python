# poly = many (multiple)
# morph = shape

from math import pi

class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Triangle(Shape):
    def __init__(self, name, base, height) -> None:
        self.base = base
        self.height = height
        super().__init__(name)
    
    def area(self):
        return 1/2*self.base*self.height

class Rectangle(Shape):
    def __init__(self, name, width, height) -> None:
        self.width = width
        self.height = height
        super().__init__(name)
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)
    def area(self):
        return pi * self.radius * self.radius

#1
t1 = Triangle('Trivuj', 10, 30)
print(t1.area())

#2
r1 = Rectangle('Choturvuj', 10, 30)
print(r1.area())

#3
c1 = Circle('Britto', 10)
print(c1.area())

