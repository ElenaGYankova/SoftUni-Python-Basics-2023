# https://judge.softuni.org/Contests/Practice/Index/1538#8

from math import floor

tournaments_count = int(input())
initial_points = int(input())

season_points = 0
tournaments_wins = 0
for _ in range(tournaments_count):
    tournament_stage = input()
    if tournament_stage == "W":
        season_points += 2000
        tournaments_wins += 1
    elif tournament_stage == "F":
        season_points += 1200
    elif tournament_stage == "SF":
        season_points += 720

final_points = season_points + initial_points
average_points = floor(season_points / tournaments_count)
winning_percentage = 100 * tournaments_wins / tournaments_count

print(f"Final points: {final_points}\n"
      f"Average points: {average_points}\n"
      f"{winning_percentage:.2f}%")


