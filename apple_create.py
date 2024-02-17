import random

class Apple:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.delicious = 10
        self.mold = 0
        print("Created!")

    def deli(self, days):
        self.delicious = self.delicious + days * 0.1 * random.randint(0, 11)

    def rot(self, days, temp):
        self.mold = days * temp


apple = Apple(120, "Red")
apple.deli(5)
apple.rot(5, 20)

print(apple.delicious)
print(apple.mold)
