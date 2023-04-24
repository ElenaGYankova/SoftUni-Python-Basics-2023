tournament_days = int(input())

day_winner = 0
total_money_earned = 0

for days in range(tournament_days):
    sport = input()
    charity = 0
    wins = 0
    loses = 0
    while sport != "Finish":
        result = input()
        if result == "win":
            wins += 1
            charity += 20

        elif result == "lose":
            loses += 1

        sport = input()
    if wins > loses:
        day_winner += 1
        charity *= 1.10

    total_money_earned += charity

if day_winner > tournament_days // 2:
    total_money_earned *= 1.2
    print(f"You won the tournament! Total raised money: {total_money_earned:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_earned:.2f}")
