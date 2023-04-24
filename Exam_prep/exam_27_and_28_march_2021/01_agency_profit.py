company = input()
adults_count = int(input())
kids_count = int(input())
price_adults_ticket = float(input())
service_price = float(input())

price_kids_ticket = price_adults_ticket * 0.30
adults_ticket_profit = adults_count * (price_adults_ticket + service_price)
kids_ticket_price = kids_count * (price_kids_ticket + service_price)
profit = (adults_ticket_profit + kids_ticket_price) * 0.20

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")
