n = int(input())

for i in range(1, int(n) + 1):
    if i == 1:
        print((2 * n) * "*", n * " ", (2 * n) * "*", sep="")
    elif i == int((n + 1) / 2):
        print("*", (2 * n - 2) * "/", "*", n * "|", "*", (2 * n - 2) * "/", "*", sep="")
    elif i == n:
        print((2 * n) * "*", n * " ", (2 * n) * "*", sep="")
    else:
        print("*", (2 * n - 2) * "/", "*", n * " ", "*", (2 * n - 2) * "/", "*", sep="")
