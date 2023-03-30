from math import floor
tournaments_participated = int(input())
starting_points = int(input())
ranklist_points = 0
wins = 0
for i in range(tournaments_participated):
    tournament_stage = input()
    if tournament_stage == "W":
        ranklist_points += 2000
        wins += 1
    elif tournament_stage == "F":
        ranklist_points += 1200
    elif tournament_stage == "SF":
        ranklist_points += 720
p_wins = (wins / tournaments_participated) * 100
average_points = ranklist_points / tournaments_participated
final_points = ranklist_points + starting_points
print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{p_wins:.2f}%")