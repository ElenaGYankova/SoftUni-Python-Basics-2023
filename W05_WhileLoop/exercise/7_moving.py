free_spase_width = int(input())
free_spase_lenght = int(input())
free_spase_high = int(input())
volume = free_spase_lenght * free_spase_width * free_spase_high

volume_is_full = False
finished = False

while not(volume_is_full or finished):
    boxes = input()
    if boxes == "Done":
        finished = True
        print(f"{volume} Cubic meters left.")
    else:
        volume -= int(boxes)
        if volume < 0:
            volume_is_full = True
            print(f"No more free space! You need {abs(volume)} Cubic meters more.")
