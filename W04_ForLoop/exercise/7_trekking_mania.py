group = int(input())

musala = 0
montblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
people_count = 0

for i in range(group):
    climbers = int(input())
    people_count += climbers
    if climbers <= 5:
        musala += climbers
    elif climbers <= 12:
        montblan += climbers
    elif climbers <= 25:
        kilimandjaro += climbers
    elif climbers <= 40:
        k2 += climbers
    elif climbers >= 41:
        everest += climbers
g1 = (musala / people_count) * 100
g2 = (montblan / people_count) * 100
g3 = (kilimandjaro / people_count) * 100
g4 = (k2 / people_count) * 100
g5 = (everest / people_count) * 100
print(f"{g1:.2f}%")
print(f"{g2:.2f}%")
print(f"{g3:.2f}%")
print(f"{g4:.2f}%")
print(f"{g5:.2f}%")
