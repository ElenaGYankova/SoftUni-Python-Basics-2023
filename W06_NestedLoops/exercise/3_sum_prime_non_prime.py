sum_prime = 0
sum_non_prime = 0
stop_command = False

while not stop_command:
    command = input()
    if command == "stop":
        stop_command = True
        break

    command = int(command)
    if command < 0:
        print("Number is negative.")
        continue

    is_prime = True
    for number in range(2, command):
        if command % number == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += command
    else:
        sum_non_prime += command

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
