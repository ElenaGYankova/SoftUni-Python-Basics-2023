chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

if season in "Spring" "Summer":
    price_c = 2.00
    price_r = 4.10
    price_t = 2.50
elif season in "Autumn" "Winter":
    price_c = 3.75
    price_r = 4.50
    price_t = 4.15

if holiday == "Y":
    price_c *= 1.15
    price_r *= 1.15
    price_t *= 1.15

bouquet = chrysanthemums * price_c + roses * price_r + tulips * price_t

if season == "Spring" and tulips > 7:
    bouquet *= 0.95
if season == "Winter" and roses >= 10:
    bouquet *= 0.90
if chrysanthemums + roses + tulips > 20:
    bouquet *= 0.80

final_price = bouquet + 2
print(f"{final_price:.2f}")
