championship_stage = input()
ticket_type = input()
ticket_count = int(input())
trophy_picture = input()

ticket_price = 0
if championship_stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90

elif championship_stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40

elif championship_stage == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

tickets_cost = ticket_price * ticket_count
if tickets_cost > 4000:
    tickets_cost -= 0.25 * tickets_cost
elif tickets_cost > 2500:
    if trophy_picture == "Y":
        tickets_cost -= 0.10 * tickets_cost
        tickets_cost += 40 * ticket_count
    elif trophy_picture == "N":
        tickets_cost -= 0.10 * tickets_cost
else:
    if trophy_picture == "Y":
        tickets_cost += 40 * ticket_count
    elif trophy_picture == "N":
        pass

print(f"{tickets_cost:.2f}")
