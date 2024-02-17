import math

class Circle:
    def __init__(self, r):
        self.area = r * r * math.pi
        print("Created!")

circle = Circle(5)
print(circle.area)
