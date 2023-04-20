start = int(input())
end = int(input())

for a in range(start // 1000, end // 1000 + 1):
    for b in range(start % 1000 // 100, end % 1000 // 100 + 1):
        for c in range(start % 100 // 10, end % 100 // 10 + 1):
            for d in range(start % 10, end % 10 + 1):

                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:

                    print(f"{a}{b}{c}{d}", end=" ")

'''
start = int(input())
end = int(input())

for a in range(int(str(start)[0]), int(str(end)[0]) + 1):
    for b in range(int(str(start)[1]), int(str(end)[1]) + 1):
        for c in range(int(str(start)[2]), int(str(end)[2]) + 1):
            for d in range(int(str(start)[3]), int(str(end)[3]) + 1):

                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:

                    print(f'{a}{b}{c}{d}', end=" ")
'''