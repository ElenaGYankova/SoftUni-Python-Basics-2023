diamond = int(input())

dashes = (int(diamond / 2) - 1)
mid_odd = 1
mid_even = 0

if diamond % 2 != 0:
    print(f"{(dashes + 1) * '-'}*{(dashes + 1) * '-'}")
for i in range(0, int(diamond/2)):
    midpoint = mid_even if diamond % 2 == 0 else mid_odd
    print(f"{(dashes - i) * '-'}*{midpoint * '-'}*{(dashes - i) * '-'}")
    if diamond % 2 == 0:
        mid_even += 2
    else:
        mid_odd += 2
mid_even = mid_even - 2
mid_odd = mid_odd - 2
for i in range((int(diamond/2)-1), 0, -1):
    if diamond % 2 == 0:
        mid_even -= 2
    else:
        mid_odd -= 2
    midpoint = mid_even if diamond % 2 == 0 else mid_odd
    print(f"{(dashes - i + 1) * '-'}*{midpoint * '-'}*{(dashes - i + 1) * '-'}")
if diamond % 2 != 0 and diamond > 1:
    print(f"{(dashes + 1) * '-'}*{(dashes + 1) * '-'}")
