n1 = int(input())
n2 = int(input())
n3 = int(input())

for a in range(1, n1 + 1):
    if a % 2 != 0:
        continue
    for b in range(1, n2 + 1):
        if b not in (2, 3, 5, 7):
            continue
        for c in range(1, n3 + 1):
            if c % 2 == 0:
                print(f"{a} {b} {c}")
