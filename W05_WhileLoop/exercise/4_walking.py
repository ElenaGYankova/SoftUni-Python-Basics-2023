input_line = input()
steps_count = 0
while input_line != "Going home":
    steps = int(input_line)
    steps_count += steps
    if steps_count >= 10000:
        break

    input_line = input()
if input_line == "Going home":
    steps_home = int(input())
    steps_count += steps_home

diff = abs(10000 - steps_count)
if steps_count >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
