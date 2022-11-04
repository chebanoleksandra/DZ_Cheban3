import random


class Class:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __shifr(self):
        shifr = random.randint(1, 4)
        if shifr == 1:
            result = self.a + self.b
        if shifr == 2:
            result = self.a - self.b
        if shifr == 3:
            result = self.a * self.b
        if shifr == 4:
            result = self.a / self.b
        print(result)

    def get_shifr(self):
        self.__shifr()


s = Class(a=int(input('Enter first number')), b=int(input('Enter second number')))
s.get_shifr()
