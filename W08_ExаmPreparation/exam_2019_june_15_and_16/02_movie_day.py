shooting_time = int(input())
scenes_count = int(input())
scene_time = int(input())

total_time = 0
total_time += 0.15 * shooting_time
total_time += scenes_count * scene_time

if total_time <= shooting_time:
    print(f"You managed to finish the movie on time! You have {round(shooting_time - total_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(total_time - shooting_time)} minutes.")
