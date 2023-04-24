best_player = ''
best_score = 0
is_hat_trick = False

while best_score < 10:
    player_name = input()
    if player_name == "END":
        break
    count_goals = int(input())
    if count_goals > best_score:
        best_player = player_name
        best_score = count_goals
    elif count_goals >= 3:
        is_hat_trick = True
    else:
        is_hat_trick = False

print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")
