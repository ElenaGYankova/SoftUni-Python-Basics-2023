tournament_name = input()
wins, looses, total_matches = 0, 0, 0

while tournament_name != "End of tournaments":
    tournament_matches = int(input())
    for current_match in range(1, tournament_matches + 1):
        user_team_points = int(input())
        opponent_team_points = int(input())
        balance = user_team_points - opponent_team_points
        if balance > 0:
            wins += 1
            print(f"Game {current_match} of tournament {tournament_name}: win with {balance} points.")
        elif balance < 0:
            looses += 1
            print(f"Game {current_match} of tournament {tournament_name}: lost with {abs(balance)} points.")

    total_matches += tournament_matches
    tournament_name = input()
else:
    winning_percentage = looses_percentage = 0
    if total_matches > 0:
        winning_percentage = 100 * wins / total_matches
        looses_percentage = 100 * looses / total_matches
    print(f"{winning_percentage:.2f}% matches win\n"
          f"{looses_percentage:.2f}% matches lost")
