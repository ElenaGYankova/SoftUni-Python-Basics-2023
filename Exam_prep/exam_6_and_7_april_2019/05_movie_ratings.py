# https://judge.softuni.org/Contests/Practice/Index/1596#4

movies_count = int(input())

highest_rating_title = ""
highest_rating_value = 1.00
lowest_rating_title = ""
lowest_rating_value = 20.00
ratings_sum = 0

for _ in range(movies_count):
    movie_title = input()
    movie_rating = float(input())

    if movie_rating > highest_rating_value:
        highest_rating_value = movie_rating
        highest_rating_title = movie_title

    if movie_rating < lowest_rating_value:
        lowest_rating_value = movie_rating
        lowest_rating_title = movie_title

    ratings_sum += movie_rating

average_rating = ratings_sum / movies_count

print(f"{highest_rating_title} is with highest rating: {highest_rating_value:.1f}")
print(f"{lowest_rating_title} is with lowest rating: {lowest_rating_value:.1f}")
print(f"Average rating: {average_rating:.1f}")
