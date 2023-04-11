num1 = int(input())
num2 = int(input())

for current_num in range(num1, num2 + 1):
    current_num_str = str(current_num)
    even_num = 0
    odd_num = 0
    for symbol in range(0, len(current_num_str)):
        digit = int(current_num_str[symbol])
        if symbol % 2 == 0:
            even_num += digit
        else:
            odd_num += digit
    if even_num == odd_num:
        print(current_num_str, end=" ")


'''
num_1 = int(input())
num_2 = int(input())

for current_num in range(num_1, num_2 + 1):
    odd_sum = 0
    even_sum = 0
    for index, char in enumerate(str(current_num), start=1):
        if index % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)
    if odd_sum == even_sum:
        print(current_num, end=" ")
'''