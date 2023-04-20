n = int(input())

for i in range(0, n + 1):
    print((n - i) * ' ', i * '*', ' | ', i * '*', (n - i) * ' ', sep="")
