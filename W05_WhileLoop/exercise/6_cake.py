cake_lenght = int(input())
cake_width = int(input())
cake = cake_lenght * cake_width

cake_finished = False
while cake_finished != True:
    command = input()
    if command == "STOP":
        print(f"{cake} pieces are left.")
        break
    else:
        cake -= int(command)
        if cake <= 0:
            cake_finished = True
            break
if cake_finished:
    print(f"No more cake left! You need {abs(cake)} pieces more.")
