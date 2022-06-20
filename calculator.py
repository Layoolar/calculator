from msilib.schema import Class
from secrets import choice


class ThisCalculator():

    # This function adds two numbers
    def add(self, x, y):
        return x+y

    # This function subtracts two numbers
    def subtract(self, x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(self, x, y):
        return x * y

    # This function divides two numbers
    def divide(self, x, y):
        x / y

    def handleOption(self, choice, x, y):
        if choice == 1:
            # return x, "+", y, "=", self.add(x, y)
            return f'{x} + {y} = {self.add(x, y)}'
        elif choice == 2:
            return f'{x} - {y} = {self.subtract(x, y)}'
        elif choice == 3:
            return f'{x} * {y} = {self.multiply(x, y)}'
        elif choice == 4:
            return f'{x} / {y} = {self.divide(x, y)}'
        else:
            return "invalid"

    def handleChoice(self, choice):
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return self.handleOption(int(choice), num1, num2)
