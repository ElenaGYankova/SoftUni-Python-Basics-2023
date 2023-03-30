count_of_numbers = int(input())
sum_of_numbers = 0

for numbers in range(count_of_numbers): #0,1,2...count_of_numbers - 1 # range(1, count_of_numbers, +1)
    current_number = int(input())
    sum_of_numbers += current_number

print(sum_of_numbers)
