number = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                is_valid = number % i == 0 and number % j == 0 and number % k == 0 and number % l == 0
                if is_valid:
                    print(f"{i}{j}{k}{l}", end=" ")

'''
number = int(input())
magic_counter = 0
is_special = False
for i in range(1111, 9999 + 1):

    for index, value in enumerate(str(i)):

        if value == "0":
            break
        elif number % int(value) == 0:
            magic_counter += 1

        if magic_counter == 4:
            is_special = True

    if is_special:
        print(i, end=" ")

    magic_counter = 0
    is_special = False
'''