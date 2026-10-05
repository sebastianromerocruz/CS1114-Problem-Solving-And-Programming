operand_a = float(input("Enter a number: "))
operator = input("Enter an operator [+-*/]: ")
operand_b = float(input("Enter another number: "))

operation = f"{operand_a} {operator} {operand_b}"

if operator == '+':
    print(f"{operation} = {operand_a + operand_b}")
elif operator == '-':
    print(f"{operation} = {operand_a - operand_b}")
elif operator == '*':
    print(f"{operation} = {operand_a * operand_b}")
else:
    if operand_b == 0:
        print(f"{operation} is an invalid operation")
    else:
        print(f"{operation} = {operand_a / operand_b}")
