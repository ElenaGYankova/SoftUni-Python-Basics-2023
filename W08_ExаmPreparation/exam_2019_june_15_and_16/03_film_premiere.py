movie_title = input()
pack_for_movie = input()
tickets_count = int(input())

ticket_price = None
if movie_title == "John Wick":
    if pack_for_movie == "Drink":
        ticket_price = 12
    elif pack_for_movie == "Popcorn":
        ticket_price = 15
    elif pack_for_movie == "Menu":
        ticket_price = 19

elif movie_title == "Star Wars":
    if pack_for_movie == "Drink":
        ticket_price = 18
    elif pack_for_movie == "Popcorn":
        ticket_price = 25
    elif pack_for_movie == "Menu":
        ticket_price = 30

elif movie_title == "Jumanji":
    if pack_for_movie == "Drink":
        ticket_price = 9
    elif pack_for_movie == "Popcorn":
        ticket_price = 11
    elif pack_for_movie == "Menu":
        ticket_price = 14

if movie_title == "Star Wars" and tickets_count >= 4:
    ticket_price -= 0.30 * ticket_price

if movie_title == "Jumanji" and tickets_count == 2:
    ticket_price -= 0.15 * ticket_price

total_price = ticket_price * tickets_count

print(f"Your bill is {total_price:.2f} leva.")
