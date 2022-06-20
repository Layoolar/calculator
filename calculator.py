from msilib.schema import Class
from secrets import choice

# Class that handles the calculator app


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
        return x / y

    # Function that handles the choice input to determine which operation to run
    def handleOption(self, choice, x, y):
        if choice == 1:
            return f'{x} + {y} = {self.add(x, y)}'
        elif choice == 2:
            return f'{x} - {y} = {self.subtract(x, y)}'
        elif choice == 3:
            return f'{x} * {y} = {self.multiply(x, y)}'
        elif choice == 4:
            return f'{x} / {y} = {self.divide(x, y)}'

    # A function that requests for the inputs and passes it if the choice input is valid

    def handleChoice(self, choice):
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return self.handleOption(int(choice), num1, num2)
        else:
            return "Invalid input"

    # A function that starts the chains. Receives the choice input and returns the answer
    def initial(self):
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        choice = input("Enter choice(1/2/3/4): ")
        print(f' {self.handleChoice(choice)}')

    # A function to handle if you want to perform another calculation
    def nextCalc(self):
        state = True
        while state:
            next_calculation = input(
                "Let's do next calculation? (yes or y/no or n): ")
            if next_calculation == "no" or next_calculation == "n":
                state = False
            if next_calculation == "yes" or next_calculation == "y":
                self.initial()
