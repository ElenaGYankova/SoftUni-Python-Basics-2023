n = int(input())

for a in range(1, n + 1):
    print((n - a) * " ", end="")
    print("*", end="")
    print((a - 1) * " *", end="")
    print()
for b in range(n - 1, 0, -1):
    print((n - b) * " ", end="")
    print("*", end="")
    print((b - 1) * " *", end="")
    print()
