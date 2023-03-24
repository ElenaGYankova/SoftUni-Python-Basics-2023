number = float(input())

while number >= 0:
    num = number * 2
    print(f"Result: {num:.2f}")

    number = float(input())
else:
    print("Negative number!")
