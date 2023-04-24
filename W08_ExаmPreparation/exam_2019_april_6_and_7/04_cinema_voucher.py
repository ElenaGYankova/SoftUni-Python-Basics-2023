# https://judge.softuni.org/Contests/Practice/Index/1596#3

voucher_value = int(input())

tickets_count = 0
others_count = 0
while voucher_value > 0:
    purchase_value = 0
    purchase = input()
    if purchase == "End":
        break

    if len(purchase) > 8:
        purchase_value = ord(purchase[0]) + ord(purchase[1])
        if voucher_value >= purchase_value:
            tickets_count += 1
        else:
            break
    else:
        purchase_value = ord(purchase[0])
        if voucher_value >= purchase_value:
            others_count += 1
        else:
            break

    voucher_value -= purchase_value

print(f"{tickets_count}\n{others_count}")
