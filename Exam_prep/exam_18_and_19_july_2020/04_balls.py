# https://judge.softuni.org/Contests/Practice/Index/2507#3

from math import floor

n = int(input())

total_points = 0
red, orange, yellow, white, black, other = 0, 0, 0, 0, 0, 0

for _ in range(n):
    ball_color = input()
    if ball_color == "red":
        red += 1
        total_points += 5
    elif ball_color == "orange":
        orange += 1
        total_points += 10
    elif ball_color == "yellow":
        yellow += 1
        total_points += 15
    elif ball_color == "white":
        white += 1
        total_points += 20
    elif ball_color == "black":
        black += 1
        total_points = floor(total_points / 2)
    else:
        other += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")
