stadium_capacity = int(input())
fans = int(input())
A = 0
B = 0
V = 0
G = 0

for i in range(fans):
    sector = input()
    if sector == "A":
        A += 1
    elif sector == "B":
        B += 1
    elif sector == "V":
        V += 1
    elif sector == "G":
        G += 1

avg_A = (A / fans) * 100
avg_B = (B / fans) * 100
avg_V = (V / fans) * 100
avg_G = (G / fans) * 100
avg_stadium = (fans / stadium_capacity) * 100

print(f"{avg_A:.2f}%")
print(f"{avg_B:.2f}%")
print(f"{avg_V:.2f}%")
print(f"{avg_G:.2f}%")
print(f"{avg_stadium:.2f}%")
