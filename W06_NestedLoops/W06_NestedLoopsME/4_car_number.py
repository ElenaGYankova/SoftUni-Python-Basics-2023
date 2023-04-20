start = int(input())
end = int(input())

for a in range(start, end + 1):
    for b in range(start, end + 1):
        for c in range(start, end + 1):
            if (b + c) % 2 != 0:
                continue
            for d in range(start, end + 1):
                if a < d:
                    continue
                if a % 2 == 0 and d % 2 == 0:
                    continue
                if a % 2 != 0 and d % 2 != 0:
                    continue
                print(f"{a}{b}{c}{d}", end=" ")
