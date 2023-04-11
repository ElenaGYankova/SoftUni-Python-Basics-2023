n = int(input())

current_number = 1
is_current_number_bigger_than_n = False
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current_number > n:
            is_current_number_bigger_than_n = True
            break
        print(str(current_number) + ' ', end='')
        current_number += 1
    if is_current_number_bigger_than_n:
        break
    print()


'''
number = int(input())
counter = 1
is_current_bigger = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if counter > number:
            is_current_bigger = True
            break
        else:
            print(counter, end=" ")
            counter += 1
    if is_current_bigger:
        break
    print() 
'''