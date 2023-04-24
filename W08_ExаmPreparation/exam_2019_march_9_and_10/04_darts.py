player_name = input()

leg_points = 301
successful_shots = 0
unsuccessful_shots = 0
is_retire = False
current_points = 0
while leg_points > 0:
    field_type = input()
    if field_type == "Retire":
        is_retire = True
        break
    elif field_type == "Single":
        current_points = 1 * int(input())
    elif field_type == "Double":
        current_points = 2 * int(input())
    elif field_type == "Triple":
        current_points = 3 * int(input())

    if leg_points - current_points < 0:
        unsuccessful_shots += 1
    else:
        successful_shots += 1
        leg_points -= current_points

if is_retire:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
else:
    print(f"{player_name} won the leg with {successful_shots} shots.")
