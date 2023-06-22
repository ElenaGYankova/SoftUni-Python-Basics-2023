day_goal = int(input())

goal_complete = False
money = 0

while not goal_complete:
    command = input()
    if command == "closed":
        break
    elif command == "haircut":
        command_2 = input()
        if command_2 == "mens":
            money += 15
            if money >= day_goal:
                goal_complete = True
                break
        elif command_2 == "ladies":
            money += 20
            if money >= day_goal:
                goal_complete = True
                break
        elif command_2 == "kids":
            money += 10
            if money >= day_goal:
                goal_complete = True
                break
    elif command == "color":
        command_3 = input()
        if command_3 == "touch up":
            money += 20
            if money >= day_goal:
                goal_complete = True
                break
        elif command_3 == "full color":
            money += 30
            if money >= day_goal:
                goal_complete = True
                break

diff = day_goal - money
if goal_complete:
    print("You have reached your target for the day!")
    print(f"Earned money: {money}lv.")
else:
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {money}lv.")
