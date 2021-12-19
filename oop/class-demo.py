class Calculator:
    num = 100
    # constructor
    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print("Constructor")
    def getData(self):
        print("Method in class")
    def Summary(self):
        # can call <ClassName>.<variable>
        # but cannot call variable directly in class.
        return self.firstNum + self.secondNum + Calculator.num;
obj = Calculator(2, 3)
obj1 = Calculator(3, 5)
print(obj.Summary())
