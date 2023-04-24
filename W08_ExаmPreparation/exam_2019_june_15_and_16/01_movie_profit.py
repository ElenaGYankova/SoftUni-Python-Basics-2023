movie_title = input()
projection_days = int(input())
ticket_count = int(input())
ticket_price = float(input())
percent_for_cinema = float(input()) / 100

total_tickets_sold = projection_days * ticket_count
total_tickets_cost = total_tickets_sold * ticket_price

movie_profit = (1 - percent_for_cinema) * total_tickets_cost

print(f"The profit from the movie {movie_title} is {movie_profit:.2f} lv.")
