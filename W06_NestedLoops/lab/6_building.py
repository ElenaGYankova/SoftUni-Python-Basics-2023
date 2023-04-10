floors = int(input())
rooms = int(input())

for current_floor in range(floors, 0, -1):
    for current_room in range(rooms):
        if current_floor == floors:
            print(f"L{current_floor}{current_room}", end = " ")
        elif current_floor % 2 == 0:
            print(f"O{current_floor}{current_room}", end = " ")
        else: #elif current_room % 2 != 0:
            print(f"A{current_floor}{current_room}", end = " ")
    print()
