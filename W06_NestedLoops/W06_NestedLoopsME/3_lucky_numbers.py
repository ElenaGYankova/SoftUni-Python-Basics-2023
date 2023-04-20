number = int(input())

if number < 10:
    check = number
else:
    check = 10
for a in range(1, check):
    for b in range(1, check):
        if number % (a + b) != 0:
            continue
        for c in range(1, check):
            for d in range(1, check):
                if a + b == c + d:
                    print(f"{a}{b}{c}{d}", end=" ")
