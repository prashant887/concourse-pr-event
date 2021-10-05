class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def diff(self):
        return self.a - self.b


if __name__ == '__main__':
    calc = Calculator(8, 5)
    print(calc.sum())
    print(calc.diff())
