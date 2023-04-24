rent = int(input())

statuettes = rent - (rent * 0.30)
catering = statuettes - (statuettes * 0.15)
sounding = catering / 2

total = rent + statuettes + catering + sounding
print(f"{total:.2f}")
