start = input()
end = input()
blacklist = input()

counter = 0
for a in range(ord(start), ord(end) + 1):
    if a == ord(blacklist):
        continue
    for b in range(ord(start), ord(end) + 1):
        if b == ord(blacklist):
            continue
        for c in range(ord(start), ord(end) + 1):
            if c == ord(blacklist):
                continue
            counter += 1
            print(f"{chr(a)}{chr(b)}{chr(c)}", end=" ")
print(counter)
