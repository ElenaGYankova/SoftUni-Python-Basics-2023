turns = int(input())
result = 0
f_0_to_9 = 0
f_10_to_19 = 0
f_20_to_29 = 0
f_30_to_39 = 0
f_40_to_50 = 0
invalid_numbers = 0

for i in range(turns):
    score = int(input())
    if score < 0 or score > 50:
        result /= 2
        invalid_numbers += 1
    elif score <= 9:
        result += score * 0.2
        f_0_to_9 += 1
    elif score <= 19:
        result += score * 0.3
        f_10_to_19 += 1
    elif score <= 29:
        result += score * 0.4
        f_20_to_29 += 1
    elif score <= 39:
        result += 50
        f_30_to_39 += 1
    elif score <= 50:
        result += 100
        f_40_to_50 += 1

avg_0_to_9 = (f_0_to_9 / turns) * 100
avg_10_to_19 = (f_10_to_19 / turns) * 100
avg_20_to_29 = (f_20_to_29 / turns) * 100
avg_30_to_39 = (f_30_to_39 / turns) * 100
avg_40_to_50 = (f_40_to_50 / turns) * 100
avg_inv_num = (invalid_numbers / turns) * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {avg_0_to_9:.2f}%")
print(f"From 10 to 19: {avg_10_to_19:.2f}%")
print(f"From 20 to 29: {avg_20_to_29:.2f}%")
print(f"From 30 to 39: {avg_30_to_39:.2f}%")
print(f"From 40 to 50: {avg_40_to_50:.2f}%")
print(f"Invalid numbers: {avg_inv_num:.2f}%")
