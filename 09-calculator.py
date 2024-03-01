
number1 = input("Enter number one:")
number2 = input("Enter number two:")
number1 = int(number1)
number2 = int(number2)

summ = number1 + number2
ress = number1 - number2
mull = number1 * number2
divv = number1 / number2

message = f"""
For numbers {number1} and {number2},
the result of the sum is {summ}.
the result of the substraction is {ress}.
the result of the multiplication is {mull}.
the result of the division is {divv}.
"""

print(message)
