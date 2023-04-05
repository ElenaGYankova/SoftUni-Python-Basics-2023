needed_money = float(input())
available_money = float(input())
days = 0
days_spended = 0

while available_money < needed_money:
    action = input()
    action_money = float(input())
    days += 1
    if action == "save":
        available_money += action_money
        days_spended = 0
    else:
        available_money -= action_money
        if available_money < 0:
            available_money = 0
        days_spended += 1
        if days_spended == 5:
            print("You can't save the money.")
            print(days)
            break
else:
    print(f"You saved the money for {days} days.")
