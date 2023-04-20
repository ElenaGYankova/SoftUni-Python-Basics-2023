n = int(input())

p1 = 0
p2 = 0
p3 = 0

for num in range(n):
    numbers = int(input())
    if numbers % 2 == 0:
        p1 += 1
    if numbers % 3 == 0:
        p2 += 1
    if numbers % 4 == 0:
        p3 += 1

p1_percent = p1 * 100 / n
p2_percent = p2 * 100 / n
p3_percent = p3 * 100 / n

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
