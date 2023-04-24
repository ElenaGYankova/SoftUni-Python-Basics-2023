actor_name = input()
initial_points = float(input())
jury_count = int(input())

target_points = 1250.5
total_actor_points = initial_points
for n in range(jury_count):
    if total_actor_points > target_points:
        break
    appraiser_name = input()
    appraiser_points = float(input())
    current_actor_points = len(appraiser_name) * appraiser_points / 2
    total_actor_points += current_actor_points

if total_actor_points > target_points:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_actor_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {target_points - total_actor_points:.1f} more!")
