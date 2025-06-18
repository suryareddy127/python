'''
input: num1
       num2
operation( '+','-','*','/' )
output:
    perform the operation on the input
'''

num1 = float(input("enter a value: "))
num2 = float(input("enter a value: "))
operator = input("enter operator: ")
if operator == "+":
    print(f"Addition of two numbers: {num1 + num2}")
elif operator == "-":
    print(f"Substraction of two numbers: {num1 - num2}")
elif operator == "*":
    print(f"Multiplication of two numbers: {num1 * num2}")
elif operator == "/":
    print(f"Division of two numbers: {num1 / num2}")
else:
    print("invalid operator")
