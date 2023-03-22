exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival = arrival_hour * 60 + arrival_minute

diff = abs(exam_time - arrival)
diff_h = diff // 60
diff_m = diff % 60

if exam_time == arrival:
    print("On time")
elif exam_time > arrival:
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    elif diff < 60:
        print("Early")
        print(f"{diff} minutes before the start")
    elif diff >= 60:
        print("Early")
        print(f"{diff_h}:{diff_m:02d} hours before the start")
elif exam_time < arrival:
    if diff < 60:
        print("Late")
        print(f"{diff} minutes after the start")
    elif diff >= 60:
        print("Late")
        print(f"{diff_h}:{diff_m:02d} hours after the start")
