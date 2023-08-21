start = int(input())
end = int(input())
magic_number = int(input())

counter = 0
combinations_found = False
for first in range(start, end + 1):
    for second in range(start, end + 1):
        counter += 1
        if first + second == magic_number:
            combinations_found = True
            print(f"Combination N:{counter} ({first} + {second} = {magic_number})")
            break
    if combinations_found:
        break
else:
    print(f"{counter} combinations - neither equals {magic_number}")

