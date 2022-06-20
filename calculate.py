from calculator import ThisCalculator
# Program make a simple calculator

# Program make a simple calculator
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    calcFunction = ThisCalculator()

    print(calcFunction.handleChoice(choice))
    # check if choice is one of the four options

    # if choice == '1':
    #     print(num1, "+", num2, "=", calcFunction.add(num1, num2))

    # elif choice == '2':
    #     print(num1, "-", num2, "=", calcFunction.subtract(num1, num2))

    # elif choice == '3':
    #     print(num1, "*", num2, "=", calcFunction.multiply(num1, num2))

    # elif choice == '4':
    #     print(num1, "/", num2, "=", calcFunction.divide(num1, num2))

    # check if user wants another calculation
    # break the while loop if answer is no

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no" or next_calculation == "n":
        break
