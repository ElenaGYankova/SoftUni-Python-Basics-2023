import sys

number = input()
min_num = sys.maxsize

while number != "Stop":
    num = int(number)
    if num < min_num:
        min_num = num
    number = input()
print(min_num)
