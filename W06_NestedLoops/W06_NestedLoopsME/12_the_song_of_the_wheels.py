control_number = int(input())
password = ""
counter = 0
is_found = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b and c > d) and (a * b + c * d == control_number):
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        password = f"{a}{b}{c}{d}"
                        is_found = True
if is_found:
    print()
    print(f"Password: {password}")
else:
    print()
    print("No!")


'''
control_number = int(input())
counter = 0
num_found = False
combination = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a >= b:
                    break
                if c <= d:
                    break
                if a * b + c* d == control_number:
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        combination = (a, b, c, d)
                        num_found = True
if num_found:
    print(f"\nPassword: {combination[0]}{combination[1]}{combination[2]}{combination[3]}")
else:
    print(f"\nNo!")
'''