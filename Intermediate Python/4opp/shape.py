from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def calculate_area(self):
        return self.side * self.side

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height

