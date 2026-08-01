class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1416

    def get_area(self):
        return self.pi * (self.radius ** 2)

test = Circle(10)
print(test.get_area())