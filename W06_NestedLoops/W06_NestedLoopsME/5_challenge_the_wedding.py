male_clients = int(input())
female_clients = int(input())
max_tables = int(input())
counter = 0

for i in range(1, male_clients + 1):
    for j in range(1, female_clients + 1):
        if counter >= max_tables:
            break
        print(f"({i} <-> {j})", end=" ")
        counter += 1
