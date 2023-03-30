n = int(input())
odd_sum = 0
even_sum = 0

for position in range(1, n + 1):
    current_num = int(input())
    if position % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num
if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No")
    print(f"Diff = {diff}")
