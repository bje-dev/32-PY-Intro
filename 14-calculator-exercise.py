print("Welcome to the calculator in python")
print("To exit, type exit")

number1 = 0
number2 = 0
total = 0
operation = ""
while operation != "exit":

    number1 = input("Enter first number:")
    number1 = int(number1)
    operation = input("Enter an operation: suma - rest - mult - divi")
    operation = str(operation)
    number2 = input("Enter second number:")
    number2 = int(number2)
    if operation == "suma":
        total = number1 + number2
        print(f"The result of the operation is: {total}")
    elif operation == "rest":
        total = number1 - number2
        print(f"The result of the operation is: {total}")
    elif operation == "mult":
        total = number1 * number2
        print(f"The result of the operation is: {total}")
    elif operation == "divi":
        total = number1 / number2
        print(f"The result of the operation is: {total}")
    elif operation == "exit":
        print("End")
        break
    else:
        print("Input error - Please type a valid operator again")
