a = int(input())
b = int(input())
max_passwords = int(input())

counter = 0
A = ord("#")
B = ord("@")

for x in range(1, a + 1):
    if counter >= max_passwords or counter == (a * b):
        break
    for y in range(1, b + 1):
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        A += 1
        B += 1
        if A > ord("7"):
            A = ord("#")
        if B > ord("`"):
            B = ord("@")
        counter += 1
        if counter >= max_passwords or counter == (a * b):
            break
