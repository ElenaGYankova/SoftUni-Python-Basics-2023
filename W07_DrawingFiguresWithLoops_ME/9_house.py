from math import ceil
number = int(input())
n_count = 0
dashes = ceil((number / 2) - 1) * "-"
for n in range(ceil(number / 2)):
    if n == 0:
        if number % 2 == 0:
            print(f"{dashes}{2 * '*'}{dashes}")
            n_count = 2
        else:
            print(f"{dashes}*{dashes}")
            n_count = 1
    elif n != 0:
        n_count += 2
        dashes_2 = ceil((number - (n_count + 1))/2) * "-"
        print(f"{dashes_2}{n_count * '*'}{dashes_2}")
for n in range(1, number - (int((number + 1)/2)) + 1):
    print(f"|{(number - 2) * '*'}|")
