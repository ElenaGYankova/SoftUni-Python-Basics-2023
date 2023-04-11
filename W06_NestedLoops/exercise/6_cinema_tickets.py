line_input = input()

total_count_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0

while line_input != "Finish":
    movie = line_input
    capacity = int(input())

    command_line = input()
    current_movie_count = 0
    while command_line != "End":
        type_ticket = command_line
        total_count_tickets += 1
        current_movie_count += 1
        if type_ticket == "student":
            student_count += 1
        elif type_ticket == "standard":
            standard_count += 1
        else:
            kid_count += 1

        if current_movie_count == capacity:
            break
        command_line = input()

    percentage_current = current_movie_count / capacity * 100
    print(f"{movie} - {percentage_current:.2f}% full.")

    line_input = input()

print(f"Total tickets: {total_count_tickets}")
percent_student = student_count / total_count_tickets * 100
print(f"{percent_student:.2f}% student tickets.")
percent_standard = standard_count / total_count_tickets * 100
print(f"{percent_standard:.2f}% standard tickets.")
percent_kid = kid_count / total_count_tickets * 100
print(f"{percent_kid:.2f}% kids tickets.")

'''
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while not day_end:
    movie_name = input()
    if movie_name == "Finish":
        break
    free_seats = int(input())
    for ticket in range(free_seats + 1):
        if ticket == free_seats:
            hall_full_percent = (ticket / free_seats) * 100
            print(f"{movie_name} - {hall_full_percent:.2f}% full.")
            break
        ticket_type = input()
        if ticket_type == "End":
            hall_full_percent = (ticket / free_seats) * 100
            print(f"{movie_name} - {hall_full_percent:.2f}% full.")
            break
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

total_tickets = student_tickets + standard_tickets + kid_tickets
student_tickets_average = (student_tickets / total_tickets) * 100
standard_tickets_average = (standard_tickets / total_tickets) * 100
kid_tickets_average = (kid_tickets / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_average:.2f}% student tickets.")
print(f"{standard_tickets_average:.2f}% standard tickets.")
print(f"{kid_tickets_average:.2f}% kids tickets.")
'''