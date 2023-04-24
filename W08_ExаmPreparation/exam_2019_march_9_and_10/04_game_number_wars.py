first_player_name = input()
second_player_name = input()

first_player_score = 0
second_player_score = 0
end_flag = False

while not end_flag:
    first_player_card = input()
    if first_player_card == "End of game":
        print(f"{first_player_name} has {first_player_score} points\n"
              f"{second_player_name} has {second_player_score} points")
        break

    second_player_card = input()

    first_player_card = int(first_player_card)
    second_player_card = int(second_player_card)

    if first_player_card > second_player_card:
        first_player_score += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        second_player_score += second_player_card - first_player_card
    else:
        end_flag = True

        first_player_card = int(input())
        second_player_card = int(input())
        print("Number wars!")
        if first_player_card > second_player_card:
            print(f"{first_player_name} is winner with {first_player_score} points")
        else:
            print(f"{second_player_name} is winner with {second_player_score} points")
