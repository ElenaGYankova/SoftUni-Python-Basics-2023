import sys

counter = 0
best_result = -sys.maxsize
best_title = None
command = input()
while command != "STOP":
    counter += 1
    if not counter < 7:
        print("The limit is reached.")
        break
    movie_title = command
    current_movie_points = 0
    for name in movie_title:
        current_movie_points += ord(name)
        if name.islower():
            current_movie_points -= 2 * len(movie_title)
        elif name.isupper():
            current_movie_points -= len(movie_title)

    if current_movie_points > best_result:
        best_result = current_movie_points
        best_title = movie_title

    command = input()

print(f"The best movie for you is {best_title} with {best_result} ASCII sum.")
