import sys

iterations = int(input())
max_num = -sys.maxsize
sum_numbers = 0
for number in range(iterations):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num
sum_numbers -= max_num
diff = abs(max_num - sum_numbers)
if sum_numbers == max_num:
    print(f"Yes")
    print(f"Sum = {sum_numbers}")
else:
    print(f"No")
    print(f"Diff = {diff}")
