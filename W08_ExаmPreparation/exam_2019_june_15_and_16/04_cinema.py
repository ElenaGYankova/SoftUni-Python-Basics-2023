cinema_capacity = int(input())

total_income = 0
command = input()
while not command == "Movie time!":
    current_people = int(command)
    if cinema_capacity < current_people:
        print("The cinema is full.")
        break
    cinema_capacity -= current_people

    current_cost = current_people * 5
    if not current_people % 3:
        current_cost -= 5
    total_income += current_cost

    command = input()
else:
    print(f"There are {cinema_capacity} seats left in the cinema.")

print(f"Cinema income - {total_income} lv.")
