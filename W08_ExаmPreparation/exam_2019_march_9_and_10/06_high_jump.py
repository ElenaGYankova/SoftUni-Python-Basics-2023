target_height = int(input())

total_tries = 0
failed = False
current_height = target_height - 30

while current_height <= target_height:
    current_tries = 0
    while current_tries < 3:
        total_tries += 1
        current_tries += 1
        jump_height = int(input())
        if jump_height > current_height:
            current_height += 5
            break
    else:
        failed = True

    if failed:
        break

if failed:
    print(f"Tihomir failed at {current_height}cm after {total_tries} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {target_height}cm after {total_tries} jumps.")
