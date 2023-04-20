hundreds = int(input())
tens = int(input())
singles = int(input())

for a in range(1, hundreds + 1):
    if a % 2 == 0:
        for b in range(1, tens + 1):
            if b in [2, 3, 5, 7]:
                for c in range(1, singles + 1):
                    if c % 2 == 0:
                        print(f"{a} {b} {c}")
