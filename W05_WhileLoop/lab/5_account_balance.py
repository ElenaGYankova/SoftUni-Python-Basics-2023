money = input()
current_sum = 0

while money != "NoMoreMoney":
    if float(money) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(money):.2f}")
    current_sum += float(money)
    money = input()
print(f"Total: {current_sum:.2f}")
