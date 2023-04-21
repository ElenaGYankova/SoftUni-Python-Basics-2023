# https://judge.softuni.org/Contests/Practice/Index/1596#5

student_tickets_count = 0
standard_tickets_count = 0
kid_tickets_count = 0
all_tickets_count = 0
while True:
    movie = input()
    if movie == "Finish":
        break

    free_places = int(input())
    current_places = 0
    for _ in range(free_places):
        ticket_type = input()
        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_tickets_count += 1
        elif ticket_type == "standard":
            standard_tickets_count += 1
        elif ticket_type == "kid":
            kid_tickets_count += 1

        current_places += 1

    hall_percent = 100 * current_places / free_places
    print(f"{movie} - {hall_percent:.2f}% full.")

    all_tickets_count += current_places

student_tickets_percent = 100 * student_tickets_count / all_tickets_count
standard_tickets_percent = 100 * standard_tickets_count / all_tickets_count
kid_tickets_percent = 100 * kid_tickets_count / all_tickets_count

print(f"Total tickets: {all_tickets_count}")
print(f"{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.")
print(f"{kid_tickets_percent:.2f}% kids tickets.")
