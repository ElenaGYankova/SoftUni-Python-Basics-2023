lily_age = int(input())
washing_machine = float(input())
one_toy_price = int(input())
bday_money = 0
brother_money = 0
counter = 0
toys = 0

for age in range(lily_age):
    counter += 1
    if counter % 2 == 0:
        bday_money += (counter / 2) * 10
        brother_money += 1
    else:
        toys += 1

money_for_toys = one_toy_price * toys
total_money = bday_money - brother_money
diff = abs((money_for_toys + total_money) - washing_machine)
if money_for_toys + total_money >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
