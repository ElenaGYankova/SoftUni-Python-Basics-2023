first_player_eggs = int(input())
second_player_eggs = int(input())
out_of_eggs = False

while first_player_eggs > 0 and second_player_eggs > 0:
    winner = input()
    if winner == "End":
        break
    if winner == "one":
        second_player_eggs -= 1
    elif winner == "two":
        first_player_eggs -= 1

if winner == "one":
    print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
elif winner == "two":
    print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
else:
    print(f"Player one has {first_player_eggs} eggs left.\n"
          f"Player two has {second_player_eggs} eggs left.")
