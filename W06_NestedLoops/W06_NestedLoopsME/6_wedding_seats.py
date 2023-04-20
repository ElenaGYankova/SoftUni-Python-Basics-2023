last_sector = input()
rows_first_sector = int(input())
odd_row_seats = int(input())
seats = 0

for a in range(ord("A"), ord(last_sector) + 1):
    rows_first_sector += 1
    for b in range(1, rows_first_sector):
        if b % 2 == 0:
            for c in range(ord("a"), ord("a") + odd_row_seats + 2):
                print(f"{chr(a)}{b}{chr(c)}")
                seats += 1
        else:
            for c in range(ord("a"), ord("a") + odd_row_seats):
                print(f"{chr(a)}{b}{chr(c)}")
                seats += 1
print(seats)
