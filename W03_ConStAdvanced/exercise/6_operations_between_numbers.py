n1 = int(input())
n2 = int(input())
operator = input()

operation = 0
rest = 0
if operator == "+":
     operation = n1 + n2
     rest = operation % 2
     if rest != 0:
         print(f"{n1} {operator} {n2} = {operation} - odd")
     else:
         print(f"{n1} {operator} {n2} = {operation} - even")
elif operator == "-":
    operation = n1 - n2
    rest = operation % 2
    if rest != 0:
        print(f"{n1} {operator} {n2} = {operation} - odd")
    else:
        print(f"{n1} {operator} {n2} = {operation} - even")
elif operator == "*":
    operation = n1 * n2
    rest = operation % 2
    if rest != 0:
        print(f"{n1} {operator} {n2} = {operation} - odd")
    else:
        print(f"{n1} {operator} {n2} = {operation} - even")
elif operator == "/":
    if n2 != 0:
        operation = n1 / n2
        print(f"{n1} {operator} {n2} = {operation:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")
elif operator == "%":
    if n2 != 0:
        operation = n1 % n2
        print(f"{n1} {operator} {n2} = {operation}")
    else:
        print(f"Cannot divide {n1} by zero")
