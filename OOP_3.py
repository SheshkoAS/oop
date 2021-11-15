class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def subtraction(self, a, b):
        self.a = a
        self.b = b
        return self.a - self.b

example = Math(24, 8)


print(example.addition())
print(example.multiplication())
print(example.division())
print(example.subtraction(16, 15))