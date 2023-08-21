class calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2


    def minus(self):
        return self.num1 - self.num2


    def multiply(self):
        return self.num1 * self.num2


    def divide(self):
        return self.num1 / self.num2
        
        
        
num = int(input("Enter number 1 : "))
numm = int(input("Enter number 2 : "))

cal = calculator(num, numm)
print("Add :", cal.add(), ", Minus :", cal.minus(), ", Multiply :", cal.multiply(), ", Divide :", cal.divide())