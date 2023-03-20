fruit = input()
day = input()
quantity = float(input())
price = 0
if day in "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" \
        and fruit in "banana" "apple" "orange" "grapefruit" "kiwi" "pineapple" "grapes":
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85

    final_price = price * quantity
    print(f"{final_price:.2f}")

elif day in "Saturday" "Sunday" \
        and fruit in "banana" "apple" "orange" "grapefruit" "kiwi" "pineapple" "grapes":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20

    final_price = price * quantity
    print(f"{final_price:.2f}")

else:
    print("error")