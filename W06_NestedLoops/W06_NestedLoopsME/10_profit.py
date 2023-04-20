one_lv = int(input())
two_lv = int(input())
five_lv = int(input())
total_sum = int(input())

for a in range(one_lv + 1):
    for b in range(two_lv + 1):
        for c in range(five_lv + 1):
            if total_sum == a + b * 2 + c * 5:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {total_sum} lv.")
