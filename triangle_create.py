import math

class Triangle:
    def __init__(self, a, b, c):
        s = (a + b + c) / 2
        self.area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Created!")


tr1 = Triangle(3, 4, 5)
tr2 = Triangle(6, 12, 14)
print(tr1.area)
print(tr2.area)
