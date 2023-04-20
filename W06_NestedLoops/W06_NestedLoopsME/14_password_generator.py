n = int(input())
L = int(input())

for a in range(1, n):
    for b in range(1, n):
        for c in range(ord("a"), ord("a") + L):
            for d in range(ord("a"), ord("a") + L):
                for e in range(max(a, b) + 1, n + 1):
                    print(f"{a}{b}{chr(c)}{chr(d)}{e}", end=" ")
