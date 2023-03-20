age = float(input())
gender = str(input())

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")

if gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
