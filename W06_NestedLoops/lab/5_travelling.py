destination = input()

while destination != "End":
    needed_money = float(input())
    collected_money = 0
    while collected_money < needed_money:
        current_money = float(input())
        collected_money += current_money
    print(f"Going to {destination}!")
    destination = input()

'''
destination = input()
min_budget = float(input())

collected_money = 0
end_of_vacation = False
while not end_of_vacation:
    money = float(input())
    collected_money += money
    if collected_money >= min_budget:
        print(f"Going to {destination}!")
        destination = input()
        if destination == "End": 
            end_of_vacation = True
            break
        min_budget = float(input())
        collected_money = 0 
'''
